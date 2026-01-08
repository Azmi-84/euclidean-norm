import marimo

__generated_with = "0.17.2"
app = marimo.App()


@app.cell
def _():
    # special, anonymous and inline lambda parameter: expression we don't have to return anything it will auto return and parameter can be multiple but expression is one

    sqr_sum = lambda x, y: x**2 + y**2
    print(sqr_sum(2, 3))
    return


@app.cell
def _():
    chk_even = lambda x: x % 2 == 0
    print(chk_even(10))
    print(chk_even(11))
    return


if __name__ == "__main__":
    app.run()
