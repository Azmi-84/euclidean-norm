# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "matplotlib==3.10.7",
#     "numpy==2.3.4",
#     "pandas==2.3.3",
# ]
# ///

import marimo

__generated_with = "0.17.6"
app = marimo.App(width="full")


@app.cell
def _():
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    return np, plt


@app.cell
def _(np):
    np.random.seed(42)

    hours_one = np.random.randint(2, 20, size=10)
    days = np.linspace(1, 10, 10, retstep=False, dtype="int64")
    return days, hours_one


@app.cell
def _(days, hours_one, plt):
    plt.title("Study Hours vs Days")
    plt.xlabel("Days")
    plt.ylabel("Study Hours")
    plt.plot(days, hours_one)
    return


@app.cell
def _(np):
    hours_two = np.random.randint(3, 30, size=10)
    return (hours_two,)


@app.cell
def _(days, hours_one, hours_two, plt):
    plt.title("Study Hours vs Days")
    plt.xlabel("Days")
    plt.ylabel("Study Hours")
    plt.plot(days, hours_one)
    plt.plot(days, hours_two)
    return


if __name__ == "__main__":
    app.run()
