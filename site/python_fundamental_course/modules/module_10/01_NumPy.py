import marimo

__generated_with = "0.17.2"
app = marimo.App()


@app.cell
def _():
    # List is not homogenous and it can contain mixed data type which is critical issue when handling large datasets and implementing operations
    # To solve these problems NumPys ndarray is very useful
    # Suppose we wanted to multiply with an integer value in a list
    # SIMD = Single Instruction Multiple Data
    lst = [1, 2, 3]
    print(lst*5)
    lst = [x*5 for x in lst]
    print(lst)
    # lst = [i for i in range(10000000)] # computer stopped due to large range in list data type
    # print(lst)
    # lst = [i*5 for i in lst]
    # print(lst)
    return


@app.cell
def _():
    import numpy as np

    # array_zero = np.array([i for i in range(10000000)])
    # print(array_zero*5)

    array_one = np.array([i for i in range(5)])
    print(array_one*5, type(array_one), array_one.ndim)

    array_two = np.array([[i for i in range(5)], [i for i in range(5)]])
    print(array_two.ndim)

    array_three = np.array([[[i for i in range(5)], [i for i in range(5)]], [[i for i in range(5)], [i for i in range(5)]]])
    print(array_three.ndim)
    return array_one, array_three, array_two, np


@app.cell
def _(array_one, array_three, array_two):
    # numpy array methods

    # dimension: already mentioned in the previous column

    # shape
    print(array_one.shape, array_two.shape, array_three.shape)

    # data type
    print(array_one.dtype, array_two.dtype, array_three.dtype)

    # size
    print(array_one.size, array_two.size, array_three.size)
    return


@app.cell
def _(np):
    # upcasting: array_six to float and array_seven to string [U is string data type in numpy]

    array_four = np.array([i for i in range(5)])
    array_five = np.array([float(i) for i in range(5)])
    array_six = np.array([i if i%2 == 0 else float(i) for i in range(5)])
    array_seven = np.array([i if i%2 == 0 else (chr(64+i) if i==1 else float(i)) for i in range(5)])

    print(array_four, array_five, array_six, array_seven)
    print(array_four.dtype, array_five.dtype, array_six.dtype, array_seven.dtype)
    return


@app.cell
def _(np):
    # selecting a data type for an array

    array_eight = np.array([i for i in range(5)], dtype=np.int16)
    print(array_eight.dtype)
    array_eight = array_eight.astype(np.int8)
    print(array_eight.dtype)

    # problem of int8 is we can't use big number for this data type cause value greater than 2^n shows OverflowError
    # array_eight = np.array([i for i in range(129)], dtype=np.int8)
    # print(array_eight, array_eight.dtype)
    return


@app.cell
def _(np):
    # tuple
    array_nine = np.array(tuple(i for i in range(5)))
    print(array_nine, array_nine.dtype)

    # set
    array_ten = np.array(set(i for i in range(5)))
    print(array_ten, array_ten.dtype)

    array_ten = np.array(list(set(i for i in range(5))))
    print(array_ten, array_ten.dtype)

    # dictionary
    array_eleven_dict = {chr(key+64): val for key, val in zip(range(1, 6), range(5))}
    array_eleven = np.array(array_eleven_dict)
    array_eleven_keys = array_eleven_dict.keys()
    array_eleven_values = array_eleven_dict.values()
    array_eleven_items = array_eleven_dict.items()

    print(array_eleven, array_eleven.dtype, type(array_eleven_keys), type(array_eleven_values), type(array_eleven_items))

    array_eleven_keys = np.array(list(array_eleven_dict.keys()))
    array_eleven_values = np.array(list(array_eleven_dict.values()))
    array_eleven_items = np.array(list(array_eleven_items))

    print(array_eleven_keys, array_eleven_values, array_eleven_items)
    print(array_eleven_keys.dtype, array_eleven_values.dtype, array_eleven_items.dtype)
    return


@app.cell
def _(array_three, np):
    # creating ndarray form scratch

    array_twelve = np.zeros((2, 3))
    print(array_twelve, array_twelve.dtype)

    array_thirteen = np.zeros_like(array_three)
    print(array_thirteen, array_thirteen.dtype, array_thirteen.shape, array_three.shape)

    array_fourteen = np.ones((2, 3))
    array_fifteen = np.ones_like((array_thirteen))
    print(array_fourteen.shape, array_fifteen.shape)
    return


@app.cell
def _(np):
    array_sixteen = np.empty((3, 4))
    print(array_sixteen)

    array_seventeen = np.full((3, 4), 10)
    print(array_seventeen)

    array_seventeen = np.full((3, 4), True)
    print(array_seventeen)

    array_seventeen = np.full((3, 4), np.inf)
    print(array_seventeen)
    return


@app.cell
def _(np):
    array_eighteen = np.random.rand(3, 4)
    print(array_eighteen, array_eighteen.dtype)

    array_eighteen = np.random.randint(3, 5)
    print(array_eighteen)

    array_eighteen = np.random.randint(3, 5, 10)
    print(array_eighteen)

    array_eighteen = np.random.randint(3, 5, (10, 5))
    print(array_eighteen)
    return


@app.cell
def _(np):
    array_nineteen = np.random.uniform(3, 10, (3, 4))
    print(array_nineteen, array_nineteen.dtype)
    return


@app.cell
def _(np):
    # array creation with range function
    array_twenty = np.arange(2, 20, 2)
    print(array_twenty, array_twenty.dtype, array_twenty.size)

    array_twenty = array_twenty.reshape(3, 3)
    print(array_twenty, array_twenty.dtype, array_twenty.size)
    return


@app.cell
def _(np):
    # array creation with linspace (linear space)
    array_twenty_one = np.linspace(2, 20, 5, retstep=False)
    print(array_twenty_one, array_twenty_one.dtype, array_twenty_one.shape)
    return


@app.cell
def _(np):
    # array creation with logspace
    array_twenty_two = np.logspace(0, 4, 5)
    print(array_twenty_two)
    return


@app.cell
def _(np):
    # creating matrix for linear algebra
    array_twenty_three = np.diag([1, 2, 3, 4, 5])
    print(array_twenty_three)

    array_twenty_four = np.eye(4, dtype=np.int64)
    print(array_twenty_four)

    array_twenty_four = np.eye(3, 4, dtype=np.int64)
    print(array_twenty_four)

    array_twenty_four = np.eye(3, 4, -1, dtype=np.int64)
    print(array_twenty_four)
    return


@app.cell
def _(array_one, array_two):
    # indexing and slicing
    print(array_one.shape, array_two.shape)
    array_one[2] = 10
    print(array_one)
    array_two[0][2] = 84
    print(array_two)
    array_one_1 = array_one[1:4]
    print(array_one_1)
    array_two_1 = array_two[0:1:1, 0::1]
    print(array_two_1)
    return


if __name__ == "__main__":
    app.run()
