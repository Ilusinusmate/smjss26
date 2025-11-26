"""
Descriptive analysis of survey data with frequency tables
"""
import pandas as pd
import numpy as np
from collections import Counter
import re

def clean_column_name(col):
    """Shorten column names for better readability"""
    # Extract key parts of question
    if '[' in col and ']' in col:
        # Extract text within brackets
        match = re.search(r'\[(.*?)\]', col)
        if match:
            return match.group(1)
    
    # For questions without brackets, take first meaningful part
    parts = col.split('?')[0].split('\n')
    return parts[0][:80] + '...' if len(parts[0]) > 80 else parts[0]

def analyze_column(df, col_name, top_n=10):
    """Analyze a single column and return frequency statistics"""
    
    # Remove NaN values
    valid_responses = df[col_name].dropna()
    
    if len(valid_responses) == 0:
        return None
    
    # Count frequencies
    freq = valid_responses.value_counts()
    
    # Calculate percentages
    percentages = (freq / len(valid_responses) * 100).round(2)
    
    # Create summary dataframe
    summary = pd.DataFrame({
        'Response': freq.index,
        'Frequency': freq.values,
        'Percentage': percentages.values
    })
    
    # Limit to top N responses if there are many unique values
    if len(summary) > top_n:
        summary = summary.head(top_n)
        summary = pd.concat([
            summary,
            pd.DataFrame({
                'Response': ['Others'],
                'Frequency': [freq.iloc[top_n:].sum()],
                'Percentage': [percentages.iloc[top_n:].sum()]
            })
        ], ignore_index=True)
    
    return summary

def generate_descriptive_statistics(df):
    """Generate comprehensive descriptive statistics"""
    
    stats = {
        'total_responses': len(df),
        'total_questions': len(df.columns) - 1,  # Excluding source column
        'response_rate_by_source': df['source'].value_counts().to_dict(),
    }
    
    return stats

def create_frequency_tables(input_file='data/processed/merged_survey_data.xlsx', 
                           output_file='data/processed/frequency_analysis.xlsx'):
    """Create detailed frequency tables for all survey questions"""
    
    print("Loading merged dataset...")
    df = pd.read_excel(input_file)
    
    print(f"Total responses: {len(df)}")
    print(f"Total columns: {len(df.columns)}")
    
    # Generate overall statistics
    stats = generate_descriptive_statistics(df)
    print(f"\nDescriptive Statistics:")
    print(f"Total responses: {stats['total_responses']}")
    print(f"Total questions: {stats['total_questions']}")
    print(f"Responses by source:")
    for source, count in stats['response_rate_by_source'].items():
        print(f"  - {source}: {count}")
    
    # Create Excel writer
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        
        # Write summary statistics
        summary_df = pd.DataFrame([
            ['Total Responses', stats['total_responses']],
            ['Total Questions', stats['total_questions']],
            ['', ''],
            ['Responses by Source', ''],
        ])
        
        for source, count in stats['response_rate_by_source'].items():
            summary_df = pd.concat([
                summary_df,
                pd.DataFrame([[source, count]])
            ], ignore_index=True)
        
        summary_df.columns = ['Metric', 'Value']
        summary_df.to_excel(writer, sheet_name='Summary', index=False)
        
        # Analyze each column (excluding timestamp and source)
        columns_to_analyze = [col for col in df.columns 
                             if col not in ['Carimbo de data/hora', 'source']]
        
        print(f"\nAnalyzing {len(columns_to_analyze)} questions...")
        
        # Create frequency tables for key questions
        # Group similar questions together
        
        # Demographics and background
        demographic_cols = [col for col in columns_to_analyze if any(x in col.lower() for x in 
                           ['role', 'experience', 'team size', 'industry', 'country', 'age', 'gender'])]
        
        # AI usage patterns
        usage_cols = [col for col in columns_to_analyze if any(x in col.lower() for x in 
                     ['which ai', 'how often', 'frequency', 'use ai'])]
        
        # Scrum activities
        scrum_cols = [col for col in columns_to_analyze if any(x in col.lower() for x in 
                     ['sprint', 'backlog', 'planning', 'retrospective', 'daily'])]
        
        # Benefits and challenges
        benefit_cols = [col for col in columns_to_analyze if any(x in col.lower() for x in 
                       ['benefit', 'helpful', 'advantage', 'positive'])]
        
        challenge_cols = [col for col in columns_to_analyze if any(x in col.lower() for x in 
                         ['risk', 'problem', 'challenge', 'negative', 'frustration'])]
        
        # Process each group
        groups = {
            'Demographics': demographic_cols[:20],  # Limit to avoid too many sheets
            'AI Usage': usage_cols[:20],
            'Scrum Activities': scrum_cols[:20],
            'Benefits': benefit_cols[:20],
            'Challenges': challenge_cols[:20],
        }
        
        for group_name, cols in groups.items():
            if not cols:
                continue
                
            print(f"\nProcessing {group_name} ({len(cols)} questions)...")
            
            # Create a combined sheet for this group
            combined_df = pd.DataFrame()
            
            for i, col in enumerate(cols):
                freq_table = analyze_column(df, col, top_n=15)
                
                if freq_table is not None:
                    # Add question header
                    question_short = clean_column_name(col)
                    
                    # Add to combined dataframe
                    header_df = pd.DataFrame({
                        'Response': [f"Q{i+1}: {question_short}"],
                        'Frequency': [''],
                        'Percentage': ['']
                    })
                    
                    combined_df = pd.concat([combined_df, header_df, freq_table, 
                                           pd.DataFrame({'Response': [''], 'Frequency': [''], 'Percentage': ['']})], 
                                          ignore_index=True)
            
            if not combined_df.empty:
                # Write to Excel (sheet name max 31 chars)
                sheet_name = group_name[:31]
                combined_df.to_excel(writer, sheet_name=sheet_name, index=False)
        
        # Create a detailed frequency table for ALL columns
        print("\nCreating comprehensive frequency table...")
        all_freq_data = []
        
        for col in columns_to_analyze[:50]:  # Limit to first 50 to avoid huge file
            freq_table = analyze_column(df, col, top_n=10)
            if freq_table is not None:
                freq_table['Question'] = clean_column_name(col)
                all_freq_data.append(freq_table)
        
        if all_freq_data:
            all_freq_df = pd.concat(all_freq_data, ignore_index=True)
            all_freq_df = all_freq_df[['Question', 'Response', 'Frequency', 'Percentage']]
            all_freq_df.to_excel(writer, sheet_name='All Frequencies', index=False)
    
    print(f"\nFrequency analysis saved to: {output_file}")
    return output_file

if __name__ == "__main__":
    create_frequency_tables()
