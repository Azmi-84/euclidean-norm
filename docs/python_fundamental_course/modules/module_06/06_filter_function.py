import marimo

__generated_with = "0.18.0"
app = marimo.App()


@app.cell
def _():
    # filter is a very powerful function for segregation of data based on our demands

    numbers = [val for val in range(2, 50, 2)]
    print(numbers[-1])

    even = list(map(lambda val: val % 2 == 0, numbers))
    print(even)

    even = list(filter(lambda val: val % 2 == 0, numbers))
    print(even)

    even = list(filter(lambda val: val > 20, numbers))
    print(even)
    return


@app.cell
def _():
    data = [1, "", None, None, True, False]

    cleaned_data = list(filter(None, data))
    print(cleaned_data)
    return


@app.cell
def _():
    strings = "Hello world, Welcome to the age of artificial intelligence (AI)"

    strings = list(map(str.upper, strings))
    print(strings)

    strings = "".join(strings)
    print(strings)
    return (strings,)


@app.cell
def _(strings):
    vowel = list(filter(lambda ch: ch in "aAeEiIoOuU", strings))
    print(vowel)

    vowel = list(set(vowel))
    print(vowel)
    return


if __name__ == "__main__":
    app.run()
