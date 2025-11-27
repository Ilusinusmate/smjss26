# Supplementary Material: "Large Language Models in Scrum Management: Findings from a Global Survey of Practitioners"

## Overview

This repository contains the supplementary material for the research paper **"Large Language Models in Scrum Management: Findings from a
Global Survey of Practitioners"** submitted to the **Journal of Software and Systems**. The study investigates how Agile practitioners use AI chat assistants (such as ChatGPT, Claude, Gemini) to support Scrum management activities.

## Research Questions

The study addresses the following research questions:

1. **RQ1**: What is the current level of knowledge and usage of LLMs
   among Scrum professionals?
2. **RQ2**: In which Scrum practices (artifacts, events, and roles) are
   LLMs being adopted, and how helpful are they perceived to be?
3. **RQ3**: What benefits do Scrum teams perceive from using LLMs?
4. **RQ4**: What risks and challenges are associated with LLM use
   in Scrum contexts?
5. **RQ5**: What are professionals’ expectations for the future role
   of LLMs in Scrum management activities?

## Methodology

### Survey Design

- **Survey Type**: Online questionnaire distributed to Agile practitioners
- **Target Population**: Scrum Masters, Product Owners, Developers, and other Agile roles
- **Distribution Channels**:
  - Direct distribution to Agile communities
  - Udemy course participants (Scrum certification courses)
- **Total Responses**: 159 participants
  - Survey 1 (respostas): 135 responses
  - Survey 2 (Udemy): 24 responses

### Data Collection

The survey collected data on:

- **Demographics**: Role, experience, team size, industry
- **AI Usage Patterns**: Tools used, frequency, specific tasks
- **Scrum Activities**: Sprint planning, backlog refinement, retrospectives, daily standups
- **Benefits**: Efficiency gains, quality improvements, time savings
- **Challenges**: Accuracy issues, trust concerns, ethical considerations
- **Future Perspectives**: AI's role in Scrum, required skills, potential automation

## Repository Structure

```
smjss26/
├── README.md                  # This file
├── DATA_README.md             # Detailed data documentation
├── OVERVIEW.md                # Quick start guide
├── columns.md                 # Survey columns dictionary
├── requirements.txt           # Python dependencies
├── .gitignore                 # Git ignore patterns
├── CITATION.cff               # Citation information
├── LICENSE                    # License information
├── data/
│   ├── raw/                   # Original survey data (2 Excel files)
│   └── processed/             # Merged and analyzed datasets
│       ├── merged_survey_data.xlsx      # Unified dataset
│       └── frequency_analysis.xlsx      # Frequency tables
├── scripts/
│   └── analyze_survey.py      # Generate descriptive statistics
├── src/
│   ├── data_processing/       # Data cleaning and merging scripts
│   │   ├── merge_datasets.py
│   │   └── descriptive_analysis.py
│   ├── visualization/         # Plotting and visualization scripts
│   │   └── create_plots.py
│   └── generate_summary_report.py
├── notebooks/                 # Jupyter notebooks for analysis
│   └── survey_analysis.ipynb
└── outputs/
    ├── descriptive_stats.md   # Tabular statistics report
    └── plots/                 # Generated visualizations (16 plots)
```

