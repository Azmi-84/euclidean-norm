# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.17.0",
#     "pyzmq",
# ]
# ///

import marimo

__generated_with = "0.17.7"
app = marimo.App(width="full")


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _(pd):
    df = pd.read_csv('Modules/Module-13/student_data.csv')
    df
    return (df,)


@app.cell
def _(df):
    # adding a column to the dataframe

    df['Country'] = 'Bangladesh'
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df['Total Makrs'] = df['Algorithm Marks']+df['Python Marks']+df['Data Structure Marks']
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _():
    import numpy as np
    return (np,)


@app.cell
def _(df, np):
    df['A+ in DS'] = np.where(df['Data Structure Marks']>90, 'A+', 'A')
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df, np):
    df['Passed in DS'] = np.where(df['Data Structure Marks']>70, 'Passed', 'Failed')
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df['First Name'] = df['FullName'].str.split(' ').str[0]
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df['Last Name'] = df['FullName'].str.split(' ').str[1]
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    from pathlib import Path

    filepath = Path('Modules/Module-13/New_Student_Info.csv')
    df.to_csv(filepath)
    return


if __name__ == "__main__":
    app.run()
