# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "numpy==2.3.4",
#     "pandas[pyarrow]==2.3.3",
#     "plotly[express]==6.4.0",
# ]
# ///

import marimo

__generated_with = "0.17.6"
app = marimo.App(width="full")


@app.cell
def _():
    import numpy as np
    import pandas as pd
    import plotly.express as px
    from pathlib import Path
    return Path, pd, px


@app.cell
def _(Path, pd):
    _filepath = Path('sns_data.csv')
    df = pd.read_csv(_filepath)
    return (df,)


@app.cell
def _(df):
    df
    return


@app.cell
def _(df, px):
    px.scatter(data_frame=df, x="study_hours", y="test_score")
    return


@app.cell
def _(df, px):
    px.scatter(data_frame=df, x="study_hours", y="test_score", color='gender')
    return


@app.cell
def _(df, px):
    px.scatter(data_frame=df, x="study_hours", y="test_score", color='gender', size='Tshirt_size', hover_data=['hostel', 'subject'])
    return


@app.cell
def _(df, px):
    px.line(data_frame=df, x='study_hours', y='test_score')
    return


@app.cell
def _(df, px):
    px.histogram(data_frame=df, x='attendance_rate')
    return


@app.cell
def _(df, px):
    px.histogram(data_frame=df, x='attendance_rate', color='gender')
    return


@app.cell
def _(df, px):
    px.histogram(data_frame=df, x='class_level', color='gender')
    return


if __name__ == "__main__":
    app.run()
