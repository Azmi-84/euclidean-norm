import marimo

__generated_with = "0.17.8"
app = marimo.App()


@app.cell
def _():
    # declaration
    int_tup = (10, 20, 30, 40, 50)
    print(f"Tuple: {int_tup} and its type is: {type(int_tup)}")

    float_tup = (10.5, 20.5, 30.5)
    print(f"Tuple: {float_tup} and its type is: {type(float_tup)}")

    mixed_tup = (10, 20.5, "Hello", [1, 2, 3], (4, 5))
    print(f"Tuple: {mixed_tup} and its type is: {type(mixed_tup)}")
    return


@app.cell
def _():
    tup_01 = (10)
    print(tup_01, type(tup_01))

    tup_02 = (10,)
    print(tup_02, type(tup_02))
    # If we just put a single value in parenthesis, it is considered as int. To make it a tuple, we need to add a comma after the value.

    tup_02 = 10
    print(tup_02, type(tup_02))

    tup_01 = tuple([10, 20, 30])  # we can convert a list to a tuple using the tuple() function
    print(tup_01, type(tup_01))
    return


@app.cell
def _():
    # accessing tuple elements
    _tup = (10, 'mixed', 30.5, False, [1, 2, 3], (1, 2, 3))
    # for i in range(len(_tup)):
        # print(_tup[i], type(_tup[i]), end=' | ')

    for _i in _tup:
        print(_i, type(_i), end=" | ") # without len function python can handle iterator due to it's iterator protocol
    return


@app.cell
def _():
    # immutability
    # tup[0] = 20
    # TypeError: 'tuple' object does not support item assignment
    return


@app.function
# This codebase highlights the importance of proper understanding of core python concept and a function can be use inside the same function.

def deep_count(sequence, target):
    count = 0
    for _item in sequence:
        if _item == target:
            count += 1
        elif isinstance(_item,  (list, tuple, set)):
            count += deep_count(_item, target)
    return count


@app.cell
def _():
    _tup = (10, 10, 24, 24, [10, 2, 3, 4], {10, 2, 3, 4})
    print(_tup.count(10), _tup.index(10)) # only element inside the tuple is counted not inside the nested one

    print(deep_count(_tup, 10))
    return


if __name__ == "__main__":
    app.run()
