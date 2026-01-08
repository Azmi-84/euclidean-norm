import marimo

__generated_with = "0.17.2"
app = marimo.App()


@app.cell
def _():
    path = '/home/abdullahalazmi/Programming/Phitron-AI-ML/Module-07/test.txt'
    with open(path, 'w') as _file:
        'when we use "w" mode, the file is opened as writing mode and when we add new lines it overwrite the existing file\n    '
        _file.write('Hello test file line 1.')
        _file.write('Hello test file line 2.')
        _file.write('Hello test file line 3.')
    with open(path, 'r') as _file:
        print(_file.read(), end='')
    return (path,)


@app.cell
def _(path):
    with open(path, 'w+') as _file:
        "when we use 'w+' mode it allow us to write and read file simultaneously and we don't have to worry about again reading option.\n    "
        _file.write('Hello test file with write plus read mode line 1.')
        _file.write('Hello test file with write plus read mode line 2.')
        _file.write('Hello test file with write plus read mode line 3.')
        _file.seek(0)
        print(_file.read(), end='')
    return


@app.cell
def _(path):
    with open(path, 'a+') as _file:
        'when we use "a" mode, the file is opened as append mode and rather overwriting the existing file it then add context at the end of the line.\n    '
        _file.write('Hello test 2 file.')
        _file.write('Hello test 2 file.')
        _file.write('Hello test 2 file.')
        _file.seek(0)
        print(_file.read(), end='')
    return


@app.cell
def _(path):
    with open(path, 'a+') as _file:
        _file.write('\nNew Line ONE\n')
        _file.write('New Line TWO\n')
        _file.write('New Line THREE\n')
        _file.write('New Line FOUR\n')
        _file.seek(0)
        content = _file.readlines()
        print(f'Content of the file: \n{content}\n')
        content = list(map(str.strip, content))
        print(f'Content of the mapped file for removing new line: \n{content}\n')
        filtered_content = list(filter(lambda val: len(val) > 15, content))  # removing the '/n' using the strip() function.
        print(f'Filtered Content of the file for length greater than 15: \n{filtered_content}')  # print(file.read(), end="")
    return


if __name__ == "__main__":
    app.run()
