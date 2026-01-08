import marimo

__generated_with = "0.17.8"
app = marimo.App()


@app.cell
def _():
    # Loop Control Statements in Python
    _num = 0
    _sum_of_num = 0

    while _num <= 10:
        _sum_of_num += _num
        print(_num, end="|")
        _num += 1
    
    print(_num)
    return


@app.cell
def _():
    # _num = eval(input('Enter a number: '))
    _num = 543
    _sum_of_digits = 0
    _temp_num = _num

    while _temp_num > 0:
        _rem = _temp_num % 10
        print(f"reminder: {_rem}", end="|")
    
        _sum_of_digits = _sum_of_digits + _rem
        print(f"sum of digits: {_sum_of_digits}", end="|")
    
        _temp_num = _temp_num // 10
        print(f"temp: {_temp_num}", end="|")

    print(f"answer: {_sum_of_digits}")
    return


@app.cell
def _():
    # _temp_num = eval(input('Enter a number: '))
    _temp_num = 45
    sum_of_reversed = 0

    while _temp_num > 0:
        _rem = _temp_num % 10
        sum_of_reversed = sum_of_reversed * 10 + _rem
        _temp_num = _temp_num // 10

    print(sum_of_reversed)
    return


@app.cell
def _():
    div_num = int(input('Enter a number: '))
    _sum_of_num = 0

    while div_num > 0:
        if div_num % 5 == 0:
            _sum_of_num += div_num
        div_num -= 1
    
    print(_sum_of_num)
    return


@app.cell
def _():
    # Factorial of a number

    fact_num = int(input("Enter a number: "))
    temp = fact_num
    fact = 1

    if fact_num == 0:
        print(f"Factorial of 0 is 1")
    elif fact_num < 0:
        print("Factorial is not defined for negative number")
    else:
        while fact_num >= 1:
            fact *= fact_num
            fact_num -= 1
        
        print(f"Factorial of {temp} is {fact}")
    return


@app.cell
def _():
    from math import factorial

    factorial(70)
    return


@app.cell
def _():
    perfect_num = int(input('Enter a number: '))
    perfect_sum = 0

    for _i in range(1, perfect_num):
        if perfect_num % _i == 0:
            perfect_sum += _i
        
    if perfect_num == perfect_sum:
        print(f'{perfect_num} is a perfect number')
    else:
        print(f'{perfect_num} is not a perfect number')
    return


@app.cell
def _():
    arm_num = int(input('Enter a number: '))
    original_num = arm_num
    original_num_2 = arm_num
    arm_sum = 0
    point = 0

    while arm_num > 0:
        _rem = arm_num % 10
        point += 1
        arm_num = arm_num // 10
    
    while original_num > 0:
        _rem = original_num % 10
        arm_sum += _rem ** point
        original_num = original_num // 10
    
    if arm_sum == original_num_2:
        print(f'{original_num_2} is a armstrong number')
    else:
    # print(point)
        print(f'{original_num_2} is not a armstrong number')
    return


@app.cell
def _():
    print('Number from 1 to 10 reverse order:')

    for _i in range(10, 0, -1):
        print(_i, end=' ')
    return


@app.cell
def _():
    ev_num = int(input('Enter a number:'))
    ev_sum = 0

    for _i in range(1, ev_num + 1):
        if _i % 2 == 0:
            ev_sum += _i
        
    print(f'Even sum is {ev_sum}')
    return


@app.cell
def _():
    nums = int(input('Enter a number'))
    sums = 0

    for _i in range(1, nums + 1):
        if _i % 2 != 0 and _i % 3 != 0 and (_i % 5 != 0):
            sums += _i
        
    print(sums)
    return


@app.cell
def _():
    namta = int(input('Enter a number'))

    for _i in range(1, namta + 1):
        print(f'Multiplication table of {_i}')
        for _k in range(1, 11):
            print(_i, '*', _k, '=', _i * _k)
    return


@app.cell
def _():
    # Pattern Display
    _user_want = int(input('Enter the no'))

    for _i in range(1, _user_want + 1):
        for _k in range(1, _i + 1):
            print(f'{_k}', end='')
        
        print()
    return


@app.cell
def _():
    # Pattern Display
    _user_want = int(input('Enter the no'))
    count = 1

    for _i in range(1, _user_want + 1):
        for _k in range(1, _i + 1):
            print(f'{count}', end='')
            count += 1
        
        print()
    return


@app.cell
def _():
    # Pattern Display
    _user_want = int(input('Enter the no'))

    for _i in range(_user_want, 0, -1):
        for _k in range(1, _i + 1):
            print(f'{_k}', end='')
        
        print()
    return


@app.cell
def _():
    _user_want = int(input('Enter a number'))
    letter = 65

    for _i in range(1, _user_want + 1):
        for _k in range(1, _i + 1):
            print(f'{chr(letter)}', end='')
            letter += 1
        
        print()
    return


@app.cell
def _():
    # Hollow Square Pattern
    _user_input = int(input('Enter a number'))

    for _i in range(1, _user_input + 1):
        for _k in range(1, _user_input + 1):
            if _i == 1 or _i == _user_input or _k == 1 or (_k == _user_input):
                print('+', end=' ')
            else:
                print(' ', end=' ')
            
        print()
    return


@app.cell
def _():
    # Inverted and Rotated Half-Pyramid
    _user_input = int(input('Enter a number'))

    for _i in range(1, _user_input + 1):
        n = _user_input - _i
        for _k in range(1, n + 1):
            print(' ', end=' ')
        for _k in range(1, _i + 1):
            print('+', end=' ')
        
        print()
    return


@app.cell
def _():
    _user_input = int(input('Enter a number'))

    for _i in range(1, _user_input + 1):
        num_spaces = _user_input - _i
        for _k in range(1, num_spaces + 1):  # no of spaces decrease as the row no increases
            print(' ', end=' ')
        num_symbols = 2 * _i - 1
        for _k in range(1, num_symbols + 1):
            print('+', end=' ')
        
        print()
    return


if __name__ == "__main__":
    app.run()
