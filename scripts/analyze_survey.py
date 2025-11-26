#!/usr/bin/env python3
"""Generate descriptive statistics for the AI Chat Assistants in Scrum survey."""

from pathlib import Path
from typing import Dict, List, Tuple
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "processed" / "merged_survey_data.xlsx"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_MD = OUTPUT_DIR / "descriptive_stats.md"


def load_data(path: Path) -> pd.DataFrame:
    """Load the merged survey data."""
    df = pd.read_excel(path, engine="openpyxl")
    return df


def value_table(series: pd.Series, total: int) -> List[Dict[str, str]]:
    """Create frequency table for a categorical variable."""
    counts = series.value_counts(dropna=False)
    rows = []
    for value, count in counts.items():
        label = "Missing/No answer" if pd.isna(value) else str(value).strip()
        percent = (count / total) * 100 if total else 0
        rows.append({
            "response": label,
            "count": int(count),
            "percent": f"{percent:.1f}%",
        })
    return rows


def format_markdown_table(rows: List[Dict[str, str]]) -> str:
    """Format rows as markdown table."""
    lines = ["| Response | Count | Percent |", "| --- | ---: | ---: |"]
    for row in rows:
        lines.append(f"| {row['response']} | {row['count']} | {row['percent']} |")
    return "\n".join(lines)


def get_column_short_name(col: str) -> str:
    """Extract short name from long column name."""
    if '[' in col and ']' in col:
        import re
        match = re.search(r'\[(.*?)\]', col)
        if match:
            return match.group(1)
    
    # Take first part before question mark or newline
    parts = col.split('?')[0].split('\n')
    short = parts[0].strip()
    return short[:80] + '...' if len(short) > 80 else short


