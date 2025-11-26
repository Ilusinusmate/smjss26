"""
Create visualizations for survey data analysis
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

def ensure_output_dir():
    """Ensure output directory exists"""
    os.makedirs('outputs/plots', exist_ok=True)

def plot_response_distribution(df):
    """Plot distribution of responses by source"""
    ensure_output_dir()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    source_counts = df['source'].value_counts()
    bars = ax.bar(range(len(source_counts)), source_counts.values, 
                  edgecolor='black', color=['#3498db', '#e74c3c'])
    
    # Add value labels on bars
    for i, (bar, count) in enumerate(zip(bars, source_counts.values)):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                f'{count}', ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    ax.set_xticks(range(len(source_counts)))
    ax.set_xticklabels(['Survey 1\n(respostas)', 'Survey 2\n(Udemy)'], fontsize=11)
    ax.set_ylabel('Number of Responses', fontsize=12)
    ax.set_title('Distribution of Survey Responses by Source', fontsize=14, fontweight='bold')
    ax.set_ylim(0, max(source_counts.values) * 1.15)
    
    plt.tight_layout()
    plt.savefig('outputs/plots/response_distribution.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: response_distribution.png")
    plt.close()

def plot_likert_scale_question(df, column, title, output_name):
    """Plot a Likert scale question - percentages add up to 100%"""
    ensure_output_dir()
    
    # Define Likert scale order
    likert_order = [
        'Never',
        'Rarely',
        'Sometimes',
        'Often',
        'Always',
        'Very Low',
        'Low',
        'Moderate',
        'High',
        'Very High',
        'Strongly Disagree',
        'Disagree',
        'Neutral',
        'Agree',
        'Strongly Agree',
        'Not at all helpful',
        'Slightly helpful',
        'Moderately helpful',
        'Very helpful',
        'Extremely helpful'
    ]
    
    # Get value counts (excluding NaN)
    valid_responses = df[column].dropna()
    if len(valid_responses) == 0:
        return
    
    total_valid = len(valid_responses)
    freq = valid_responses.value_counts()
    
    # Try to order by Likert scale
    ordered_responses = []
    for scale_val in likert_order:
        if scale_val in freq.index:
            ordered_responses.append(scale_val)
    
    # Add any remaining responses not in the predefined order
    for val in freq.index:
        if val not in ordered_responses:
            ordered_responses.append(val)
    
    # Filter to only include responses that exist
    ordered_responses = [r for r in ordered_responses if r in freq.index]
    
    if not ordered_responses:
        return
    
    # Create plot
    fig, ax = plt.subplots(figsize=(12, 6))
    
    frequencies = [freq[r] for r in ordered_responses]
    # Calculate percentages based on total valid responses (should sum to 100%)
    percentages = [(f/total_valid*100) for f in frequencies]
    
    bars = ax.bar(range(len(ordered_responses)), frequencies, 
                  edgecolor='black', color='#2ecc71')
    
    # Add value labels
    for i, (bar, count, pct) in enumerate(zip(bars, frequencies, percentages)):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{count}\n({pct:.1f}%)', ha='center', va='bottom', fontsize=9)
    
    # Add total percentage check in title
    total_pct = sum(percentages)
    title_with_check = f"{title}\n(n={total_valid}, total={total_pct:.1f}%)"
    
    ax.set_xticks(range(len(ordered_responses)))
    ax.set_xticklabels(ordered_responses, rotation=45, ha='right')
    ax.set_ylabel('Frequency', fontsize=12)
    ax.set_title(title_with_check, fontsize=13, fontweight='bold')
    ax.set_ylim(0, max(frequencies) * 1.25)
    
    plt.tight_layout()
    plt.savefig(f'outputs/plots/{output_name}.png', dpi=300, bbox_inches='tight')
    print(f"✓ Saved: {output_name}.png (n={total_valid}, Σ%={total_pct:.1f}%)")
    plt.close()

def plot_multiple_choice_question(df, column, title, output_name, top_n=10):
    """Plot a multiple choice question with top N responses - percentages based on valid responses"""
    ensure_output_dir()
    
    valid_responses = df[column].dropna()
    if len(valid_responses) == 0:
        return
    
    total_valid = len(valid_responses)
    freq = valid_responses.value_counts().head(top_n)
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Shorten labels if too long
    labels = [str(label)[:60] + '...' if len(str(label)) > 60 else str(label) 
              for label in freq.index]
    
    bars = ax.barh(range(len(freq)), freq.values, edgecolor='black', color='#9b59b6')
    
    # Calculate percentages based on total valid responses
    percentages = [(count / total_valid * 100) for count in freq.values]
    total_shown_pct = sum(percentages)
    
    # Add value labels
    for i, (bar, count, pct) in enumerate(zip(bars, freq.values, percentages)):
        ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
                f'{count} ({pct:.1f}%)', va='center', fontsize=9)
    
    ax.set_yticks(range(len(freq)))
    ax.set_yticklabels(labels, fontsize=9)
    ax.set_xlabel('Frequency', fontsize=12)
    
    # Add sample size and coverage to title
    title_with_info = f"{title}\n(n={total_valid}, showing top {len(freq)}, coverage={total_shown_pct:.1f}%)"
    ax.set_title(title_with_info, fontsize=13, fontweight='bold')
    ax.set_xlim(0, max(freq.values) * 1.15)
    
    plt.tight_layout()
    plt.savefig(f'outputs/plots/{output_name}.png', dpi=300, bbox_inches='tight')
    print(f"✓ Saved: {output_name}.png (n={total_valid}, coverage={total_shown_pct:.1f}%)")
    plt.close()

def create_all_visualizations():
    """Create all visualizations for the survey"""
    
    print("Loading data...")
    df = pd.read_excel('data/processed/merged_survey_data.xlsx')
    
    print(f"\nCreating visualizations for {len(df)} responses...\n")
    
    # 1. Response distribution
    print("Creating response distribution plot...")
    plot_response_distribution(df)
    
    # 2. Find and plot key Likert scale questions
    likert_columns = [col for col in df.columns if any(x in col.lower() for x in 
                     ['how often', 'to what extent', 'do you agree', 'helpful'])]
    
    print(f"\nFound {len(likert_columns)} Likert-scale questions")
    
    # Plot first few Likert questions
    for i, col in enumerate(likert_columns[:10]):  # Limit to 10
        short_title = col.split('?')[0][:80] if '?' in col else col[:80]
        plot_likert_scale_question(df, col, short_title, f'likert_{i+1}')
    
    # 3. Find and plot multiple choice questions
    print("\nCreating multiple choice visualizations...")
    
    # AI tools used
    ai_tool_cols = [col for col in df.columns if 'which ai' in col.lower() or 'what ai' in col.lower()]
    if ai_tool_cols:
        plot_multiple_choice_question(df, ai_tool_cols[0], 
                                     'AI Chat Assistants Used', 
                                     'ai_tools_used', top_n=10)
    
    # Roles
    role_cols = [col for col in df.columns if 'role' in col.lower() and 'scrum' in col.lower()]
    if role_cols:
        plot_multiple_choice_question(df, role_cols[0], 
                                     'Scrum Roles', 
                                     'scrum_roles', top_n=8)
    
    # Experience
    exp_cols = [col for col in df.columns if 'experience' in col.lower() and 'year' in col.lower()]
    if exp_cols:
        plot_multiple_choice_question(df, exp_cols[0], 
                                     'Years of Experience', 
                                     'experience_years', top_n=8)
    
    # Benefits
    benefit_cols = [col for col in df.columns if 'benefits' in col.lower() and 'experienced' in col.lower()]
    if benefit_cols:
        plot_multiple_choice_question(df, benefit_cols[0], 
                                     'Benefits Experienced with AI Chat Assistants', 
                                     'benefits_experienced', top_n=12)
    
    # Challenges
    challenge_cols = [col for col in df.columns if 'problem' in col.lower() or 'frustration' in col.lower()]
    if challenge_cols:
        plot_multiple_choice_question(df, challenge_cols[0], 
                                     'Problems and Frustrations Encountered', 
                                     'problems_frustrations', top_n=12)
    
    print("\n" + "="*50)
    print("All visualizations created successfully!")
    print("Check the 'outputs/plots/' directory")
    print("="*50)

if __name__ == "__main__":
    create_all_visualizations()
