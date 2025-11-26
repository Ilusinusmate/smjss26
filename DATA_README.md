# Data Structure Documentation

This document provides detailed information about the data files, formats, and structure used in the research on AI chat assistants in Scrum.

## Directory Structure

```
data/
├── raw/                                                      # Original survey data
│   ├── Exploring the Use of AI Chat Assistants in Scrum (respostas).xlsx
│   └── Exploring the Use of AI Chat Assistants in Scrum - Udemy (Responses).xlsx
└── processed/                                                # Processed datasets
    ├── merged_survey_data.xlsx                              # Unified dataset
    └── frequency_analysis.xlsx                              # Frequency tables

outputs/
└── plots/                                                    # Generated visualizations
    ├── response_distribution.png
    ├── ai_tools_used.png
    ├── scrum_roles.png
    ├── experience_years.png
    ├── benefits_experienced.png
    ├── problems_frustrations.png
    └── likert_*.png                                         # Likert scale analyses

notebooks/                                                    # Analysis notebooks
└── survey_analysis.ipynb                                    # Interactive analysis

src/                                                          # Source code
├── data_processing/
│   ├── merge_datasets.py                                    # Dataset merging
│   └── descriptive_analysis.py                              # Frequency analysis
└── visualization/
    └── create_plots.py                                      # Visualization generation
```

## Data Files

### Raw Data (`data/raw/`)

#### File 1: Exploring the Use of AI Chat Assistants in Scrum (respostas).xlsx

- **Source**: Primary survey distribution
- **Responses**: 135
- **Columns**: 104 questions + timestamp
- **Format**: Excel (.xlsx)
- **Language**: Mixed (Portuguese and English)

#### File 2: Exploring the Use of AI Chat Assistants in Scrum - Udemy (Responses).xlsx

- **Source**: Udemy course participants
- **Responses**: 24
- **Columns**: 103 questions + timestamp
- **Format**: Excel (.xlsx)
- **Language**: English

### Processed Data (`data/processed/`)

#### merged_survey_data.xlsx

- **Description**: Unified dataset combining both surveys
- **Total Responses**: 159
- **Total Columns**: 105 (104 questions + source identifier)
- **Format**: Excel (.xlsx)

**Column Structure**:

- `Carimbo de data/hora`: Timestamp of response submission
- `source`: Origin of response ('Survey 1 (respostas)' or 'Survey 2 (Udemy)')
- 103 survey questions (various types)

**Additional Column**:

- `source`: Identifies which survey the response came from

#### frequency_analysis.xlsx

- **Description**: Comprehensive frequency tables for all survey questions
- **Format**: Excel (.xlsx) with multiple sheets

**Sheets**:

1. **Summary**: Overall statistics

   - Total responses
   - Responses by source
   - Total questions

2. **Demographics**: Frequency tables for demographic questions

   - Role in Scrum team
   - Years of experience
   - Team size
   - Industry
   - Country

3. **AI Usage**: AI tool usage patterns

   - Which AI tools are used
   - Frequency of use
   - Specific tasks

4. **Scrum Activities**: Usage in Scrum events and activities

   - Sprint Planning
   - Backlog Refinement
   - Retrospectives
   - Daily Standups
   - Other Agile management tasks

5. **Benefits**: Reported benefits

   - Efficiency improvements
   - Quality enhancements
   - Time savings
   - Collaboration improvements

6. **Challenges**: Problems and frustrations

   - Accuracy issues
   - Trust concerns
   - Ethical considerations
   - Technical limitations

7. **All Frequencies**: Comprehensive frequency table for all questions

## Survey Question Categories

### 1. Demographics and Background (Questions 1-10)

- Current role in Scrum team
- Years of experience with Agile/Scrum
- Team size
- Industry sector
- Country/Region
- Age range
- Gender (optional)

### 2. AI Tool Usage (Questions 11-20)

- Which AI chat assistants are used
- Frequency of use
- Duration of use
- Primary use cases
- Integration with existing tools

### 3. Scrum Event Support (Questions 21-40)

#### Sprint Planning

- Story estimation support
- Capacity planning
- Sprint goal definition
- Task breakdown
- Risk identification

#### Backlog Refinement

- User story creation
- Acceptance criteria definition
- Story splitting
- Prioritization support
- Technical spike definition

#### Sprint Retrospective

- Action item generation
- Improvement suggestions
- Root cause analysis
- Team feedback synthesis
- Retrospective format ideas

#### Daily Standup

- Status update preparation
- Impediment identification
- Progress tracking
- Communication support

### 4. Other Agile Management Tasks (Questions 41-60)

- Product roadmap development
- Product vision definition
- Risk management
- Metrics interpretation
- Stakeholder communication
- Team working agreements
- Documentation

### 5. Benefits Assessment (Questions 61-70)

- Perceived helpfulness by role (PO, SM, Developer)
- Specific benefits experienced
- Efficiency improvements
- Agreement with benefit statements:
  - Reduced cognitive load
  - Improved collaboration
  - Accelerated event preparation
  - Better decision-making
  - Increased transparency

### 6. Challenges and Risks (Questions 71-85)

- Problems encountered
- Biggest risks identified
- Concerns about:
  - Reduced understanding
  - Reduced accountability
  - Reduced trust
  - Reduced motivation
- Negative examples

### 7. Future Perspectives (Questions 86-95)

- Future relationship between humans and AI
- Potential role replacement
- Required new skills
- Long-term implications

### 8. Open-Ended Responses (Questions 96-100)

- Example prompts used
- Positive examples
- Negative examples
- Additional comments and suggestions

