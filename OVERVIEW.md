# Quick Start Guide - Survey Analysis Repository

## 📊 What's in this Repository?

This repository contains a complete analysis of survey data exploring how Agile practitioners use AI chat assistants in Scrum. It includes:

- **159 survey responses** from Scrum Masters, Product Owners, and Developers
- **Merged dataset** combining two survey sources
- **Comprehensive frequency analysis** with detailed statistics
- **16 visualizations** showing key findings
- **Interactive Jupyter notebook** for exploration
- **Complete documentation** and citation information

## 🚀 Quick Start

### 1. View the Results (No Setup Required)

Simply browse these files:

- **`outputs/plots/`** - All visualizations (PNG files)
- **`data/processed/frequency_analysis.xlsx`** - Detailed frequency tables
- **`data/processed/merged_survey_data.xlsx`** - Complete dataset

### 2. Run the Analysis (Requires Python)

```bash
# Install dependencies
pip install -r requirements.txt

# Merge datasets
python src/data_processing/merge_datasets.py

# Generate frequency analysis
python src/data_processing/descriptive_analysis.py

# Create visualizations
python src/visualization/create_plots.py

# Generate summary report
python src/generate_summary_report.py
```

### 3. Interactive Analysis

```bash
# Open Jupyter notebook
jupyter notebook notebooks/survey_analysis.ipynb
```

## 📈 Key Statistics

- **Total Responses**: 159
  - Survey 1 (respostas): 135 (84.9%)
  - Survey 2 (Udemy): 24 (15.1%)
- **Total Questions**: 104
- **Visualizations Generated**: 16
- **Average Response Rate**: 49.1%

## 📁 Repository Structure

```
smjss26/
├── 📄 README.md                    # Main documentation
├── 📄 DATA_README.md               # Data structure details
├── 📄 OVERVIEW.md                  # This file
├── 📄 CITATION.cff                 # Citation information
├── 📄 LICENSE                      # MIT License
├── 📄 requirements.txt             # Python dependencies
│
├── 📂 data/
│   ├── 📂 raw/                     # Original survey files (2 Excel files)
│   └── 📂 processed/               # Processed data
│       ├── merged_survey_data.xlsx      # Unified dataset (159 responses)
│       └── frequency_analysis.xlsx      # Frequency tables by topic
│
├── 📂 src/
│   ├── 📂 data_processing/
│   │   ├── merge_datasets.py            # Merge survey data
│   │   └── descriptive_analysis.py      # Generate frequency tables
│   ├── 📂 visualization/
│   │   └── create_plots.py              # Generate all plots
│   └── generate_summary_report.py       # Summary report
│
├── 📂 notebooks/
│   └── survey_analysis.ipynb            # Interactive analysis
│
└── 📂 outputs/
    └── 📂 plots/                        # 16 visualizations
        ├── response_distribution.png
        ├── ai_tools_used.png
        ├── scrum_roles.png
        ├── experience_years.png
        ├── benefits_experienced.png
        ├── problems_frustrations.png
        └── likert_*.png (10 files)
```

## 🔍 What Can You Find?

### Demographics

- Participant roles (Scrum Master, Product Owner, Developer)
- Years of experience with Agile/Scrum
- Team sizes and industries
- Geographic distribution

### AI Usage Patterns

- Which AI tools are used (ChatGPT, Claude, Gemini, etc.)
- Frequency of use
- Specific tasks supported
- Integration approaches

### Scrum Activities

- Sprint Planning support
- Backlog Refinement assistance
- Retrospective facilitation
- Daily Standup preparation
- Documentation and reporting

### Benefits

- Time savings
- Quality improvements
- Efficiency gains
- Better decision-making
- Reduced cognitive load

### Challenges

- Accuracy concerns
- Trust issues
- Context understanding
- Ethical considerations
- Over-reliance risks

### Future Perspectives

- AI's role in Scrum
- Potential automation
- Required new skills
- Human-AI collaboration

## 📊 Available Visualizations

1. **response_distribution.png** - Survey response sources
2. **ai_tools_used.png** - Most popular AI assistants
3. **scrum_roles.png** - Participant role distribution
4. **experience_years.png** - Experience level breakdown
5. **benefits_experienced.png** - Top benefits reported
6. **problems_frustrations.png** - Common challenges
7. **likert_1.png to likert_10.png** - Likert scale analyses for:
   - Usage frequency
   - Helpfulness ratings
   - Agreement with benefit statements
   - Risk perceptions

## 🔧 Technical Requirements

- **Python**: 3.8 or higher
- **Key Libraries**:
  - pandas >= 2.0.0
  - matplotlib >= 3.7.0
  - seaborn >= 0.12.0
  - openpyxl >= 3.1.0
  - jupyter >= 1.0.0

## 📖 Documentation Files

- **README.md** - Comprehensive project documentation
- **DATA_README.md** - Detailed data structure and formats
- **OVERVIEW.md** - This quick start guide
- **CITATION.cff** - Citation information for academic use
- **LICENSE** - MIT License

## 🎯 Use Cases

### For Researchers

- Analyze survey methodology
- Replicate analysis with modifications
- Extend with additional visualizations
- Compare with other studies

### For Practitioners

- Understand current AI usage in Scrum
- Identify best practices
- Learn about common challenges
- Explore future trends

### For Educators

- Teaching material for Agile courses
- Case study for AI in software engineering
- Data analysis examples
- Research methodology examples

## 📝 Citation

If you use this data or code, please cite:

```bibtex
@article{smjss2026_scrum_survey,
   title={Large Language Models in Scrum Management: Findings from a
Global Survey of Practitioners},
   author={Danyllo Wagner Albuquerque, João Gabriel Salvador Paiva, Mirko Perkusich},
   journal={Journal of Software and Systems},
   year={2026},
   url={https://github.com/Ilusinusmate/smjss26}
}
```

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📧 Contact

For questions or collaboration:

- Danyllo Wagner Albuquerque: [ORCID](https://orcid.org/0000-0001-5515-7812)
- João Gabriel Salvador Paiva: [ORCID](https://orcid.org/0009-0008-5558-429X)
- Mirko Perkusich: [ORCID](https://orcid.org/0000-0002-9433-4962)

## 🔗 Related Resources

- [Scrum Guide](https://scrumguides.org/)
- [Agile Alliance](https://www.agilealliance.org/)

---

**Last Updated**: November 25, 2025  
**Version**: 1.0.0  
**Status**: Complete and ready for use
