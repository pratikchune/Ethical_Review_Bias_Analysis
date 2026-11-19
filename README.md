# Ethical Review Report -- Data Science Bias Analysis

A beginner-friendly data analytics project that examines a **synthetic
hiring and recruitment dataset** for differences in candidate selection
outcomes across gender groups. Python is used for data cleaning and
fairness calculations, and Power BI is used to build an interactive
dashboard.

## Project Objectives

-   Inspect and clean recruitment data.
-   Compare applicant counts and selection rates for male and female
    candidates.
-   Calculate Demographic Parity Difference (DPD) and Disparate Impact
    Ratio (DIR).
-   Export analysis results and an ethical review summary.
-   Present results in Power BI.

## Tools and Technologies

-   Python
-   Pandas
-   NumPy
-   Power BI Desktop
-   CSV

## Dataset

File: `dataset/hiring_bias_analysis_dataset.csv`

The synthetic dataset contains 500 sample candidate records with these
columns:

  Column               Description
  -------------------- --------------------------------------
  `Candidate_ID`       Unique candidate identifier
  `Gender`             Candidate gender group (Male/Female)
  `Age`                Candidate age
  `Education`          Education category
  `Experience_Years`   Years of experience
  `Test_Score`         Assessment score
  `Interview_Score`    Interview score
  `Department`         Department applied to
  `Selected`           Selection outcome (Yes/No)

This is demonstration data, not real applicant data. Do not use it to
make actual hiring decisions.

## Project Structure

``` text
Ethical_Review_Bias_Analysis/
├── dataset/
│   └── hiring_bias_analysis_dataset.csv
├── output/
│   ├── cleaned_dataset.csv
│   ├── gender_selection_summary.csv
│   ├── fairness_metrics.csv
│   └── ethical_review_report.txt
├── analysis.py
├── Ethical_Review_Bias_Analysis.pbix
└── README.md
```

The `output/` files are generated when the Python analysis runs. The
Power BI `.pbix` file is created separately in Power BI Desktop.

## Setup and Run

### 1. Install dependencies

Open a terminal in the project folder and run:

``` bash
python -m pip install pandas numpy
```

### 2. Run the analysis

Ensure the dataset is inside the `dataset/` folder, then run:

``` bash
python analysis.py
```

### 3. Generated outputs

The script creates the `output/` folder if it does not exist and
generates:

-   `cleaned_dataset.csv` -- cleaned candidate records.
-   `gender_selection_summary.csv` -- applicant, selected and rejected
    counts, and selection rates by gender.
-   `fairness_metrics.csv` -- calculated fairness indicators.
-   `ethical_review_report.txt` -- findings and recommendations.

## Fairness Metrics

### Selection Rate

`Selected applicants in a group / Total applicants in that group`

### Demographic Parity Difference

`Male selection rate - Female selection rate`

A value closer to zero indicates more similar selection rates. The sign
indicates which group's rate is higher.

### Disparate Impact Ratio

`Lower selection rate / Higher selection rate`

A value closer to 1 indicates more similar selection rates. A value
below 0.80 is commonly used as a screening signal in some contexts; it
is not a universal legal test and does not by itself prove
discrimination.

## Power BI Dashboard

1.  In Power BI Desktop, select **Get Data → Text/CSV**.
2.  Import `output/cleaned_dataset.csv`.
3.  Create KPI cards for total applicants, total selected, male
    selection rate and female selection rate.
4.  Add a gender distribution donut chart.
5.  Add a selected-versus-rejected column chart.
6.  Add KPI cards for DPD and DIR.
7.  Save the report as `Ethical_Review_Bias_Analysis.pbix`.

## Limitations

-   The dataset is synthetic and intended for learning and
    demonstration.
-   A difference in selection rates is a prompt for further
    investigation, not proof of unfair treatment.
-   These metrics do not account for every relevant factor, such as
    job-related qualifications, role differences, sample size or
    intersectional groups.
-   A proper ethical review should examine recruitment criteria, data
    quality, context and applicable laws before drawing conclusions.

## Conclusion

This project demonstrates a basic workflow for reviewing recruitment
data, calculating group-level fairness indicators, documenting potential
disparities and communicating results through a Power BI dashboard.
