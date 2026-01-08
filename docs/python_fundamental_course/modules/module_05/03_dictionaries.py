import marimo

__generated_with = "0.17.8"
app = marimo.App()


@app.cell
def _():
    information = {"Name": "VSCode", "System": "Linux"}
    print(information)
    return


@app.cell
def _():
    information_1 = {}
    information_1['Name'] = 'Cursor'
    information_1['System'] = 'Linux'
    print(information_1)
    return


@app.cell
def _():
    information_2 = dict(Name='Helix', System='Linux')
    print(information_2)
    return


@app.cell
def _():
    information_3 = dict([('Name', 'CodeBlock'), ('System', 'Linux')])
    print(information_3)
    return (information_3,)


@app.cell
def _(information_3):
    # Access value from a dictionary
    print(information_3['Name'], information_3.get('Name'))
    return


@app.cell
def _():
    # Adding, replacing and deleting values
    information_4 = dict(Name='Helix', System='Linux')
    information_4['Name'] = 'Jet Brain'
    print(information_4)
    return


@app.cell
def _():
    # Formatting dictionaries
    information_5 = dict(Name='Zed', System='Linux')
    text = 'This is %(Name)s for %(System)s system.' % information_5
    print(text)
    return


@app.cell
def _():
    # Deleting item using del operator
    information_6 = dict(Name='Zed', System='Linux', Version=1.0, License='MIT')
    del information_6['System']
    # we use del when we are sure that the key is present in the dictionary
    print(information_6)
    return (information_6,)


@app.cell
def _(information_6):
    information_6.pop('Version')
    # we use pop when we are not sure that the key is present in the dictionary, auto error handing
    print(information_6)
    return


@app.cell
def _():
    # Comparing dictionaries

    information_one = dict(Name="Zed", System="Linux")
    information_two = dict(Name="Zed", System="Linux")
    return information_one, information_two


@app.cell
def _(information_one, information_two):
    print(information_one == information_two)
    return


@app.cell
def _(information_one, information_two):
    print(information_one != information_two)
    return


@app.cell
def _():
    # Dictionary methods
    information_7 = dict(Name='Chem', System='Linux', Version=2.0, License='Apache')
    return (information_7,)


@app.cell
def _(information_7):
    print(information_7.keys())
    return


@app.cell
def _(information_7):
    print(information_7.values())
    return


@app.cell
def _(information_7):
    print(information_7.items())
    return


@app.cell
def _():
    information_8 = dict(Name='marimo', System='Linux', Version=1.0, License='GPL')
    item = information_8.items()

    print(item, type(item))

    for _i in item:
        print(_i, "|", type(_i))
    return (information_8,)


@app.cell
def _(information_8):
    information_8.clear()
    return


@app.cell
def _(information_8):
    print(information_8)
    return


@app.cell
def _():
    # ICPC Min and Max Problem

    # print(user_input, type(user_input), numbers, type(numbers))
    user_input = input()
    numbers = user_input.split()

    num_1 = int(numbers[0])
    num_2 = int(numbers[1])
    num_3 = int(numbers[2])

    max_num = num_1

    if num_2 > max_num:
        max_num = num_2
    if num_3 > max_num:
        max_num = num_3

    min_num = num_1

    if num_2 < min_num:
        min_num = num_2
    if num_3 < min_num:
        min_num = num_3

    print(min_num, max_num)
    return


@app.cell
def _():
    _num = int(input())
    n_list = list(map(int, input().split()))

    even = 0
    odd = 0
    pos = 0
    neg = 0

    for _num in n_list:
        if _num % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
        if _num > 0:
            pos = pos + 1
        elif _num < 0:
            neg = neg + 1
        
    print(f'Even: {even}\nOdd: {odd}\nPositive: {pos}\nNegative: {neg}')
    return


@app.cell
def _():
    sum = 0

    for _i in range(1, 11):
        print(_i, 'is processing')
        if _i % 2 == 0:
            continue
        print(_i, 'is added to the sum')
        sum = sum + _i
    
    print('Total sum is:', sum)
    return


