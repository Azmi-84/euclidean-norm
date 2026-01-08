import marimo

__generated_with = "0.17.2"
app = marimo.App()


@app.cell
def _():
    import something_in_file as info
    info.greeting(' Azmi')
    return


if __name__ == "__main__":
    app.run()