## Data Types and Formats

### Question Types

1. **Single Choice**: Radio button selection

   - Example: "What is your current role?"
   - Values: Single text value

2. **Multiple Choice**: Checkbox selection

   - Example: "Which AI chat assistants do you use?"
   - Values: Comma-separated text values or multiple rows

3. **Likert Scale**: 5-point agreement scale

   - Example: "To what extent do you agree..."
   - Values:
     - "Strongly Disagree"
     - "Disagree"
     - "Neutral"
     - "Agree"
     - "Strongly Agree"

4. **Frequency Scale**: Usage frequency

   - Values:
     - "Never"
     - "Rarely"
     - "Sometimes"
     - "Often"
     - "Always"

5. **Helpfulness Scale**: Perceived helpfulness

   - Values:
     - "Not at all helpful"
     - "Slightly helpful"
     - "Moderately helpful"
     - "Very helpful"
     - "Extremely helpful"

6. **Open-Ended**: Free text responses
   - Example: "Please describe positive examples..."
   - Values: Text strings of varying length

### Missing Data

- Missing values are represented as `NaN` in pandas
- Empty responses in Excel appear as blank cells
- Some questions were optional, resulting in varying response rates

## Data Processing Pipeline

### 1. Data Merging (`merge_datasets.py`)

```python
# Reads both Excel files
df1 = pd.read_excel('data/raw/file1.xlsx')
df2 = pd.read_excel('data/raw/file2.xlsx')

# Adds source identifier
df1['source'] = 'Survey 1 (respostas)'
df2['source'] = 'Survey 2 (Udemy)'

# Concatenates datasets
df_merged = pd.concat([df1, df2], ignore_index=True)

# Saves unified dataset
df_merged.to_excel('data/processed/merged_survey_data.xlsx', index=False)
```

### 2. Descriptive Analysis (`descriptive_analysis.py`)

For each question:

1. Count frequency of each response
2. Calculate percentage
3. Identify top N responses (default: 10)
4. Group remaining responses as "Others"
5. Create frequency table

Output format:

```
Question | Response | Frequency | Percentage
---------|----------|-----------|------------
Q1       | Option A | 45        | 28.3%
Q1       | Option B | 38        | 23.9%
...
```

### 3. Visualization (`create_plots.py`)

Generates various plot types:

- **Bar charts**: For categorical data
- **Horizontal bar charts**: For questions with many options
- **Grouped bar charts**: For Likert scale questions
- **Stacked bar charts**: For comparing across groups

## Data Quality and Validation

### Quality Checks Performed

1. **Duplicate Detection**: No duplicate responses found
2. **Timestamp Validation**: All responses have valid timestamps
3. **Column Consistency**: Both surveys have matching question structure
4. **Missing Data Analysis**: Documented in frequency tables
5. **Outlier Detection**: Reviewed open-ended responses for spam

### Data Cleaning Steps

1. Standardized column names (preserved original long names)
2. Unified response formats across both surveys
3. Handled missing values appropriately
4. Validated Likert scale responses
5. Cleaned text responses (removed extra whitespace)

## Privacy and Ethics

### Data Anonymization

- No personally identifiable information (PII) is stored
- Email addresses (for interview opt-in) are stored separately and not included in this repository
- All responses are anonymous
- Timestamps are preserved but cannot be linked to individuals

### Ethical Considerations

- Informed consent was obtained from all participants
- Participants were informed about data usage
- Data is used solely for research purposes
- Results are reported in aggregate form

## Data Access and Reuse

### License

The data is provided under [specify license] for research purposes.

### Citation

When using this data, please cite:

```bibtex
@dataset{smjss2026_scrum_survey,
   title={Survey Data: Large Language Models in Scrum Management: Findings from a
Global Survey of Practitioners},
   author={Danyllo Wagner Albuquerque, João Gabriel Salvador Paiva, Mirko Perkusich},
   year={2026},
   publisher={GitHub},
   url={https://github.com/Ilusinusmate/smjss26}
}
```

### Restrictions

- Data may be used for academic research
- Commercial use requires permission
- Redistribution should include proper attribution
- Modifications should be documented

## Technical Specifications

### File Formats

- **Excel (.xlsx)**: OpenXML format, compatible with Excel 2007+
- **PNG images**: 300 DPI resolution for publication quality
- **Python scripts**: Python 3.8+ compatible

### Dependencies

See `requirements.txt` for complete list:

- pandas >= 2.0.0
- openpyxl >= 3.1.0
- matplotlib >= 3.7.0
- seaborn >= 0.12.0
- numpy >= 1.24.0

### System Requirements

- **Memory**: Minimum 4GB RAM (8GB recommended)
- **Storage**: ~100MB for data and outputs
- **Python**: Version 3.8 or higher

## Troubleshooting

### Common Issues

1. **Excel file won't open**: Install openpyxl: `pip install openpyxl`
2. **Encoding errors**: Files are UTF-8 encoded
3. **Missing plots**: Run `create_plots.py` to generate
4. **Memory errors**: Process data in chunks if needed

## Updates and Versioning

- **Version 1.0**: Initial release (2025)
- Future updates will be documented in CHANGELOG.md

## Contact

For questions about the data structure or access:

- Danyllo Wagner Albuquerque: [ORCID](https://orcid.org/0000-0001-5515-7812)
- João Gabriel Salvador Paiva: [ORCID](https://orcid.org/0009-0008-5558-429X)
- Mirko Perkusich: [ORCID](https://orcid.org/0000-0002-9433-4962)

---

**Last Updated**: November 2025
