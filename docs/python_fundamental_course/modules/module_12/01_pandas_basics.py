# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo>=0.17.0",
#     "numpy==2.3.4",
#     "pandas==2.3.3",
#     "pyzmq",
# ]
# ///

import marimo

__generated_with = "0.17.8"
app = marimo.App(width="full")


@app.cell
def _():
    import pandas as pd
    import numpy as np
    from pathlib import Path
    return Path, np, pd


@app.cell
def _(Path, pd):
    filepath = Path('./student_data.csv')
    df = pd.read_csv(filepath)
    df
    return (df,)


@app.cell
def _(df):
    print(type(df))
    # DataFrame is tabular data and Series is a single row or column
    return


@app.cell
def _(df):
    # df['StudentID']
    print(type(df["StudentID"]))
    return


@app.cell
def _(df):
    # _df = pd.read_parquet("Modules/Module-12/students.parquet")
    # _df

    # _df = pd.read_excel("Modules/Module-12/phitron_student_marks.xlsx")
    # _df

    # _df = pd.read_json("Modules/Module-12/data.json")
    # _df

    df.head()
    return


@app.cell
def _(df):
    df.tail()
    return


@app.cell
def _(df, np):
    df.columns

    columns_list = list(df.columns)
    print(columns_list)

    columns_array = np.array(columns_list)
    print(columns_array, columns_array.dtype)
    return


@app.cell
def _(df):
    df.index
    return


@app.cell
def _(df):
    df.info()
    return


@app.cell
def _(df):
    df.sample(10)
    return


@app.cell
def _(df):
    df.describe()
    return


@app.cell
def _(df):
    df['FullName']
    return


@app.cell
def _(df):
    print(type(df['FullName']))
    return


@app.cell
def _(df):
    # df.loc[row_start:row_end, col_start:col_end]

    df.loc[0]
    return


@app.cell
def _(df):
    type(df.loc[0])
    return


@app.cell
def _(df):
    # multiple rows

    df.loc[[2, 3, 19]]
    return


@app.cell
def _(df):
    # multiple rows using range

    df.loc[3:7]
    return


@app.cell
def _(df):
    # single column

    df.loc[:, ['Python Marks']]
    return


@app.cell
def _(df):
    # Multiple Column

    df.loc[:, ['Python Marks', 'Algorithm Marks']]
    return


@app.cell
def _(df):
    # Row with Column

    df.loc[3:7, ['CompletionStatus']]
    return


if __name__ == "__main__":
    app.run()
