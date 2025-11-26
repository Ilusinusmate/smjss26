"""
Merge survey datasets and create unified Excel file
"""
import pandas as pd
import os

def merge_survey_data():
    """Merge the two survey datasets into a unified Excel file"""
    
    # Read both datasets
    df1 = pd.read_excel('data/raw/Exploring the Use of AI Chat Assistants in Scrum (respostas).xlsx')
    df2 = pd.read_excel('data/raw/Exploring the Use of AI Chat Assistants in Scrum - Udemy (Responses).xlsx')
    
    # Add source column to identify origin
    df1['source'] = 'Survey 1 (respostas)'
    df2['source'] = 'Survey 2 (Udemy)'
    
    # Merge datasets
    df_merged = pd.concat([df1, df2], ignore_index=True)
    
    print(f"Dataset 1 shape: {df1.shape}")
    print(f"Dataset 2 shape: {df2.shape}")
    print(f"Merged dataset shape: {df_merged.shape}")
    print(f"\nTotal responses: {len(df_merged)}")
    print(f"Responses from Survey 1: {len(df1)}")
    print(f"Responses from Survey 2: {len(df2)}")
    
    # Save merged dataset
    output_path = 'data/processed/merged_survey_data.xlsx'
    df_merged.to_excel(output_path, index=False)
    print(f"\nMerged dataset saved to: {output_path}")
    
    return df_merged

if __name__ == "__main__":
    df = merge_survey_data()
