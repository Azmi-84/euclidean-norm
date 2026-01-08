# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "pandas==2.3.3",
# ]
# ///

import marimo

__generated_with = "0.17.6"
app = marimo.App(width="full")


@app.cell
def _():
    import pandas as pd
    from pathlib import Path
    return Path, pd


@app.cell
def _(Path, pd):
    filepath = Path("Modules/Module-13/student_data.csv")
    df = pd.read_csv(filepath)
    return (df,)


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df["Data Structure Marks"].isnull()
    return


@app.cell
def _(df):
    # unique() function only work on Series not in DataFrame

    df["Instructor"].unique()
    return


@app.cell
def _(df):
    len(df["Instructor"].unique())
    return


@app.cell
def _(df):
    df["Algorithm Marks"].unique()
    return


@app.cell
def _(df):
    len(df["Algorithm Marks"].unique())
    return


@app.cell
def _(df):
    # without null value

    df["Algorithm Marks"].nunique()
    return


@app.cell
def _(df):
    df.nunique()
    return


@app.cell
def _(df):
    df.isnull()
    return


@app.cell
def _(df):
    df['Data Structure Marks'].isnull()
    return


@app.cell
def _(df):
    df['Data Structure Marks'].notnull()
    return


@app.cell
def _(df):
    df['Data Structure Marks'].hasnans
    return


if __name__ == "__main__":
    app.run()
