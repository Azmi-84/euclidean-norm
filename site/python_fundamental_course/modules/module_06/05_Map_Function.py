import marimo

__generated_with = "0.17.2"
app = marimo.App()


@app.cell
def _():
    # map() function is able to use a single function in every single value

    lst = [val for val in range(1, 40, 2)]

    # sqr = lambda x: x**2

    # sqr_list = list(map(sqr, lst))
    sqr_list = list(map(lambda val: val**2 if val % 2 == 0 else (val**3 if val % 3 == 0 else val), lst))
    print(sqr_list)
    return


@app.cell
def _():
    # for string
    strings = "Hello world, Welcome to the age of artificial intelligence (AI)"

    strings = list(map(str.upper, strings))
    print(strings)

    strings = "".join(strings)
    print(strings)
    return


if __name__ == "__main__":
    app.run()
