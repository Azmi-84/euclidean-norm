import marimo

__generated_with = "0.17.2"
app = marimo.App()


@app.cell
def _():
    import numpy as np

    array_one = np.random.randint(1, 100, size=(10, 2)) # 10 samples and 2 features
    print(f'{len(array_one)}\n{array_one}\n{array_one.shape}')
    return array_one, np


@app.cell
def _(array_one):
    array_one_1 = array_one.reshape(4, 5)
    print(f'{len(array_one_1)}\n{array_one_1}\n{array_one_1.shape}')
    return (array_one_1,)


@app.cell
def _(array_one_1, np):
    array_one_col_flat = np.ravel(array_one_1, 'F')  # This will flatten the matrix column wise
    print(array_one_col_flat)
    array_one_row_flat = np.ravel(array_one_1, 'C')
    print(array_one_row_flat)  # This will flatten the matrix row wise
    return


@app.cell
def _(array_one_1):
    array_one_2 = array_one_1.flatten()
    print(array_one_2, array_one_2.ndim)
    return


@app.cell
def _(np):
    # concatenation
    array_two = np.random.randint(1, 15, size=(6, 7))
    array_three = np.random.randint(20, 35, size=(6, 7))
    # print(f'{array_two}\n{array_three}')

    array_two_plus_three = np.concatenate((array_two, array_three), axis=0) # row wise concatenation
    print(array_two_plus_three)

    array_two_plus_three = np.concatenate((array_two, array_three), axis=1) # column wise concatenation
    print(array_two_plus_three)
    return


@app.cell
def _(np):
    # transpose array
    array_three_1 = np.linspace(10, 100, 10, dtype=np.int64)
    array_three_1 = array_three_1.reshape(2, 5)
    print(array_three_1)
    array_three_1 = np.transpose(array_three_1)
    # print(array_three.ndim)
    print(array_three_1)
    return (array_three_1,)


@app.cell
def _(array_three_1, np):
    # split array
    # array_four = np.split(array_three, 3) # ValueError: array split does not result in an equal division
    # print(array_four)
    array_four = np.array_split(array_three_1, 3)
    print(array_four)
    return


if __name__ == "__main__":
    app.run()