@app.cell
def _():
    acc = 95
    _count = 0

    for _i in range(20):
        acc = acc + 1
        _count = _count + 1
        print('Current accuracy:', acc)
        if acc == 100:
            print('Accuracy reached 100%')
            break
    
    print('Total iterations:', _count)
    return


@app.cell
def _():
    _number = int(input())

    while _number > 0:
        print(_number % 10, end=' ')
        _number = _number // 10
    return


@app.cell
def _():
    t = int(input())

    for _i in range(t):
        _number = int(input())
        if _number == 0:
            print(0)
            continue
        while _number > 0:
            print(_number % 10, end=' ')
            _number = _number // 10
        print()
    return


@app.cell
def _():
    x = 5
    if x > 3:
        print("A")
    elif x > 1:
        print("B")
    else:
        print("C")
    return


@app.cell
def _():
    _i = 0
    while _i < 3:
        _i = _i + 1
        if _i == 2:
            break
    print('Done')
    return


@app.cell
def _():
    for _i in range(2):
        for k in range(3):
            if k == 1:
                break
            print(_i, k)
    return


@app.cell
def _():
    for _i in range(3):
        if _i == 1:
            break
    print(_i)
    return


@app.cell
def _():
    _count = 0
    for _n in [1, 2, 3, 4, 5]:
        if _n % 2 != 0:
            break
        _count = _count + 1
    print(_count)
    return


@app.cell
def _():
    for _i in range(5, 0, -1):
        if _i % 2 == 0:
            continue
        if _i == 3:
            break
        print(_i)
    return


@app.cell
def _():
    _prompt = 'What is your name?'
    print(_prompt, type(_prompt))
    return


@app.cell
def _():
    message = """Tell me about yourself.
    What are the issues you've been facing while learning to code?
    How are you tackling them?
    """
    # For multiline string we should use triple cotation
    print(message, type(message), len(message))
    return (message,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Indexing and Slicing
    """)
    return


@app.cell
def _():
    string = 'hello world'
    for _i in range(11):
        print(string[_i], end=' ')
    return (string,)


@app.cell
def _(message):
    # slicing string[start:end:step]
    first_message = message[0:24]
    print(first_message)
    return


@app.cell
def _(message):
    back_index_message = message[-114:-1]
    print(back_index_message)
    return


@app.cell
def _(message):
    print("you" in message)
    print("You" in message)
    print(type("You" in message))
    return


@app.cell
def _(string):
    processed_string = string.lower()
    print(processed_string)

    processed_string = string.upper()
    print(processed_string)

    processed_string = string.capitalize()  # First letter convert into capital letter
    print(processed_string)
    return


@app.cell
def _(string):
    #  shurur dik theke kon index theke substring ta shuru hoise
    index = string.find("world")
    print(index)
    print(string[6:])
    return


@app.cell
def _():
    #  shesher dik theke kon index theke substring ta shuru hoise
    last_string = "hello world world ML ML, to ML, you ML"
    print(last_string.find("world"))
    print(last_string[6:])
    print(last_string.rfind("world"))
    print(last_string[12:])
    print(last_string.count("world"))
    return (last_string,)


@app.cell
def _(last_string):
    # replace a substring
    # main string doesn't change
    new_string = last_string.replace("ML", "AI/ML")
    print(last_string)  # last string is immutable
    print(new_string)
    return


@app.cell
def _():
    # Splitting, Joining and Formatting Strings
    _prompt = 'This is a string'
    tokens = _prompt.split()  # by default split by space and it returns a list
    print(tokens, type(tokens))
    return


@app.cell
def _():
    dashed_prompt = "This-is-a-string"
    dashed_tokens = dashed_prompt.split("-")
    print(dashed_tokens)
    return


@app.cell
def _():
    mixed_prompt = "This is-a string, split by both space and -"
    mixed_tokens = mixed_prompt.split("-")  # this will split only by '-'
    print(mixed_tokens)

    # to solve this we can first replace '-' with ' ' and then split by space
    mixed_tokens = mixed_prompt.replace("-", " ").split()
    print(mixed_tokens)
    return (mixed_tokens,)


@app.cell
def _(mixed_tokens):
    sentence = "^<->^".join(mixed_tokens)
    print(sentence, type(sentence))
    return


if __name__ == "__main__":
    app.run()
