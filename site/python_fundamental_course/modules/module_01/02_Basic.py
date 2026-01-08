import marimo

__generated_with = "0.17.8"
app = marimo.App()


@app.cell
def _():
    from math import pi

    radius = eval(input("Enter the radius of the circle: "))
    if radius > 0:
        area = pi * (radius**2)
        print(f"Radius of the circle: {radius} | Area: {area} | Data Type: {isinstance(radius, int)}")
    elif radius == 0:
        print("A circle with radius 0 has no area.")
    else:
        print("Error: Radius cannot be negative!")
    return


@app.cell
def _():
    # Simple Calculator

    first_number = eval(input("Enter the first number: "))
    second_number = eval(input("Enter the second number: "))

    print(f"Which operation you want? | (1) Addition | (2) Subtraction | (3) Multiplication | (4) Division")
    choice = eval(input("Give your choice: "))

    if choice == 1:
        add = first_number + second_number
        print(f"First number is: {first_number} | Second number is: {second_number} | Addition: {first_number + second_number}")
    elif choice == 2:
        sub = first_number - second_number
        print(f"First number is: {first_number} | Second number is: {second_number} | Subtraction: {first_number - second_number}")
    elif choice == 3:
        mul = first_number * second_number
        print(f"First number is: {first_number} | Second number is: {second_number} | Multiplication: {first_number * second_number}")
    elif choice == 4:
        if second_number > 0:
            div = first_number / second_number
            print(f"First number is: {first_number} | Second number is: {second_number} | Division: {first_number / second_number}")
        else:
            print("Denominator can't be zero")
    else:
        print("Wrong input!!!")
    return


@app.cell
def _():
    # Simple Prime Number Checker
    # from math import sqrt

    val = eval(input("Enter a number: "))
    flag = 0

    if val <= 1:
        print("Enter number more than 1")

    # for i in range(2, int(sqrt(val)) + 1):
    for i in range(2, int(val**0.5) + 1):
        if val % i == 0:
            flag = 1

    if flag == 0:
        print(f"{val} is a prime number")
    else:
        print(f"{val} is not a prime number")
    return


if __name__ == "__main__":
    app.run()
