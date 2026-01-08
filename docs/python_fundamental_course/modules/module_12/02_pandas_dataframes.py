# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "numpy==2.3.4",
#     "pandas==2.3.3",
# ]
# ///

import marimo

__generated_with = "0.17.2"
app = marimo.App(width="full")


@app.cell
def _():
    import pandas as pd
    import numpy as np
    return (pd,)


@app.cell
def _(pd):
    df = pd.read_csv("./student_data.csv")
    return (df,)


@app.cell
def _(df):
    df_c = df.set_index("StudentID")
    # # inplace=True whill modify the original file rather than copying file
    return (df_c,)


@app.cell
def _(df_c):
    # df_c.loc[3:7] # this show error
    df_c.iloc[3:7]
    return


@app.cell
def _(df_c):
    df_c.rename(
        columns={
            "FullName": "Full Name",
            "CompletionStatus": "Completion Status",
            "EnrollmentDate": "Enrollment Date",
        },
        inplace=True,
    )
    df_c
    return


@app.cell
def _(df):
    # row deletion
    # df.drop(0, inplace=True)
    df
    return


@app.cell
def _(df):
    # column deletion
    # df.drop('Instructor', axis=1, inplace=True)
    df
    return


@app.cell
def _(df):
    df.loc[1, 'Python Marks'] = 90
    df.loc[1, 'Completion Status'] = 'Completed'
    df
    return


@app.cell
def _(df):
    df.loc[1:3, 'Python Marks'] += 2
    df
    return


@app.cell
def _(df):
    for i, seris in df.iterrows():
        print(f'{i}: {seris}')
    return


@app.cell
def _(df):
    for k in df.itertuples():
        print(k)
    return


@app.cell
def _():
    # 
    return


if __name__ == "__main__":
    app.run()
