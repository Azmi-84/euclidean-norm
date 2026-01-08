import marimo

__generated_with = "0.17.8"
app = marimo.App()


@app.cell
def _():
    print("Hello World!")
    print("I'm learning Python")
    print("Python is a versatile language")
    return


@app.cell
def _():
    print("Hello World!", end=" ")
    print("I'm learning Python.", end=" ")
    print("Python is a versatile language.", end=" ")
    return


@app.cell
def _():
    _a = 30
    _b = 20
    _a, _b = (_b, _a)
    print(_a, _b)
    return


@app.cell
def _():
    # length = int(input("Enter the length: "))
    # breadth = int(input("Enter the breadth: "))
    length = 23.3
    breadth = 23.3
    area = length * breadth
    print("The area of the rectangle is:", area)
    return


@app.cell
def _():
    # When using input function, the input is taken as a string by default. To convert it to an integer, we use the int() function. If we want to take float input, we can use the float() function and others accordingly.
    # To get an expected input, we can use eval() function. For example, if we want to take a list as input, we can use eval(input()).


    number = eval(input("Enter a number: "))
    strings = input("Enter a string: ")

    print(number, type(number))
    print(strings, type(strings))
    return


@app.cell
def _():
    _d = 34.44456968
    _d = format(_d, '.3f')  # This will round the number to 3 decimal places
    print(_d, type(_d))
    return


@app.cell
def _():
    _d = 34.44456968
    _d = format(_d, '7.3f')  # This will round the number to 3 decimal places and make the total length 7 by adding spaces in the front if necessary
    print(_d, len(_d), type(_d))
    print(" " in _d)
    print(f"{_d.find(" ")}")
    return


@app.cell
def _():
    x = 20.345123
    x = format(x, "<7.3f")  # This will round the number to 3 decimal places and make the total length 7 by adding spaces in the back if necessary
    print(x, len(x))
    return


@app.cell
def _():
    from math import pi
    print(pi, format(pi, ".3%"), type(pi))
    return


@app.cell
def _():
    # Specifier Format
    # 10.2f ---> floating point number with precision 2 and width 10.
    # <10.2f ---> Left Justify the floating point number.
    # >10.2f ---> Right Justify the formatted item.
    # 10X ---> Format integer in hexadecimal with width 10
    # 20s ---> Format String with width 20
    # 10.2% ---> Format the number in decimal
    return


@app.cell
def _():
    _val = 344
    print(format(_val, '10X'))
    return


@app.cell
def _():
    characters = "characters"
    print(format(characters, ".5s"), format(characters, "5s"))
    print(len(characters))
    return


@app.cell
def _():
    # Python Inbuilt Function
    return


@app.cell
def _():
    # ceil(x) ----> Round X to nearest integer and returns that integer.
    # floor(x) ----> Returns the largest value not greater than X
    # exp(x) ----> Returns the exponential value for e^x
    # log(x) ----> Returns the natural logarithmic of x (to base e)
    # log(x, base) ----> Returns the logarithm of x to the given base
    # sqrt(x) ----> Return the square root of x
    # Sin(x) ----> Return the sin of X, where X is the value in radians
    # asin(x) ----> Return the angle in radians for the inverse of sine
    # cos(x) ----> Return the sin of X, where X is the value in radians
    # aCos(x) ----> Return the angle in radians for the inverse of cosine
    # tan(x) ----> Return the tangent of X, where X is the value in radians
    # degrees(x) ----> Convert angle X from to radians to degrees
    # Radians(x) ----> Convert angle X from to radians to degrees
    return


@app.cell
def _():
    import math

    print(math.ceil(10.23))
    print(math.floor(10.23))
    print(math.exp(2))
    print(format(math.exp(2), ".3f"))
    print(math.log(2.7))
    print(math.floor(math.log(2.7)))
    print(math.ceil(math.log(2.7)))
    return


@app.cell
def _():
    # ord and chr functions
    # "ord" return the ASCII value of a character
    # "chr" return the character of ASCII value

    print(ord("A"), chr(65))
    return


@app.cell
def _():
    # Summary

    # 1. Python breaks each statement into a sequence of lexical components called tokens.
    # 2.Literals are numbers, strings or characters that appear directly in a program.
    # 3.Python offers an inbuilt method called type to know the exact type of any value.
    # 4.Keywords are reserved words.
    # 5.Keywords cannot be used as identifiers or variables. An identifier is a name used to identify a variable, function, class or other objects.
    # 6.Everything in Python is an object.
    # 7.The int function converts a string or a number into a whole number or integer.
    # 8.The float function converts a string into a floating-point number.
    # 9.The Boolean data type is represented in Python as of type bool.
    # 10.print function is used to display contents on the screen.
    # 11.input() function is used to accept input from the user.
    # 12.format() function can be used to return a formatted string.
    # 13. Python Tokens: keywords, identifiers/Variables, Operators, Delimiters, literals
    # 14. Integer Literal: 18, Floating Point Literal: 21.98, "Q" : Character literal, "Hello": String Literal
    # 15. keywords: and, as, assert, break, class, continue, def, del, elif, else, except, False, finally, for, from, global, if, import, in, is, lambda, None, nonlocal, not, or, pass, raise, return,
    # True, try, while, with, yield
    # 16. Operators: "+ - * / // % ** ---> Arithmetic Operator" "== != <> <= >= ---> Relational Operator" "and not or ---> Logical Operator" "& | ~ ^ << >> ---> Bitwise Operator"
    # 17. Delimiter: Delimiters are symbols that perform a special role in Python like grouping, punctuation and assignment. Python uses the following symbols and symbol combinations as delimiters. ( ) [ ] { } , : . ‘ = ; += -= *= /= //= %= &= |= ^= >>= <<= **=
    # 18. Identifier: • Is a sequence of characters that consists of letters, digits and underscore • Can be of any length • Starts with a letter which can be either lower or upper case • Can start with an underscore ‘_’ • Cannot start with a digit • Cannot be a keyword. Some examples of valid identifiers are Name, Roll_NO, A1, _Address etc.
    return