def build_report(df: pd.DataFrame) -> str:
    """Build comprehensive markdown report."""
    total = len(df)
    
    # Count responses by source
    source_counts = df['source'].value_counts()
    
    lines: List[str] = [
        "# Descriptive Statistics",
        "",
        "## Survey Overview",
        "",
        f"- **Total responses**: {total}",
        f"- **Survey 1 (respostas)**: {source_counts.get('Survey 1 (respostas)', 0)} ({source_counts.get('Survey 1 (respostas)', 0)/total*100:.1f}%)",
        f"- **Survey 2 (Udemy)**: {source_counts.get('Survey 2 (Udemy)', 0)} ({source_counts.get('Survey 2 (Udemy)', 0)/total*100:.1f}%)",
        f"- **Total questions**: {len(df.columns) - 1}",  # Excluding source
        "",
    ]
    
    # Demographics
    lines.append("## Demographics and Background")
    lines.append("")
    
    demographic_questions = [
        col for col in df.columns 
        if any(x in col.lower() for x in ['role', 'experience', 'team size', 'industry', 'country', 'age'])
    ]
    
    for col in demographic_questions:  # Limit to first 10
        if col in ['Carimbo de data/hora', 'source']:
            continue
        
        short_name = get_column_short_name(col)
        lines.append(f"### {short_name}")
        lines.append("")
        
        rows = value_table(df[col], total)
        lines.append(format_markdown_table(rows[:10]))  # Top 10 responses
        
    
    # AI Usage
    lines.append("## AI Chat Assistant Usage")
    lines.append("")
    
    ai_usage_questions = [
        col for col in df.columns 
        if any(x in col.lower() for x in ['which ai', 'how often', 'frequency'])
    ]
    
    for col in ai_usage_questions[:5]:
        short_name = get_column_short_name(col)
        lines.append(f"### {short_name}")
        lines.append("")
        
        rows = value_table(df[col], total)
        lines.append(format_markdown_table(rows[:15]))  # Top 15 responses
        
        if len(rows) > 15:
            lines.append(f"_... and {len(rows) - 15} more responses_")
        lines.append("")
    
    # Helpfulness ratings
    lines.append("## Helpfulness of AI Chat Assistants by Role")
    lines.append("")
    
    helpfulness_cols = [
        col for col in df.columns 
        if 'helpful' in col.lower() and 'scrum accountabilities' in col.lower()
    ]
    
    if helpfulness_cols:
        lines.append("| Role | Not at all helpful | Slightly helpful | Moderately helpful | Very helpful | Extremely helpful | n |")
        lines.append("| --- | ---: | ---: | ---: | ---: | ---: | ---: |")
        
        for col in helpfulness_cols:
            role_name = get_column_short_name(col)
            counts = df[col].value_counts()
            total_valid = df[col].notna().sum()
            
            not_helpful = counts.get('Not at all helpful', 0)
            slightly = counts.get('Slightly helpful', 0)
            moderately = counts.get('Moderately helpful', 0)
            very = counts.get('Very helpful', 0)
            extremely = counts.get('Extremely helpful', 0)
            
            lines.append(f"| {role_name} | {not_helpful} | {slightly} | {moderately} | {very} | {extremely} | {total_valid} |")
        
        lines.append("")
    
    # Benefits
    lines.append("## Perceived Benefits")
    lines.append("")
    
    benefit_cols = [
        col for col in df.columns 
        if 'benefit' in col.lower() and 'agree' in col.lower()
    ]
    
    if benefit_cols:
        lines.append("| Statement | Strongly Disagree | Disagree | Neutral | Agree | Strongly Agree | n |")
        lines.append("| --- | ---: | ---: | ---: | ---: | ---: | ---: |")
        
        for col in benefit_cols[:5]:
            statement = get_column_short_name(col)
            counts = df[col].value_counts()
            total_valid = df[col].notna().sum()
            
            sd = counts.get('Strongly Disagree', 0) + counts.get('Strongly disagree', 0)
            d = counts.get('Disagree', 0)
            n = counts.get('Neutral', 0)
            a = counts.get('Agree', 0)
            sa = counts.get('Strongly Agree', 0) + counts.get('Strongly agree', 0)
            
            lines.append(f"| {statement[:60]}... | {sd} | {d} | {n} | {a} | {sa} | {total_valid} |")
        
        lines.append("")
    
    # Risks
    lines.append("## Perceived Risks of Intensive Use")
    lines.append("")
    
    risk_cols = [
        col for col in df.columns 
        if 'intensive use' in col.lower() and 'could cause' in col.lower()
    ]
    
    if risk_cols:
        lines.append("| Risk | Yes | No | Maybe | n | % Yes |")
        lines.append("| --- | ---: | ---: | ---: | ---: | ---: |")
        
        for col in risk_cols:
            risk_name = get_column_short_name(col)
            counts = df[col].value_counts()
            total_valid = df[col].notna().sum()
            
            yes = counts.get('Yes', 0)
            no = counts.get('No', 0)
            maybe = counts.get('Maybe', 0)
            pct_yes = (yes / total_valid * 100) if total_valid > 0 else 0
            
            lines.append(f"| {risk_name[:50]}... | {yes} | {no} | {maybe} | {total_valid} | {pct_yes:.1f}% |")
        
        lines.append("")
    
    # Footer
    lines.append("---")
    lines.append("")
    lines.append(f"_All percentages are calculated over the {total} total responses._")
    lines.append(f"_Tables show frequency distributions. Missing/No answer responses are included in totals._")
    lines.append("")
    lines.append(f"**Generated from**: `{DATA_PATH.name}`")
    
    return "\n".join(lines)


def main(data_path: Path = DATA_PATH, output_path: Path = OUTPUT_MD) -> None:
    """Main execution function."""
    df = load_data(data_path)
    OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
    report = build_report(df)
    output_path.write_text(report, encoding="utf-8")
    print(f"✓ Saved descriptive statistics to {output_path.relative_to(ROOT)}")
    print(f"  Total responses analyzed: {len(df)}")


if __name__ == "__main__":
    main()
