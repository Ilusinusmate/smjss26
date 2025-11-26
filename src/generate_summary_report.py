"""
Generate a comprehensive summary report of the survey analysis
"""
import pandas as pd
import os
from datetime import datetime

def generate_summary_report():
    """Generate a comprehensive summary report"""
    
    print("="*70)
    print("SURVEY ANALYSIS SUMMARY REPORT")
    print("="*70)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)
    
    # Load data
    print("\n📊 Loading data...")
    df = pd.read_excel('data/processed/merged_survey_data.xlsx')
    
    # Basic statistics
    print("\n" + "="*70)
    print("1. DATASET OVERVIEW")
    print("="*70)
    print(f"Total Responses: {len(df)}")
    print(f"Total Questions: {len(df.columns) - 1}")  # Excluding source
    print(f"\nResponses by Source:")
    for source, count in df['source'].value_counts().items():
        percentage = (count / len(df)) * 100
        print(f"  • {source}: {count} ({percentage:.1f}%)")
    
    # Data completeness
    print("\n" + "="*70)
    print("2. DATA COMPLETENESS")
    print("="*70)
    
    # Calculate response rate for each column
    response_rates = {}
    for col in df.columns:
        if col not in ['Carimbo de data/hora', 'source']:
            valid_responses = df[col].notna().sum()
            rate = (valid_responses / len(df)) * 100
            response_rates[col] = rate
    
    avg_response_rate = sum(response_rates.values()) / len(response_rates)
    print(f"Average Response Rate: {avg_response_rate:.1f}%")
    print(f"Questions with >90% response rate: {sum(1 for r in response_rates.values() if r > 90)}")
    print(f"Questions with >80% response rate: {sum(1 for r in response_rates.values() if r > 80)}")
    print(f"Questions with >70% response rate: {sum(1 for r in response_rates.values() if r > 70)}")
    
    # Key findings
    print("\n" + "="*70)
    print("3. KEY FINDINGS SUMMARY")
    print("="*70)
    
    # AI Tools
    ai_tool_cols = [col for col in df.columns if 'which ai' in col.lower() or 'what ai' in col.lower()]
    if ai_tool_cols:
        print("\n📱 Most Used AI Chat Assistants:")
        top_tools = df[ai_tool_cols[0]].value_counts().head(5)
        for i, (tool, count) in enumerate(top_tools.items(), 1):
            percentage = (count / df[ai_tool_cols[0]].notna().sum()) * 100
            print(f"  {i}. {tool}: {count} ({percentage:.1f}%)")
    
    # Roles
    role_cols = [col for col in df.columns if 'role' in col.lower() and 'scrum' in col.lower()]
    if role_cols:
        print("\n👥 Participant Roles:")
        top_roles = df[role_cols[0]].value_counts().head(5)
        for i, (role, count) in enumerate(top_roles.items(), 1):
            percentage = (count / df[role_cols[0]].notna().sum()) * 100
            print(f"  {i}. {role}: {count} ({percentage:.1f}%)")
    
    # Experience
    exp_cols = [col for col in df.columns if 'experience' in col.lower() and 'year' in col.lower()]
    if exp_cols:
        print("\n📅 Experience Levels:")
        top_exp = df[exp_cols[0]].value_counts().head(5)
        for i, (exp, count) in enumerate(top_exp.items(), 1):
            percentage = (count / df[exp_cols[0]].notna().sum()) * 100
            print(f"  {i}. {exp}: {count} ({percentage:.1f}%)")
    
    # Benefits
    benefit_cols = [col for col in df.columns if 'benefits' in col.lower() and 'experienced' in col.lower()]
    if benefit_cols:
        print("\n✅ Top Benefits Experienced:")
        top_benefits = df[benefit_cols[0]].value_counts().head(5)
        for i, (benefit, count) in enumerate(top_benefits.items(), 1):
            percentage = (count / df[benefit_cols[0]].notna().sum()) * 100
            benefit_short = benefit[:60] + '...' if len(benefit) > 60 else benefit
            print(f"  {i}. {benefit_short}: {count} ({percentage:.1f}%)")
    
    # Challenges
    challenge_cols = [col for col in df.columns if 'problem' in col.lower() or 'frustration' in col.lower()]
    if challenge_cols:
        print("\n⚠️  Top Challenges Encountered:")
        top_challenges = df[challenge_cols[0]].value_counts().head(5)
        for i, (challenge, count) in enumerate(top_challenges.items(), 1):
            percentage = (count / df[challenge_cols[0]].notna().sum()) * 100
            challenge_short = challenge[:60] + '...' if len(challenge) > 60 else challenge
            print(f"  {i}. {challenge_short}: {count} ({percentage:.1f}%)")
    
    # Files generated
    print("\n" + "="*70)
    print("4. GENERATED FILES")
    print("="*70)
    
    print("\n📁 Data Files:")
    data_files = [
        'data/processed/merged_survey_data.xlsx',
        'data/processed/frequency_analysis.xlsx'
    ]
    for file in data_files:
        if os.path.exists(file):
            size = os.path.getsize(file) / 1024  # KB
            print(f"  ✓ {file} ({size:.1f} KB)")
        else:
            print(f"  ✗ {file} (not found)")
    
    print("\n📊 Visualizations:")
    plot_dir = 'outputs/plots'
    if os.path.exists(plot_dir):
        plots = [f for f in os.listdir(plot_dir) if f.endswith('.png')]
        print(f"  Total plots generated: {len(plots)}")
        for plot in sorted(plots)[:10]:  # Show first 10
            print(f"  ✓ {plot}")
        if len(plots) > 10:
            print(f"  ... and {len(plots) - 10} more")
    else:
        print("  ✗ No plots directory found")
    
    print("\n📓 Notebooks:")
    notebooks = [
        'notebooks/survey_analysis.ipynb'
    ]
    for nb in notebooks:
        if os.path.exists(nb):
            print(f"  ✓ {nb}")
        else:
            print(f"  ✗ {nb} (not found)")
    
    print("\n📄 Documentation:")
    docs = [
        'README.md',
        'DATA_README.md',
        'CITATION.cff',
        'LICENSE',
        '.gitignore'
    ]
    for doc in docs:
        if os.path.exists(doc):
            print(f"  ✓ {doc}")
        else:
            print(f"  ✗ {doc} (not found)")
    
    # Repository structure
    print("\n" + "="*70)
    print("5. REPOSITORY STRUCTURE")
    print("="*70)
    print("""
smjss26/
├── README.md                          ✓ Main documentation
├── DATA_README.md                     ✓ Data documentation
├── CITATION.cff                       ✓ Citation information
├── LICENSE                            ✓ MIT License
├── .gitignore                         ✓ Git ignore patterns
├── requirements.txt                   ✓ Python dependencies
├── data/
│   ├── raw/                          ✓ Original survey data (2 files)
│   └── processed/                    ✓ Merged and analyzed data
├── src/
│   ├── data_processing/              ✓ Data processing scripts
│   └── visualization/                ✓ Visualization scripts
├── notebooks/                         ✓ Jupyter notebooks
└── outputs/
    └── plots/                        ✓ Generated visualizations
    """)
    
    # Next steps
    print("\n" + "="*70)
    print("6. NEXT STEPS")
    print("="*70)
    print("""
1. Review the generated visualizations in outputs/plots/
2. Open the Jupyter notebook for interactive analysis:
   jupyter notebook notebooks/survey_analysis.ipynb
3. Review frequency tables in data/processed/frequency_analysis.xlsx
4. Update author information in README.md and CITATION.cff
5. Add any additional analysis or visualizations as needed
6. Commit to version control (git)
    """)
    
    print("="*70)
    print("REPORT GENERATION COMPLETE")
    print("="*70)

if __name__ == "__main__":
    generate_summary_report()
