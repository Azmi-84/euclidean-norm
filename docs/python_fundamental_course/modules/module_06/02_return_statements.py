import marimo

__generated_with = "0.17.5"
app = marimo.App()


@app.cell
def _():
    def _smth_pred():
        return 10
    print(type(_smth_pred()))
    return


@app.cell
def _():
    def _smth_pred():
        return 'name'
    print(type(_smth_pred()))
    return


@app.cell
def _():
    def _smth_pred():
        return (10, 20, 30)
    print(f'{type(_smth_pred())}')
    _a, _b, c = _smth_pred()
    # unpacking
    print(_a, _b, c)
    return


@app.cell
def _():
    def _smth_pred():
        """when we return a single list the class is list but when we return multiple list the class is tuple

        Returns:
            list: if the return is single list
            tuple: if the return is multiple list
        """
        _a = [10, 20, 30]  # return [10, 20, 30]
        _b = [10.1, 20.1, 30.1]
        return (_a, _b)
    print(f'type: {type(_smth_pred())} and value: {_smth_pred()}')
    _a, _b = _smth_pred()
    # unpacking
    print(_a, _b)
    return


@app.cell
def _():
    def _smth_pred():
        """same as list

        Returns:
            set: if return a single set
            tuple: if return multiple set
        """
        _a = {10, 20, 30}  # return {10, 20, 30}
        _b = {40, 50, 60}
        return (_a, _b)
    print(f'{type(_smth_pred())}')
    _a, _b = _smth_pred()
    # unpacking
    print(_a, _b)
    return


@app.cell
def _():
    def _smth_pred():
        """same as previous one

        Returns:
            dict: if return a single dict
            tuple: if return multiple dict
        """
        _a = {'name': 'name', 'year': 2025, 'lang': ['Python', 12, (1, 2, 4)]}  # return {"name": "name", "year": 2025, "lang": ["Python", 12, (1, 2, 4)]}
        _b = {'name': 'name', 'year': 2025, 'lang': ['Python', 12, (1, 2, 4)], (2, 4, 6): {'name': 'name', 'year': 2025, 'lang': ['Python', 12, (1, 2, 4)]}}
        return (_a, _b)
    print(f'{type(_smth_pred())}')
    _a, _b = _smth_pred()
    # unpacking
    print(f'{_a}\n{_b}')
    return


@app.cell
def _():
    def _smth_pred():
        """same as previous one

        Returns:
            tuple: as we return multiple data type
        """
        _a = {10, 20, 30}  # return {10, 20, 30}
        _b = [40, 50, 60]
        return (_a, _b)
    print(f'{type(_smth_pred())}')
    _a, _b = _smth_pred()
    # unpacking
    print(_a, _b)
    return


if __name__ == "__main__":
    app.run()
