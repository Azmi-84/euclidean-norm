import marimo

__generated_with = "0.17.2"
app = marimo.App()


@app.cell
def _():
    # NumPy IO operation
    path = '/home/abdullahalazmi/Programming/Phitron-AI-ML/Modules/Module-11/shear_cutting_info.txt'
    try:
        with open(path, 'w+') as _file:
            _file.write(','.join(['Name', 'ID', 'Time']) + '\n')
            data = [f'{k},{k},{k}' for k in range(21)]
            _file.write('\n'.join(data))
            _file.seek(0)
    except OSError:
        print('OS Error')
    except Exception as e:
        print(f'{e}')  # print(file.read())  # print('abcd')
    return (path,)


@app.cell
def _(path):
    import numpy as np
    from io import StringIO
    _file = np.genfromtxt(path, delimiter=',', names=True, dtype=None, encoding='utf-8')
    # file = np.genfromtxt(path, delimiter=',') # without header
    mask = _file['ID'] != 0  # with header
    # print(file)
    # print(file.ndim, file.size, file.shape, file.dtype.names)
    # print(np.count_nonzero(file['ID']==0), np.count_nonzero(file['Name']==0), np.count_nonzero(file['Time']==0))
    # removing rows less than equal to zero
    # print(filtered)
    # np.savetxt(path, filtered, delimiter=',', fmt='%.2f', header=','.join(file.dtype.names), comments='file without less than or equal zero rows\n')
    filtered = _file[mask]
    return


if __name__ == "__main__":
    app.run()
