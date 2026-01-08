import marimo

__generated_with = "0.18.0"
app = marimo.App()


@app.cell
def _():
    # reduce() function can provide result according to our defined logic from an iterable

    from functools import reduce

    lst = [val for val in range(2, 34, 3)]

    summation = reduce(lambda x, y: x + y, lst)
    print(summation)
    return lst, reduce


@app.cell
def _(lst, reduce):
    max_val = reduce(lambda x, y: x if x > y else y, lst)
    print(max_val)
    return


if __name__ == "__main__":
    app.run()
