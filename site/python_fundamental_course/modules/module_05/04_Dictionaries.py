import marimo

__generated_with = "0.17.5"
app = marimo.App()


@app.cell
def _():
    dic = {"name": "Abdullah Al Azmi", "age": 24, "city": "Dhaka", "country": "Bangladesh"}
    print(dic, type(dic))
    return (dic,)


@app.cell
def _(dic):
    # accessing value
    print(dic.keys())
    print(f"Name: {dic['name']}, Age: {dic['age']}, City: {dic['city']}, Country: {dic['country']}")
    return


@app.cell
def _(dic):
    # assign new value
    dic["age"] = 25
    print(dic)
    return


@app.cell
def _():
    dic_1 = {'name': 'Abdullah Al Azmi', 'age': 24, 'city': 'Dhaka', 'country': 'Bangladesh', 'name': 'Phitron'}
    print(dic_1)  # duplicate key will be overwritten
    return (dic_1,)


@app.cell
def _(dic_1):
    print(dic_1.get('name'))
    print(dic_1.get('age'))
    return


@app.cell
def _(dic_1):
    print(dic_1.get('learning'))
    print(dic_1.get('learning', 0))  # default value
    print(dic_1.get('learning', 'Python'))  # default value
    print(dic_1)
    # reason for getting "None" for the below call is the default value of previous key "learning" doesn't saved, we must have to specify it every time we cell get() function.
    print(dic_1.get('code'))
    return


@app.cell
def _(dic_1):
    dic_1['learning'] = 'Python'
    print(dic_1)
    dic_1.update({'OS': 'Linux'})
    print(dic_1)
    dic_1.update({'GUI': 'Gnome', 'Kernel': 6.18})
    print(dic_1)
    return


@app.cell
def _(dic_1):
    # deletion
    del dic_1['learning']
    print(dic_1)
    return


@app.cell
def _():
    # key in dictionary have to be immutable
    # dic_01 = {[1, 2, 3]: "Phitron"}
    # TypeError: cannot use 'list' as a dict key (unhashable type: 'list')

    dic_01 = {(1, 2, 3): "Phitron"}
    print(dic_01)
    return


@app.cell
def _(dic_1):
    keys = dic_1.keys()
    values = dic_1.values()
    items = dic_1.items()  # this returns a list of tuples of key-value pairs
    print(keys)
    print(values)
    print(items)
    dic_1['language'] = 'Python'
    print(keys)
    print(values)  # we don't have to call keys() again, it is updated automatically
    print(items)  # we don't have to call values() again, it is updated automatically  # we don't have to call items() again, it is updated automatically
    return


@app.cell
def _(dic_1):
    for _key, _value in dic_1.items():
        print(_key, _value, end=' | ')
    return


@app.cell
def _():
    # dict comprehension
    _dic_comprehension = {x: x ** 2 for x in range(1, 11) if x % 2 == 0}
    print(_dic_comprehension)
    return


@app.cell
def _():
    dic_comprehension = {x: k ** 2 for x, k in zip(range(1, 11), range(1, 11)) if k % 2 == 0}
    # zip() method create a pair of value like (1, 1), (2, 2),..., (10, 10) and as the k have to be even the only even pairs are passed, that's why the keys aren't 1, 2, 3...
    print(dic_comprehension)
    return (dic_comprehension,)


@app.cell
def _():
    coordinates = [(10, 10.5), (20, 20.5), (30, 30.5)]
    locations = ['dhaka', 'chattogram', 'sylhet']
    zone = {_key: _value for _key, _value in zip(coordinates, locations)}
    print(zone)
    return


@app.cell
def _(dic_comprehension):
    print(dic_comprehension.pop(2))  # we've to provide the key otherwise it'll show error
    print(dic_comprehension)

    dic_comprehension.popitem()  # popitem() doesn't take any argument and it remove the last key-value pair
    return


@app.cell
def _():
    _dict_comprehension = {_key: val for _key in range(11) for val in range(11)}
    print(_dict_comprehension)

    for _key in range(11):
        for val in range(11):
            _dict_comprehension[_key] = val
    print(_dict_comprehension)
    return


@app.cell
def _():
    _members = ('a', 'b', 'c', 'd')
    print(dict.fromkeys(_members))
    _value = 'Code'
    print(dict.fromkeys(_members, _value))
    return


if __name__ == "__main__":
    app.run()