@app.cell
def _():
    # Tokens and Language Structure

    # Python operates by breaking down your code into **tokens** - the smallest meaningful units of the language. Think of tokens as the "words" in Python's vocabulary. These tokens fall into five main categories: keywords, identifiers/variables, operators, delimiters, and literals. Understanding this tokenization process helps explain how Python interprets and executes your code.

    # Literals and Data Types

    # **Literals** are the actual values you write directly in your code - like the number `18`, the decimal `21.98`, or the string `"Hello"`. Python provides built-in functions to work with different data types: `int()` converts values to whole numbers, `float()` handles decimal numbers, and `bool` represents True/False values. The `type()` function is particularly useful for debugging, as it tells you exactly what kind of data you're working with.

    # Keywords and Identifiers

    # **Keywords** are Python's reserved words that have special meanings - like `if`, `for`, `def`, `class`, and `return`. These cannot be used as variable names because they're part of Python's core syntax. **Identifiers**, on the other hand, are the names you create for variables, functions, and classes. They must start with a letter or underscore, can contain letters, digits, and underscores, but cannot start with a digit or be a keyword.

    # Operators and Delimiters

    # Python includes various **operators** for different operations: arithmetic operators (`+`, `-`, `*`, `/`) for math, relational operators (`==`, `!=`, `<`, `>`) for comparisons, logical operators (`and`, `or`, `not`) for boolean logic, and bitwise operators for low-level operations. **Delimiters** are the punctuation marks that structure your code - parentheses for function calls, brackets for lists, braces for dictionaries, and various assignment operators like `+=` and `-=`.

    # Core Functions

    # Essential built-in functions: `print()` displays output to the screen, `input()` accepts user input as strings, and `format()` creates formatted strings. These functions form the foundation for user interaction in Python programs.

    # Everything is an Object

    # A crucial concept mentioned is that "everything in Python is an object." This means that numbers, strings, functions, and even data types themselves are objects with methods and attributes. This object-oriented nature makes Python flexible and powerful, allowing you to treat different types of data in consistent ways.
    return


@app.cell
def _():
    # Exercises
    _a, _b, _c = (5, 10, 15)
    _a, _b, _c = (_c, _a, _b)
    print(_a, _b, _c)
    return


@app.cell
def _():
    try:
        # age = int(input("Enter your age: "))
        # height = float(input("Enter your height: "))
        # name = input("Enter your name: ")
        age = 10
        height = 5.8
        name = "abcd"

        print(f"Name: {name} | Age: {age} | Height: {height}")

    except ValueError:
        print("Invalid error!")
    return


@app.cell
def _():
    price = 1234.5678
    product = "Laptop"
    quantity = 5

    print(f"Product: {product:<15} | Price: ${price:>8.2f} | Quantity: {quantity:>3}")
    print("Product: {:<15} | Price: ${:>8.2f} | Quantity: {:>3}".format(product, price, quantity))
    print("Total: ${:.2f}".format(price * quantity))
    return


@app.cell
def _():
    num = 255
    print(f"Decimal: {num} | Binary: {format(num, 'b')} | Octal: {format(num, 'o')} | Hexadecimal: {format(num, 'X')}")
    return


@app.cell
def _():
    _ascii_code = ord('A')
    _end_code = _ascii_code + 6
    # ascii
    while _ascii_code < _end_code:
        print(f'Character: {chr(_ascii_code)} | ASCII code: {_ascii_code}')
        _ascii_code += 1
    return


@app.cell
def _():
    _ascii_code = ord('A')
    _end_code = _ascii_code + 6
    for code in range(_ascii_code, _end_code):
        print(f'Character: {chr(code)} | ASCII code: {code}')
    return


@app.cell
def _():
    site_name = chr(65)
    end_site = chr(ord(site_name) + 6)

    for site in range(ord(site_name), ord(end_site)):
        city = chr(site)
        city = input("Enter a city name: ")
        print(f"City name: {city} | Variable name: {chr(site)}")
    return


@app.cell
def _():
    _val = input('Enter a number: ')
    print(f'Value before conversion: {_val} | Type: {type(_val)}')
    _val = int(_val)
    print(f'Value after conversion: {_val} | Type: {type(_val)}')
    return


@app.cell
def _():
    str1 = "hello world"
    print(str1.upper())
    return


if __name__ == "__main__":
    app.run()
