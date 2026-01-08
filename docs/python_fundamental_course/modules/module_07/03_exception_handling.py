import marimo

__generated_with = "0.17.2"
app = marimo.App()


@app.cell
def _():
    """Blog Link: https://www.geeksforgeeks.org/python/python-exception-handling/"""
    return


@app.cell
def _():
    _n = 10
    _res = _n / 0
    return


@app.cell
def _():
    _n = 10
    try:
        _res = _n / 0
    except ZeroDivisionError:
        print(f"{_n} can't divided by zero")
    return


@app.cell
def _():
    # Difference between Error and Exception:
    # We can't handle error cause these are serious problems in the program
    # Exception are the less severe problem that occur at runtime and can be managed using exception handling
    return


@app.cell
def _():
    try:
        _n = int(input())
        _res = 100 / _n
    except ZeroDivisionError:
        print(f"100 can't be divided by {_n}")
    except ValueError:
        print('Invalid input. Please provide an integer value')
    else:
        print(f'Result is {_res}')
    finally:
        print('Execution is complete')
    return


@app.cell
def _():
    lst = ['23', 'abcd', 23, 23.8, 'a ', 'a b']

    try:
    
        """converting string numbers to actual numbers then sum
        This filters out non-numeric strings like 'abcd'
        We cannot use [try-except] blocks inside list comprehensions
        """
        numeric_values = []
    
        for item in lst:
            if isinstance(item, (int, float)):
                numeric_values.append(item)
            elif isinstance(item, str):
                if len(item) == 1:
                    numeric_values.append(float(ord(item)))
                elif ' ' in item:
                    item = item.strip()
                    if len(item) == 1:
                        numeric_values.append(float(ord(item)))
                    else:
                        print(f"{item} length is greater than one.")
                else:
                    try:
                        numeric_values.append(float(item))
                    except Exception as e:
                        print(f"Error: {e}")
                        continue
            # elif(item, list):
            
        summation = sum(numeric_values)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
    else:
        print(f"Numeric Values: {numeric_values} and Sum of the values: {summation}")
    finally:
        print("Done")
    return


if __name__ == "__main__":
    app.run()
