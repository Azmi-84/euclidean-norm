import marimo

__generated_with = "0.17.8"
app = marimo.App()


@app.cell
def _():
    numbers = [4, 2, 9, 1, 5, 6]
    print(numbers, type(numbers))
    return (numbers,)


@app.cell
def _(numbers):
    # indexing
    print(numbers[0])
    print(numbers[1])
    print(numbers[2])
    print(numbers[3])
    print(numbers[4])
    print(numbers[5])
    return


@app.cell
def _(numbers):
    # negative indexing
    print(numbers[-1])
    print(numbers[-2])
    print(numbers[-3])
    print(numbers[-4])
    print(numbers[-5])
    print(numbers[-6])
    return


@app.cell
def _(numbers):
    for _i in range(len(numbers)):
        print(numbers[_i], end=' ')
    return


@app.cell
def _(numbers):
    # list is mutable
    print(numbers)
    numbers[0] = 10
    print(numbers)
    return


@app.cell
def _(numbers):
    # slicing
    print(numbers[1:4])  # it'll print from index 1 to index 3
    print(numbers[2:])  # it'll print from index 2 to the end
    print(numbers[:4])  # it'll print from the start to index 3
    return


@app.cell
def _(numbers):
    # adding elements to a list
    numbers.append(20)
    print(numbers)

    numbers.insert(2, 15)  # insert 15 at index 2, this will shift the rest of the elements to the right
    print(numbers)
    return


@app.cell
def _(numbers):
    # deleting elements from a list
    numbers.pop()  # it'll remove the last element
    print(numbers)

    numbers.pop(2)  # it'll remove the element at index 2
    print(numbers)

    numbers.remove(5)  # it'll remove the first occurrence of 5
    print(numbers)
    return


@app.cell
def _():
    _float_numbers = [4.5, 2.3, 9.1, 1.0, 5.6, 6.2]

    for _num in _float_numbers:
        print(_num, type(_num), "|", end=" ")
    return


@app.cell
def _():
    _string_list = ['apple', 'banana', 'cherry', 'date']

    for _fruit in _string_list:
        print(_fruit, type(_fruit), '|', end=' ')
    return


@app.cell
def _():
    mixed_list = [1, 2.5, "hello", True, 3 + 4j]

    for item in mixed_list:
        print(item, type(item), "|", end=" ")
    return


@app.cell
def _():
    _nested_list = [[1, 2], [3.5, 4.5], ["a", "b", "c"], [True, False], [5 + 6j, 7 + 8j]]

    for _sublist in _nested_list:
        for _element in _sublist:
            print(_element, type(_element), "|", end=" ")
        print(_sublist, type(_sublist), "|", end="\n")
    return


@app.cell
def _(numbers):
    _float_numbers = [4.5, 2.3, 9.1, 1.0, 5.6, 6.2]
    _string_list = ['apple', 'banana', 'cherry', 'date']

    numbers.sort()  # it'll sort in ascending order (smallest to largest)

    # numbers.sort(reverse=True)  # it'll sort in descending order (largest to smallest)
    # numbers.reverse()  # it'll reverse the list

    _float_numbers.sort()
    _string_list.sort()  # it'll sort in alphabetical order

    # mixed_list.sort() # TypeError: '<' not supported between instances of 'str' and 'float'"
    # nested_list.sort()  # it'll also give TypeError because the elements are not comparable

    print(f"Sorted numbers: {numbers} | Sorted float_numbers: {_float_numbers} | Sorted string_list: {_string_list}")
    return


@app.cell
def _():
    # Stack as list
    # Think of it as placing one plate above another, now if we want to remove or take a plate we will first take the last one cause it's easy to remove it. It's mean last in first out.

    stack = []

    # print(len(stack))
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    stack.append(5)

    print(stack)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    # print(stack.pop())
    return


@app.cell
def _():
    # List as Queue
    # In queue the first element that comes in is the first one to go out. Think of it as a line of people waiting to buy a ticket, the first person in line is the first one to get the ticket and leave the line.

    queue = []

    # insertion
    queue.append(1)
    queue.append(2)
    queue.append(3)
    queue.append(4)
    queue.append(5)

    # remove
    print(f"removed element: {queue.pop(0)}")

    # accessing the front element
    print(f"front element: {queue[0]}")

    # length of the queue
    print(f"length of queue: {len(queue)}")

    # top element
    print(f"top element: {queue[-1]}")

    print(f"removed element: {queue.pop(0)}")
    print(f"removed element: {queue.pop(0)}")
    print(f"removed element: {queue.pop(0)}")
    print(f"removed element: {queue.pop(0)}")
    return


@app.cell
def _():
    # List Comprehension
    # even = [_i for _i in range(1, 21) if _i % 2 == 0]

    even = []

    for _i in range(1, 21):
        if _i % 2 == 0:
            even.append(_i)

    print(even)
    return


@app.cell
def _():
    # general syntax
    # [expression for item in iterable if condition]

    random_list = []
    random_list = [x**2 for x in range(10) if x % 2 == 0]
    print(random_list)
    return


@app.cell
def _():
    fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
    capitalize_fruits = []

    for _fruit in fruits:
        capitalize_fruits.append(_fruit.capitalize())

    print(capitalize_fruits)

    upper_fruits = [_fruit.upper() for _fruit in fruits]
    print(upper_fruits)
    return


@app.cell
def _():
    code = "banana bandana"
    print(code.count("ana"))
    return


@app.cell
def _():
    nums = [1, 2, 3, 4, 5]
    nums[2] = nums[2] * nums[0]
    print(nums)
    return


@app.cell
def _():
    x = 1
    y = 2
    z = 1
    n = 2

    for a in range(x+1):
        for b in range(y+1):
            for c in range(z+1):
                print(a, b, c, end=" | ")

    lst = [[a, b, c] for a in range(0, x+1) for b in range(0, y+1) for c in range(0, z+1)]
    print(f"\n{lst}")

    lst = [[a, b, c] for a in range(0, x+1) for b in range(0, y+1) for c in range(0, z+1) if a+b+c != n]
    print(lst)
    return


if __name__ == "__main__":
    app.run()
