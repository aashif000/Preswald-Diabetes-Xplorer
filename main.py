from preswald import text, table, connect, get_df, slider, plotly
import pandas as pd
import plotly.express as px

# Title and description
text("# Diabetes Data Explorer")
text("An interactive dashboard for analyzing the diabetes dataset.")

# 1) Connect to data source as defined in preswald.toml
connect()

# 2) Load the CSV data
df = get_df("diabetes")  # Matches [data.diabetes] in preswald.toml

# Check if the DataFrame loaded correctly
if df is None:
    text("**Error**: Could not find the 'diabetes' dataset. Check your preswald.toml configuration.")
else:
    # 3) Basic data preview
    text("## Data Preview")
    table(df.head(10), title="First 10 rows of data")

    # 4) Descriptive statistics
    text("## Descriptive Statistics")
    desc = df.describe()
    table(desc, title="Statistical Summary")

    # 5) Interactive filter by Glucose
    min_glucose = int(df["Glucose"].min())
    max_glucose = int(df["Glucose"].max())
    text("### Filter Data by Glucose Level")
    glucose_threshold = slider("Minimum Glucose", min_val=min_glucose, max_val=max_glucose, default=100)
    
    filtered_df = df[df["Glucose"] >= glucose_threshold]
    table(filtered_df, title=f"Rows with Glucose ≥ {glucose_threshold}")

    # 6) Scatter plot: Glucose vs. BMI
    text("## Scatter Plot: Glucose vs. BMI")
    scatter_fig = px.scatter(
        filtered_df,
        x="Glucose",
        y="BMI",
        color="Outcome",  # color-coded by diabetes outcome
        title="Glucose vs. BMI (Filtered by Glucose Threshold)",
        labels={"Glucose": "Glucose", "BMI": "BMI"}
    )
    plotly(scatter_fig)

    # 7) Histogram of BMI
    text("## BMI Distribution Histogram")
    hist_fig = px.histogram(
        df,
        x="BMI",
        nbins=20,
        title="Histogram of BMI",
        labels={"BMI": "Body Mass Index"}
    )
    plotly(hist_fig)

    # 8) Pie Chart for Outcome distribution
    text("## Diabetes Outcome Distribution")
    outcome_counts = df["Outcome"].value_counts().reset_index()
    outcome_counts.columns = ["Outcome", "Count"]

    pie_fig = px.pie(
        outcome_counts,
        names="Outcome",
        values="Count",
        title="Proportion of Diabetes Outcomes (0 = No, 1 = Yes)"
    )
    plotly(pie_fig)
