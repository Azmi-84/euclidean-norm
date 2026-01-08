# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "matplotlib==3.10.7",
#     "numpy==2.3.4",
#     "pandas[pyarrow]==2.3.3",
#     "seaborn==0.13.2",
# ]
# ///

import marimo

__generated_with = "0.17.7"
app = marimo.App(width="full")


@app.cell
def _():
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    from pathlib import Path
    return Path, np, pd, sns


@app.cell
def _(Path, pd):
    filepath = Path("sns_data.csv")
    df = pd.read_csv(filepath)
    return (df,)


@app.cell
def _(df):
    df
    return


@app.cell
def _(df, sns):
    sns.lineplot(data=df, x="week", y="attendance_rate")
    return


@app.cell
def _(df, sns):
    sns.lineplot(data=df, x="week", y="attendance_rate", errorbar=None)
    return


@app.cell
def _(df, sns):
    sns.lineplot(
        data=df, x="week", y="attendance_rate", hue="gender", errorbar=None
    )
    return


@app.cell
def _(df, sns):
    sns.relplot(
        kind="line",
        data=df,
        x="week",
        y="attendance_rate",
        hue="gender",
        errorbar=None,
    )
    return


@app.cell
def _(df, sns):
    sns.relplot(
        kind="line",
        data=df,
        x="week",
        y="attendance_rate",
        hue="class_level",
        errorbar=None,
    )
    return


@app.cell
def _(df, sns):
    sns.relplot(
        kind="line",
        data=df,
        x="week",
        y="study_hours",
        hue="class_level",
        errorbar=None,
    )
    return


@app.cell
def _(df, sns):
    sns.relplot(
        kind="line",
        data=df,
        x="study_hours",
        y="test_score",
        hue="class_level",
        errorbar=None,
    )
    return


@app.cell
def _(df, sns):
    sns.scatterplot(data=df, x="study_hours", y="test_score")
    return


@app.cell
def _(df, sns):
    sns.scatterplot(data=df, x="study_hours", y="test_score", hue="gender")
    return


@app.cell
def _(df, sns):
    sns.scatterplot(
        data=df, x="study_hours", y="test_score", hue="gender", style="class_level"
    )
    return


@app.cell
def _(df, sns):
    sns.scatterplot(
        data=df, x="study_hours", y="test_score", hue="gender", style="subject"
    )
    return


@app.cell
def _(df, sns):
    sns.scatterplot(
        data=df,
        x="study_hours",
        y="test_score",
        hue="gender",
        style="subject",
        size="Tshirt_size",
    )
    return


@app.cell
def _(df, sns):
    sns.relplot(
        kind="scatter",
        data=df,
        x="study_hours",
        y="test_score",
        hue="gender",
        style="subject",
        size="Tshirt_size",
    )
    return


@app.cell
def _(sns):
    tips_data = sns.load_dataset("tips")
    tips_data
    return (tips_data,)


@app.cell
def _(sns, tips_data):
    sns.relplot(kind="scatter", data=tips_data, x="total_bill", y="tip")
    return


@app.cell
def _(sns, tips_data):
    sns.relplot(kind="scatter", data=tips_data, x="total_bill", y="tip", hue="sex")
    return


@app.cell
def _(sns, tips_data):
    sns.relplot(
        kind="scatter",
        data=tips_data,
        x="total_bill",
        y="tip",
        hue="sex",
        style="time",
    )
    return


@app.cell
def _(Path, pd):
    student_filepath = Path("student_dataset_complete.csv")

    student_df = pd.read_csv(student_filepath)
    student_df
    return (student_df,)


@app.cell
def _(sns, student_df):
    sns.scatterplot(data=student_df, x="study_hours", y="test_score")
    return


@app.cell
def _(sns, student_df):
    sns.scatterplot(data=student_df, x="study_hours", y="test_score", hue="gender")
    return


@app.cell
def _(sns, student_df):
    sns.relplot(
        kind="scatter",
        data=student_df,
        x="study_hours",
        y="test_score",
        hue="gender",
    )
    return


@app.cell
def _(sns, student_df):
    sns.relplot(
        kind="scatter",
        data=student_df,
        x="study_hours",
        y="test_score",
        col="gender",
    )
    return


