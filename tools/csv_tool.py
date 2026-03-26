import pandas as pd
from langchain.tools import Tool

# Load CSV
df = pd.read_csv("data.csv")

def query_csv(question):
    question = question.lower()

    if "print" in question or "show" in question:
        return df.head().to_string()

    elif "average" in question or "mean" in question:
        return df.mean(numeric_only=True).to_string()

    elif "max" in question:
        return df.max(numeric_only=True).to_string()

    elif "min" in question:
        return df.min(numeric_only=True).to_string()

    elif "summary" in question or "describe" in question:
        return df.describe().to_string()

    else:
        return f"Columns available: {list(df.columns)}"

csv_tool = Tool(
    name="CSV Analyzer",
    func=query_csv,
    description="Use this tool to analyze dataset: print, average, summary, max, min"
)