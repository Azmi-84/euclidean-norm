import marimo

__generated_with = "0.17.2"
app = marimo.App()


@app.cell
def _():
    array_one = [i for i in range(5)]
    _array_two = [i for i in range(5, 10)]
    _add = array_one + _array_two
    print(_add)
    return


@app.cell
def _():
    import numpy as np
    array_one_1 = np.linspace(1, 5, 5, dtype=np.int64)
    _array_two = np.linspace(6, 10, 5, dtype=np.int64)
    print(f'{array_one_1}\n{_array_two}')
    _add = array_one_1 + _array_two
    print(f'summation: {_add}, subtraction: {array_one_1 - _array_two}, multiplication: {array_one_1 * _array_two}, division: {np.round(array_one_1 / _array_two, 3)}')
    print(f'summation: {np.add(array_one_1, _array_two)}, subtraction: {np.subtract(array_one_1, _array_two)}, multiplication: {np.multiply(array_one_1, _array_two)}, division: {np.round(array_one_1 / _array_two, 3)}')
    return array_one_1, np


@app.cell
def _(array_one_1, np):
    sin_vals = np.sin(array_one_1)  # sin, cos, tan takes values in radian unit
    print(np.round(sin_vals, 3))
    deg_con = np.rad2deg(array_one_1)
    print(np.round(deg_con, 3))
    base_ten_log_val = np.log10(array_one_1)
    print(np.round(base_ten_log_val, 3))
    return


@app.cell
def _(array_one_1, np):
    # broadcasting
    array_one_2 = array_one_1 ** 2
    print(array_one_2)
    array_three = np.linspace(5, 15, 10, dtype=np.int64)
    array_three = array_three.reshape(2, 5)
    print(array_three)
    array_three = array_three ** 2
    print(array_three)
    array_four = array_one_2 + array_three
    print(array_four)
    return array_four, array_one_2


@app.cell
def _(array_four, array_one_2, np):
    # comparison
    print(array_one_2)
    print(array_four > array_one_2)
    print(np.all(array_four > array_one_2))
    print(np.any(array_four > array_one_2))
    return


@app.cell
def _(np):
    # inplace sorting
    array_five = np.random.randint(1, 10, size=10)
    print(array_five)
    array_five.sort()
    print(array_five)
    array_six = np.random.randint(1, 10, size=10)
    print(array_six)
    # copying then sorting
    array_sort = np.sort(array_six)
    print(array_sort)
    print(array_six)
    array_four_1 = np.array([[3, 2, 8, 5], [45, 23, 9, 32]])
    two_dim_horizontal_sort = np.sort(array_four_1, axis=1)
    print(two_dim_horizontal_sort)
    two_dim_vertical_sort = np.sort(array_four_1, axis=0)
    # sorting for 2D array: two possibilities, horizontal (axis=1) and vertical (axis=0)
    print(two_dim_vertical_sort)
    return (array_four_1,)


@app.cell
def _(array_four_1, np):
    # searching: np.where(condition, x, y) if true x, otherwise y
    print(array_four_1)
    index = np.where(array_four_1 == 8)
    print(index)
    index = np.where(array_four_1 > 8)
    print(index)
    index = np.where(array_four_1 > 8, array_four_1, 0)
    print(index)
    max_val = np.argmax(array_four_1)
    print(max_val)
    min_val = np.argmin(array_four_1)
    print(min_val)
    return


@app.cell
def _(np):
    # counting
    array_seven = np.random.randint(1, 100, 100)
    print(array_seven)

    no_greater_than_sixty = np.count_nonzero(array_seven>40)
    print(no_greater_than_sixty)
    return


if __name__ == "__main__":
    app.run()