## Setup Instructions

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Ilusinusmate/smjss26
   cd smjss26
   ```

2. **Create virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Data Processing

Merge the two survey datasets:

```bash
python src/data_processing/merge_datasets.py
```

### 2. Generate Descriptive Statistics

Create tabular statistics report:

```bash
python scripts/analyze_survey.py
```

This generates `outputs/descriptive_stats.md` with:

- Survey overview and demographics
- AI usage patterns
- Helpfulness ratings by role
- Perceived benefits (Likert scales)
- Perceived risks
- All percentages add up to 100%

### 3. Visualization

Create all visualizations:

```bash
python src/visualization/create_plots.py
```

This generates 16 plots in `outputs/plots/` including:

- Response distribution by source
- AI tools usage frequency (with coverage %)
- Scrum roles distribution
- Experience levels
- Benefits experienced
- Problems and frustrations
- 10 Likert scale analyses (all totaling 100%)

**Note**: All visualizations now include sample size (n) and percentage validation to ensure accuracy.

### 4. Interactive Analysis

Open the Jupyter notebook for interactive exploration:

```bash
jupyter notebook notebooks/survey_analysis.ipynb
```

## Data Description

For detailed information about data formats, file structures, and survey questions, see:

- [DATA_README.md](DATA_README.md) - Complete data documentation
- [columns.md](columns.md) - Survey columns dictionary (all 104 questions)
- [outputs/descriptive_stats.md](outputs/descriptive_stats.md) - Tabular statistics report

### Key Datasets

- **Raw Data** (`data/raw/`): Original Excel files from survey platforms
- **Merged Data** (`data/processed/merged_survey_data.xlsx`): Unified dataset with 159 responses
- **Frequency Analysis** (`data/processed/frequency_analysis.xlsx`): Detailed frequency tables organized by topic
- **Descriptive Statistics** (`outputs/descriptive_stats.md`): Markdown tables with frequencies and percentages

## Key Findings

### AI Tools Usage

The most commonly used AI chat assistants among participants:

- ChatGPT (OpenAI)
- Claude (Anthropic)
- Gemini (Google)
- GitHub Copilot
- Other specialized tools

### Scrum Activities Supported

Participants reported using AI chat assistants for:

- **Sprint Planning**: Story estimation, capacity planning, sprint goal definition
- **Backlog Refinement**: User story creation, acceptance criteria, prioritization
- **Retrospectives**: Action item generation, improvement suggestions
- **Daily Standups**: Status updates, impediment identification
- **Documentation**: Meeting notes, decision logs, reports

### Benefits Identified

- Time savings in repetitive tasks
- Improved documentation quality
- Enhanced decision-making support
- Better preparation for Scrum events
- Reduced cognitive load

### Challenges Encountered

- Accuracy and reliability concerns
- Context understanding limitations
- Trust and verification needs
- Ethical considerations
- Over-reliance risks

## Visualizations

All generated visualizations are available in the `outputs/plots/` directory:

- `response_distribution.png`: Distribution of survey responses by source
- `ai_tools_used.png`: Most popular AI chat assistants
- `scrum_roles.png`: Distribution of participant roles
- `experience_years.png`: Years of experience in Agile/Scrum
- `benefits_experienced.png`: Top benefits reported
- `problems_frustrations.png`: Common challenges faced
- `likert_*.png`: Likert scale analyses for various questions

## Contributing

This is a research repository. For questions or suggestions:

1. **Issues**: Use GitHub Issues for bug reports or data questions
2. **Discussions**: Use GitHub Discussions for research-related questions
3. **Pull Requests**: Welcome for improvements to analysis scripts

## Citation

If you use this data or code in your work, please cite:

```bibtex
@article{smjss2026_scrum_survey,
   title={Large Language Models in Scrum Management: Findings from a
Global Survey of Practitioners},
   author={Danyllo Wagner Albuquerque, João Gabriel Salvador Paiva, Mirko Perkusich},
   journal={Journal of Software and Systems},
   year={2026},
   note={Supplementary material available at GitHub repository},
   url={https://github.com/Ilusinusmate/smjss26}
}
```

See [CITATION.cff](CITATION.cff) for detailed citation information.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors

- **[Danyllo Wagner Albuquerque](https://orcid.org/0000-0001-5515-7812)**
- **[João Gabriel Salvador Paiva](https://orcid.org/0009-0008-5558-429X)**
- **[Mirko Perkusich](https://orcid.org/0000-0002-9433-4962)**
- **[Matheus Paixão](https://orcid.org/0000-0002-1775-7259)**
- **[Allysson Allex Araújo](https://orcid.org/0000-0003-2108-2335)**
- **[Marcos Kalinowski](https://orcid.org/0000-0003-1445-3425)**

## Acknowledgments

- All survey participants who shared their experiences
- Agile and Scrum communities for their support
- Udemy course participants for their valuable contributions
- Research advisors and mentors

## Disclaimer

This research is conducted for academic purposes. The data represents the experiences and opinions of survey participants at the time of data collection and may not represent all Agile practitioners or contexts.

## Contact

For questions about this research, please contact:

- Danyllo Wagner Albuquerque: [ORCID](https://orcid.org/0000-0001-5515-7812)
- João Gabriel Salvador Paiva: [ORCID](https://orcid.org/0009-0008-5558-429X)
- Mirko Perkusich: [ORCID](https://orcid.org/0000-0002-9433-4962)

---

**Keywords**: Artificial Intelligence, AI Chat Assistants, Scrum, Agile, Software Engineering, Large Language Models, ChatGPT, Project Management
