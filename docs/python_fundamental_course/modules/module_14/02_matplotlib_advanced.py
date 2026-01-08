# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "matplotlib==3.10.7",
#     "numpy==2.3.4",
#     "pandas[pyarrow]==2.3.3",
# ]
# ///

import marimo

__generated_with = "0.17.8"
app = marimo.App(width="full")


@app.cell
def _():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from pathlib import Path
    return Path, pd, plt


@app.cell
def _(Path, pd):
    filepath = Path("enrollment_data.csv")

    df = pd.read_csv(filepath)
    return (df,)


@app.cell
def _(df):
    df
    return


@app.cell
def _(df, plt):
    plt.plot(df["Year"], df["Programming"], label="Programming")
    plt.plot(df["Year"], df["Digital Marketing"], label="Digital Marketing")
    return


@app.cell
def _(df, plt):
    plt.plot(df["Year"], df["Programming"], label="Programming")
    plt.plot(df["Year"], df["Digital Marketing"], label="Digital Marketing")

    plt.legend()
    return


@app.cell
def _(df, plt):
    plt.plot(df["Year"], df["Programming"], label="Programming", color="#32a852")
    plt.plot(
        df["Year"],
        df["Digital Marketing"],
        label="Digital Marketing",
        color="#8b32a8",
    )

    plt.legend()
    return


@app.cell
def _(df, plt):
    plt.plot(
        df["Year"],
        df["Programming"],
        label="Programming",
        color="#32a852",
        linewidth=5,
    )
    plt.plot(
        df["Year"],
        df["Digital Marketing"],
        label="Digital Marketing",
        color="#8b32a8",
        linewidth=5,
    )

    plt.legend()
    return


@app.cell
def _(df, plt):
    plt.plot(
        df["Year"], df["Programming"], label="Programming", linestyle="dashdot"
    )
    plt.plot(
        df["Year"],
        df["Digital Marketing"],
        label="Digital Marketing",
        linestyle="dotted",
    )

    plt.legend()
    return


@app.cell
def _(df, plt):
    plt.plot(
        df["Year"],
        df["Programming"],
        label="Programming",
        linestyle="dashdot",
        marker="o",
    )
    plt.plot(
        df["Year"],
        df["Digital Marketing"],
        label="Digital Marketing",
        linestyle="dotted",
        marker="o",
    )

    plt.legend()
    return


@app.cell
def _(df, plt):
    plt.plot(
        df["Year"],
        df["Programming"],
        label="Programming",
        linestyle="dashdot",
        marker="o",
        linewidth=3,
    )
    plt.plot(
        df["Year"],
        df["Digital Marketing"],
        label="Digital Marketing",
        linestyle="dotted",
        marker="o",
        linewidth=None,
    )

    plt.grid()
    plt.legend()
    return


@app.cell
def _(Path, pd):
    iq_filepath = Path("student_IQdata.csv")
    iq_df = pd.read_csv(iq_filepath)
    return (iq_df,)


@app.cell
def _(iq_df):
    iq_df
    return


@app.cell
def _(iq_df, plt):
    plt.xlabel("Study Hours")
    plt.ylabel("IQ Score")
    plt.title("Relation between Study Hours and IQ Score")
    plt.scatter(iq_df["Study_Hour"], iq_df["IQ_Score"])

    plt.grid()
    plt.show()
    return


@app.cell
def _(iq_df, plt):
    plt.xlabel("Shoe Size")
    plt.ylabel("IQ Score")
    plt.title("Relation between Shoe Size and IQ Score")
    plt.scatter(iq_df["Shoe_Size"], iq_df["IQ_Score"])

    plt.grid()
    plt.show()
    return


@app.cell
def _(iq_df, plt):
    plt.xlabel("Chilling Hours")
    plt.ylabel("IQ Score")
    plt.title("Relation between Chilling Hours and IQ Score")
    plt.scatter(iq_df["Chilling_Hours"], iq_df["IQ_Score"], marker="x")

    plt.grid()
    plt.show()
    return


@app.cell
def _(iq_df, plt):
    # Histogram
    plt.xlabel("IQ Score")
    plt.ylabel("Frequency")
    plt.title("Frequency of IQ Score among Students")
    plt.hist(iq_df["IQ_Score"])
    plt.grid()
    plt.show()
    return


@app.cell
def _(iq_df, plt):
    plt.xlabel("Study Hours")
    plt.ylabel("Frequency")
    plt.title("Frequency of Study Hours among Students")
    plt.hist(iq_df["Study_Hour"])
    plt.grid()
    plt.show()
    return


@app.cell
def _(iq_df, plt):
    plt.xlabel("Study Hours")
    plt.ylabel("Frequency")
    plt.title("Frequency of Study Hours among Students")
    plt.hist(iq_df["Study_Hour"], bins=15, edgecolor="#f7fcf8")
    plt.grid()
    plt.show()
    return


@app.cell
def _(iq_df, plt):
    plt.xlabel("Study Hours")
    plt.ylabel("Frequency")
    plt.title("Frequency of Study Hours among Students")
    plt.hist(iq_df["Study_Hour"], bins=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    plt.grid()
    plt.show()
    return


@app.cell
def _():
    return


@app.cell
def _(Path, pd):
    ipl_filepath = Path('ipl_2022_dataset.csv')

    ipl_df = pd.read_csv(ipl_filepath)
    return (ipl_df,)


@app.cell
def _(ipl_df):
    ipl_df
    return


@app.cell
def _(ipl_df):
    # team wise group

    team_group = ipl_df.groupby('Team').size()
    team_group
    return (team_group,)


@app.cell
def _(team_group):
    print(team_group.index)
    team_group.values
    return


@app.cell
def _(plt, team_group):
    plt.bar(team_group.index, team_group.values)
    return


@app.cell
def _(plt, team_group):
    plt.pie(team_group, labels=team_group.index)
    plt.show()
    return


@app.cell
def _(plt, team_group):
    plt.pie(team_group, labels=team_group.index, autopct='%1.1f%%')
    plt.show()
    return


@app.cell
def _(plt, team_group):
    plt.pie(team_group, labels=team_group.index, autopct='%1.1f%%', explode=(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1))
    plt.show()
    return


@app.cell
def _(plt, team_group):
    plt.pie(team_group, labels=team_group.index, autopct='%1.1f%%', explode=(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1), shadow=True)
    plt.show()
    return


@app.cell
def _(plt, team_group):
    plt.pie(team_group, labels=team_group.index, autopct='%1.1f%%', explode=(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1), shadow=True, radius=1.5)
    plt.show()
    return


if __name__ == "__main__":
    app.run()