@app.cell
def _(sns, student_df):
    sns.relplot(
        kind="scatter",
        data=student_df,
        x="study_hours",
        y="test_score",
        col="gender",
        row="hostel",
    )
    return


@app.cell
def _(sns, student_df):
    sns.relplot(
        kind="scatter",
        data=student_df,
        x="study_hours",
        y="test_score",
        col="week",
    )
    return


@app.cell
def _(sns, student_df):
    sns.relplot(
        kind="scatter",
        data=student_df,
        x="study_hours",
        y="test_score",
        col="week",
        col_wrap=2,
    )
    return


@app.cell
def _(sns, student_df):
    # Histogram using Seaborn

    sns.histplot(data=student_df, x="attendance_rate")
    return


@app.cell
def _(sns, student_df):
    sns.histplot(data=student_df, x="attendance_rate", hue="gender")
    return


@app.cell
def _(sns, student_df):
    sns.histplot(data=student_df, x="attendance_rate", hue="gender", bins=15)
    return


@app.cell
def _(sns, student_df):
    sns.histplot(
        data=student_df, x="attendance_rate", hue="gender", bins=10, element="step"
    )
    return


@app.cell
def _(sns, student_df):
    sns.displot(kind="hist", data=student_df, x="attendance_rate", col="gender")
    return


@app.cell
def _(sns, student_df):
    # KDE (Kernal Density Estimation) Plot

    sns.kdeplot(data=student_df, x="attendance_rate")
    return


@app.cell
def _(sns, student_df):
    sns.kdeplot(data=student_df, x="attendance_rate", hue="gender")
    return


@app.cell
def _(sns, student_df):
    sns.kdeplot(data=student_df, x="attendance_rate", hue="gender", fill=True)
    return


@app.cell
def _(sns, student_df):
    # Countplot

    sns.countplot(data=student_df, x="gender")
    return


@app.cell
def _(sns, student_df):
    sns.countplot(data=student_df, x="subject", hue="gender")
    return


@app.cell
def _(sns, student_df):
    # Bar plot

    sns.barplot(data=student_df, x="gender", y="Marks")
    return


@app.cell
def _(sns, student_df):
    sns.barplot(data=student_df, x="gender", y="Marks", errorbar=None)
    return


@app.cell
def _(np, sns, student_df):
    sns.barplot(
        data=student_df, x="gender", y="Marks", errorbar=None, estimator=np.median
    )
    return


@app.cell
def _(np, sns, student_df):
    sns.barplot(
        data=student_df, x="gender", y="Marks", errorbar=None, estimator=np.max
    )
    return


@app.cell
def _(sns, student_df):
    # Regression Plot

    sns.regplot(data=student_df, x="study_hours", y="test_score")
    return


@app.cell
def _(sns, student_df):
    sns.lmplot(data=student_df, x="study_hours", y="test_score")
    return


@app.cell
def _(sns, student_df):
    sns.lmplot(data=student_df, x="study_hours", y="test_score", hue="gender")
    return


@app.cell
def _(student_df):
    student_marks = student_df[
        ["attendance_rate", "study_hours", "gender", "Marks"]
    ]
    student_marks
    return (student_marks,)


@app.cell
def _(sns, student_marks):
    sns.pairplot(data=student_marks)
    return


@app.cell
def _(sns, student_marks):
    sns.pairplot(data=student_marks, kind="hist")
    return


@app.cell
def _(sns, student_marks):
    sns.pairplot(data=student_marks, kind="reg")
    return


@app.cell
def _(sns, student_marks):
    sns.pairplot(data=student_marks, hue="gender")
    return


@app.cell
def _(sns, student_marks):
    sns.pairplot(data=student_marks, hue="gender", kind="reg")
    return


@app.cell
def _(sns, student_df):
    sns.jointplot(data=student_df, x="study_hours", y="Marks")
    return


@app.cell
def _(sns, student_df):
    sns.jointplot(data=student_df, x="study_hours", y="Marks", kind="kde")
    return


@app.cell
def _(sns, student_df):
    sns.jointplot(
        data=student_df, x="study_hours", y="Marks", kind="kde", hue="gender"
    )
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""

        """
    )
    return


if __name__ == "__main__":
    app.run()
