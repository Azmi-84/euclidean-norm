import marimo

__generated_with = "0.17.2"
app = marimo.App()


@app.cell
def _():
    path = '/home/abdullahalazmi/Programming/Phitron-AI-ML/Module-07/sample.txt'
    _file = open(path, 'r')
    _content = _file.read()  # file open in read mode only, if we don't mention anything this is the default mode
    print(_content, type(_content))
    return (path,)


@app.cell
def _(path):
    _file = open(path, 'r')
    _content = _file.readlines()
    print(_content, type(_content))
    print(_file.closed)
    _file.close()
    print(_file.closed)
    return


@app.cell
def _(path):
    with open(path, 'r') as _file:  # when we use the 'with' statement, we don't have to worry about closing the file
        _content = _file.readlines()
        print(_content, type(_content))
    print(_file.closed)
    return


@app.cell
def _(path):
    with open(path, 'r') as _file:
        for _line in _file:
            print(_line)
    return


@app.cell
def _(path):
    with open(path, 'r') as _file:
        for _line in _file:
            print(_line, end='')
    return


@app.cell
def _(path):
    with open(path, 'r') as _file:
        for _line in _file:
            l = _line.strip()
            print(l)
    return


if __name__ == "__main__":
    app.run()
