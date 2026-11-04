"""
RECORD CHECK - completed Excellent-tier example
================================================
Run from this folder: python template.py
Input: records_sample.csv
Outputs: records_report.csv and status_counts.png

The example uses the provided label,value,limit data. For another lane,
create a CSV with the same three columns (at least five data rows).
"""
from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # allows saving charts in terminals/headless environments
import matplotlib.pyplot as plt

DATA_FILE = Path(__file__).with_name("records_sample.csv")

# 1. LOAD
df = pd.read_csv(DATA_FILE)

# 2. PROCESS
df["percent"] = (df["value"] / df["limit"]) * 100
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)

# 3. OUTPUT - full table, non-OK rows, and counts by status
print("All records:")
print(df)
print("\\nRecords requiring attention:")
print(df[df["status"] != "OK"])
print("\\nCount by status:")
print(df.groupby("status").size())

df.to_csv(DATA_FILE.with_name("records_report.csv"), index=False)
df["status"].value_counts().plot(kind="bar", title="Records by status")
plt.xlabel("Status")
plt.ylabel("Number of records")
plt.tight_layout()
plt.savefig(DATA_FILE.with_name("status_counts.png"))
print("\\nSaved records_report.csv and status_counts.png")
