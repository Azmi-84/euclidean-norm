import marimo

__generated_with = "0.17.5"
app = marimo.App()


@app.cell
def _():
    def _code(lang):
        print(f'Welcome to the World of {lang}')
    _code('Python')
    return


@app.cell
def _():
    # Default argument pass
    def _code(lang='C++'):
        print(f'Welcome to the World of {lang}')
    _code()
    _code('Perl')
    return


@app.cell
def _():
    def sqr_summation(a, b, c):
        summation = a**2 + b**2 + c**2
        print(f"Summation of {a}, {b} and {c} is {summation}")


    # ans = sqr_summation(10, 20, 30) + 10

    # This error actually showing as we haven't returned anything and if we explicitly don't return the default return is None and we can't perform any operation on this Nonetype
    return


@app.cell
def _():
    def _sqr_summations(a, b, c):
        print(f'a={a}|b={b}|c={c}')
        summations = a ** 2 + b ** 2 + c ** 2
        return summations
    _ans = _sqr_summations(10, 20, 30) + 10
    # when passing the arguments the position is very important
    print(_ans)
    return


@app.cell
def _():
    def _sqr_summations(a, b, c):
        print(f'a={a}|b={b}|c={c}')
        summations = a ** 2 + b ** 2 + c ** 2
        return summations
    _ans = _sqr_summations(b=10, c=20, a=30) + 10
    # but if we mention these arguments along with the mentioning the variables name then we don't have to take care of position, it's hectic u know :]
    print(_ans)
    return


@app.cell
def _():
    def sqr_sum(*args):
        """If we wanted to pass multiple arguments we can use `*args` which allow us to execute this operation

        Returns:
            tuple: we can iterate on it and perform necessary operations
        """

        print(f"Value of args [multiple argument]: {args} and type of it {type(args)}")

        sum = 0
        for i in range(len(args)):
            sum += args[i] ** 2
        return sum

    print(sqr_sum(10, 20, 30, 40, 50, 60))
    return


@app.cell
def _():
    def student_info(**kwargs):
        """If we wanted to pass multiple keyword arguments we have to use the `**kwargs`

        Returns:
            dictionary: we can use iteration to perform any sorts of operation
        """
        print(f"Value of keyword args [multiple keyword argument]: {kwargs} and type of it {type(kwargs)}")
        print(kwargs.keys())

        total_marks = 0
        for val in kwargs["marks"]:
            total_marks += val
        return total_marks


    print(student_info(name="marimo", year=10, marks=[280, 270, 295]))
    return


if __name__ == "__main__":
    app.run()
