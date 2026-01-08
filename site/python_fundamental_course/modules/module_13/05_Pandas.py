# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "numpy==2.3.4",
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
    filepath = Path('Modules/Module-13/New_Student_Info.csv')
    df = pd.read_csv(filepath)
    return (df,)


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    # statistical function

    df.dropna()
    return


@app.cell
def _(df):
    df['Data Structure Marks'].sum()
    return


@app.cell
def _(df):
    df['Data Structure Marks'].max()
    return


@app.cell
def _(df):
    df['Data Structure Marks'].min()
    return


@app.cell
def _(df):
    df['Data Structure Marks'].mean()
    return


@app.cell
def _(df):
    df['Data Structure Marks'].median()
    return


@app.cell
def _(df):
    # highest frequency

    df['Data Structure Marks'].mode()
    return


@app.cell
def _(df):
    # standard deviation

    df['Data Structure Marks'].std()
    return


@app.cell
def _(df):
    df[['Data Structure Marks', 'Algorithm Marks', 'Python Marks', 'Total Marks']].corr()
    return


@app.cell
def _(df):
    # sum in different columns

    df[['Data Structure Marks', 'Algorithm Marks', 'Python Marks', 'Total Marks']].sum()
    return


@app.cell
def _(df):
    # row wise summation

    df[['Data Structure Marks', 'Algorithm Marks']].sum(axis=1)
    return


@app.cell
def _(df):
    # min max scaling

    mn = df['Total Marks'].min()
    mx = df['Total Marks'].max()

    df['Scaled Total Marks'] = df['Total Marks'].apply(lambda x: (x-mn)/(mx-mn))
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    # custom-built function

    def grading_system(marks):
        if marks >= 260:
            return 'A+'
        elif marks >= 240:
            return 'A'
        else:
            return 'A-'

    df['Grade'] = df['Total Marks'].apply(grading_system)
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    def marking_system(df):
        a = df['Data Structure Marks']*2
        b = df['Python Marks']*3
        c = df['Algorithm Marks']*4

        return a, b, c

    df['Exceptional Marks'] = df.apply(marking_system, axis=1)
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    # datetime and time data

    df['EnrollmentDate']
    return


@app.cell
def _(df, pd):
    df['EnrollmentDate'] = pd.to_datetime(df['EnrollmentDate'])
    return


@app.cell
def _(df):
    df['EnrollmentDate']
    return


@app.cell
def _(df):
    df['Enrollment Year'] = df['EnrollmentDate'].dt.year
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df['Enrollment Month'] = df['EnrollmentDate'].dt.month
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df, pd):
    df['Finished Date'] = pd.date_range('2025-11-01', '2026-12-31', periods=len(df['EnrollmentDate']))
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df['Time taken to finish'] = df['Finished Date'] - df['EnrollmentDate']
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df.drop(columns=['EnrollmentDate', 'Finished Date'])
    return


@app.cell
def _(df):
    # Group By

    group_by_instructor = df.groupby('Instructor')
    return (group_by_instructor,)


@app.cell
def _(group_by_instructor):
    group_by_instructor.min('Total Marks')
    return


@app.cell
def _(group_by_instructor):
    group_by_instructor.max('Total Marks')
    return


@app.cell
def _(group_by_instructor):
    group_by_instructor.min('Time taken to finish')
    return


@app.cell
def _(group_by_instructor):
    group_by_instructor.max('Time taken to finsh')
    return


@app.cell
def _(group_by_instructor):
    group_by_instructor.first()
    return


@app.cell
def _(group_by_instructor):
    group_by_instructor.last()
    return


if __name__ == "__main__":
    app.run()
