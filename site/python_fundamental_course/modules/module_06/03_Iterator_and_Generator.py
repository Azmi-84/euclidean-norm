import marimo

__generated_with = "0.17.5"
app = marimo.App()


@app.cell
def _():
    a = {10, 12, 13, 41, 522, 6, 72, 80, 29, 10}

    # iterator doesn't allow ordered indexing rathe it allow random indexing
    a_iterator = iter(a)

    print(type(a_iterator))

    print(next(a_iterator), end="|")
    print(next(a_iterator), end="|")
    print(next(a_iterator), end="|")
    print(next(a_iterator), end="|")
    print(next(a_iterator), end="|")
    print(next(a_iterator), end="|")
    print(next(a_iterator), end="|")
    print(next(a_iterator), end="|")
    print(next(a_iterator))

    for i in a:

        """iterator doesn't allow ordered indexing rather it execute it in random indexing. since for loop use the exact same iterator returned by iter(a) and the exact same next() mechanism as our manual cells they necessarily traverse and print the elements in the same sequence."""

        print(i, end=" ")
    return


@app.cell
def _():
    lst = [x**2 for x in range(1000) if x%3!=0]
    # print(lst)


    def data_loader(chunk_size, lst):

        """when we work we large dataset like 100GB or 100TB our random access memory become stuck if the system allowed to work with this dataset at the same time, that's why our system divide them into chunk

        Args:
            chunk_size (int): size of the chunk
            lst (list): list of the dataset
        """

        for i in range(0, len(lst), chunk_size):
            yield lst[i : i + chunk_size]


    b = data_loader(5, lst)
    print(type(b))
    print(next(b))
    print(next(b))
    print(next(b))
    print(next(b))
    print(next(b))
    return


if __name__ == "__main__":
    app.run()
