# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.17.0",
#     "numpy==2.3.4",
#     "pandas[pyarrow]==2.3.3",
#     "pyzmq",
# ]
# ///

import marimo

__generated_with = "0.17.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import numpy as np
    import pandas as pd
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
    **[Python Class Method vs Static Method vs Instance Method](https://realpython.com/instance-class-and-static-methods-demystified/)**
    """)
    return


@app.cell
def _():
    from demo import DemoClass

    obj = DemoClass()
    obj.instance_method()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
