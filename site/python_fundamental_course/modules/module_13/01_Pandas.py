import marimo

__generated_with = "0.17.6"
app = marimo.App(width="full")


@app.cell
def _():
    import pandas as pd

    data = {
        "Name": ["Alice one", "Bob two", "Cha one", "Dada two", "Esa One"],
        "City": ["Los abcd RK", "New efgh RK", "Los ijkl RKA", "new mnop RKA", "qrst new los rka"],
        "Department": ["EEE", "MPE", "EEE", "CSE", "SWE"],
        "Salary": [10, 20, 30, 40, 50]
    }

    df = pd.DataFrame(data)
    return (df,)


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df.loc[df['Name'].str.contains('one')]
    return


@app.cell
def _(df):
    df.loc[df['Name'].str.contains('one', case=False)]
    return


@app.cell
def _(df):
    df.loc[df['City'].str.contains(r'Los', case=False)]
    return


@app.cell
def _(df):
    # start with los

    df.loc[df['City'].str.contains(r'^Los', case=False)]
    return


@app.cell
def _(df):
    df.loc[df['City'].str.contains(r'RK', case=False)]
    return


@app.cell
def _(df):
    # end with los

    df.loc[df['City'].str.contains(r'RK$', case=False)]
    return


@app.cell
def _(df):
    # names start with vowel

    df.loc[df['Name'].str.contains(r'^[AEIOU]', case=False)]
    return


@app.cell
def _(df):
    # City start with RK or RKA

    df.loc[df['City'].str.contains(r'RK|RKA', case=False)]
    return


if __name__ == "__main__":
    app.run()
