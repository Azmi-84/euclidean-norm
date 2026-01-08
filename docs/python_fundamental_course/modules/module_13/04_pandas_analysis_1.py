# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "kagglehub==0.3.13",
#     "pandas==2.3.3",
# ]
# ///

import marimo

__generated_with = "0.17.6"
app = marimo.App(width="full")


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _():
    # import kagglehub

    # path = kagglehub.dataset_download("shivavashishtha/2022-ipl-auction-dataset")
    # print(path)
    return


@app.cell
def _(pd):
    from pathlib import Path

    filepath = Path('Modules/Module-13/New_Student_Info.csv')

    df = pd.read_csv(filepath)
    df
    return (df,)


@app.cell
def _(df):
    df.duplicated()
    return


@app.cell
def _(df):
    df.duplicated().sum()
    return


@app.cell
def _(df):
    df.drop_duplicates()
    return


@app.cell
def _():
    # permenant delete duplicates

    # df.drop_duplicates(inplace=True)
    return


@app.cell
def _(df):
    # deleting according to name basis

    df.drop_duplicates(subset=['CompletionStatus'])
    return


@app.cell
def _(df):
    df.drop_duplicates(subset=['Country'])
    return


@app.cell
def _(df):
    df.drop_duplicates(subset=['CompletionStatus'], keep='last')
    return


@app.cell
def _(df):
    df.isnull()
    return


@app.cell
def _(df):
    df.dropna()
    return


@app.cell
def _(df):
    # having null in all coulms will be consider for removing

    df.dropna(how='all')
    return


@app.cell
def _(df):
    # removing null from python marks columns

    df.dropna(subset=['Python Marks'])
    return


@app.cell
def _(df):
    # removing null from multiple colums

    df.dropna(subset=['Python Marks', 'Data Structure Marks'])
    return


@app.cell
def _(df):
    df.fillna(0)
    return


@app.cell
def _(df):
    df['FullName'].fillna('unknown')
    return


@app.cell
def _(df):
    df['Python Marks'].fillna(df['Python Marks'].mean().round(2))
    return


if __name__ == "__main__":
    app.run()
