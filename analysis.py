
import pandas as pd
import numpy as np
from pathlib import Path

# ==========================================
# ETHICAL REVIEW AND BIAS ANALYSIS PROJECT
# ==========================================

BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR / "dataset" / "hiring_bias_analysis_dataset.csv"
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)

print("=" * 55)
print("       ETHICAL REVIEW - BIAS ANALYSIS SYSTEM")
print("=" * 55)

# 1. LOAD DATASET
print("\n1. Loading Dataset...")

df = pd.read_csv(DATASET_PATH)

print("Dataset loaded successfully!")
print("Total Records:", len(df))
print("Total Columns:", len(df.columns))

# 2. DATASET INFORMATION
print("\n2. Dataset Information:")
print(df.info())

# 3. CHECK MISSING VALUES
print("\n3. Checking Missing Values:")

print(df.isnull().sum())

# 4. CHECK DUPLICATES
print("\n4. Checking Duplicate Records:")

duplicates = df.duplicated().sum()
print("Duplicate Records:", duplicates)

df = df.drop_duplicates()

# 5. HANDLE MISSING VALUES
print("\n5. Cleaning Dataset...")

numeric_columns = df.select_dtypes(include=np.number).columns

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

categorical_columns = df.select_dtypes(
    include=["object"]
).columns

for column in categorical_columns:
    if df[column].isnull().any():
        df[column] = df[column].fillna(
            df[column].mode()[0]
        )

# Standardize text values
df["Gender"] = df["Gender"].astype(str).str.strip().str.title()
df["Selected"] = df["Selected"].astype(str).str.strip().str.title()

# Validate selection values
df = df[df["Selected"].isin(["Yes", "No"])]

# SAVE CLEANED DATASET
cleaned_path = OUTPUT_DIR / "cleaned_dataset.csv"
df.to_csv(cleaned_path, index=False)

print("Dataset cleaned successfully!")
print("Cleaned dataset saved:", cleaned_path)

# 6. GENDER DISTRIBUTION
print("\n6. Gender Distribution:")

gender_distribution = df["Gender"].value_counts()

print(gender_distribution)

# 7. SELECTION ANALYSIS
print("\n7. Gender-wise Selection Analysis:")

gender_summary = df.groupby("Gender").agg(
    Applicants=("Candidate_ID", "count"),
    Selected=("Selected", lambda x: (x == "Yes").sum())
)

gender_summary["Rejected"] = (
    gender_summary["Applicants"] - gender_summary["Selected"]
)

gender_summary["Selection_Rate"] = (
    gender_summary["Selected"] /
    gender_summary["Applicants"]
)

print(gender_summary)

gender_summary.to_csv(
    OUTPUT_DIR / "gender_selection_summary.csv"
)

# 8. FAIRNESS METRICS
print("\n8. Calculating Fairness Metrics...")

selection_rates = gender_summary["Selection_Rate"]

if "Male" in selection_rates.index and "Female" in selection_rates.index:

    male_rate = selection_rates["Male"]
    female_rate = selection_rates["Female"]

    demographic_parity_difference = male_rate - female_rate

    higher_rate = max(male_rate, female_rate)
    lower_rate = min(male_rate, female_rate)

    disparate_impact_ratio = (
        lower_rate / higher_rate
        if higher_rate > 0 else np.nan
    )

else:
    raise ValueError(
        "Both Male and Female groups are required "
        "for this fairness comparison."
    )

# 9. DISPLAY RESULTS
print("\n" + "=" * 55)
print("              FAIRNESS ANALYSIS RESULTS")
print("=" * 55)

print(f"Male Selection Rate: {male_rate:.2%}")
print(f"Female Selection Rate: {female_rate:.2%}")

print(
    "Demographic Parity Difference:",
    f"{demographic_parity_difference:.4f}"
)

print(
    "Disparate Impact Ratio:",
    f"{disparate_impact_ratio:.4f}"
)

# 10. IDENTIFY POTENTIAL BIAS
print("\n9. Potential Bias Assessment:")

if disparate_impact_ratio < 0.80:
    bias_status = "Potential adverse impact warning"
    print("WARNING: Selection rates show a potential disparity.")
else:
    bias_status = "No 80% rule warning detected"
    print("No 80% rule warning detected.")

print("Assessment:", bias_status)

print(
    "Note: These metrics are screening indicators, "
    "not proof of discrimination."
)

# 11. SAVE FAIRNESS METRICS
metrics = pd.DataFrame({
    "Metric": [
        "Male Selection Rate",
        "Female Selection Rate",
        "Demographic Parity Difference",
        "Disparate Impact Ratio",
        "Potential Bias Assessment"
    ],
    "Value": [
        round(male_rate, 4),
        round(female_rate, 4),
        round(demographic_parity_difference, 4),
        round(disparate_impact_ratio, 4),
        bias_status
    ]
})

metrics.to_csv(
    OUTPUT_DIR / "fairness_metrics.csv",
    index=False
)

print("\nFairness metrics saved successfully!")

# 12. GENERATE ETHICAL REVIEW REPORT
report_path = OUTPUT_DIR / "ethical_review_report.txt"

with open(report_path, "w", encoding="utf-8") as report:

    report.write("ETHICAL REVIEW REPORT\n")
    report.write("=" * 50 + "\n\n")

    report.write("PROJECT: Hiring and Recruitment Bias Analysis\n\n")

    report.write("1. DATASET INFORMATION\n")
    report.write(f"Total Applicants: {len(df)}\n")
    report.write(f"Total Columns: {len(df.columns)}\n\n")

    report.write("2. GENDER-WISE SELECTION ANALYSIS\n")
    report.write(gender_summary.to_string())
    report.write("\n\n")

    report.write("3. FAIRNESS METRICS\n")
    report.write(f"Male Selection Rate: {male_rate:.2%}\n")
    report.write(f"Female Selection Rate: {female_rate:.2%}\n")

    report.write(
        f"Demographic Parity Difference: "
        f"{demographic_parity_difference:.4f}\n"
    )

    report.write(
        f"Disparate Impact Ratio: "
        f"{disparate_impact_ratio:.4f}\n\n"
    )

    report.write("4. POTENTIAL BIAS ASSESSMENT\n")
    report.write(bias_status + "\n\n")

    report.write("5. RECOMMENDATIONS\n")
    report.write("- Review recruitment selection criteria.\n")
    report.write("- Monitor selection rates across groups.\n")
    report.write("- Use fair and consistent evaluation methods.\n")
    report.write("- Conduct regular fairness audits.\n")
    report.write("- Investigate differences before drawing conclusions.\n\n")

    report.write("6. CONCLUSION\n")
    report.write(
        "The analysis evaluates gender-wise hiring outcomes "
        "using fairness metrics. Further investigation is "
        "required to determine the reasons for any observed "
        "differences.\n"
    )

print("Ethical review report generated successfully!")

# 13. FINAL OUTPUT
print("\n" + "=" * 55)
print("           PROJECT EXECUTION COMPLETED")
print("=" * 55)

print("\nGenerated Files:")

for file in OUTPUT_DIR.iterdir():
    print("-", file.name)

print("\nAll analysis operations completed successfully!")
