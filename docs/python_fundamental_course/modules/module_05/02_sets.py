import marimo

__generated_with = "0.17.5"
app = marimo.App()


@app.cell
def _():
    # Set is a in-built python data structure, which is mutable, store unique and unordered elements meaning we can't do indexing and slicing on set

    A = {1, 2, 3}
    print(A, type(A))

    B = {}
    print(type(B))
    # we can't declare an empty set using only bracket rather we've to do type casting for it

    C = set()
    print(type(C))
    return


@app.cell
def _():
    D = {1, 5, 4, 3, 2}
    print(D)  # no duplicate

    # accessing
    for s in D:
        print(s, end=" ")

    if 2 in D:
        print("\n2 is present")
    else:
        print("\nnot present")

    print(5 in D)
    return


@app.cell
def _():
    E = {2, 3, 4, 4, 5, 6, 8, 8, 0, 10, 1, 2}
    print(E)

    E.add(4) # no duplicate
    print(E)

    # add() method actually don't add elements at the end rather it's insert the value at the desired position of the sorted set
    E.add(7)
    print(E)

    E.add(-1)
    print(E)
    return


@app.cell
def _():
    F = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    G = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
    _I = {4, 3, 5, 6, 2, 6, 2, 4, 7, 5, 23, 24, 53}
    print(f'Union of F and G: {F.union(G)}')
    # union() return a set containing the union of sets
    print(f'Union of F, G and I: {F.union(G).union(_I)}')
    print(f'Intersection of F and G: {F.intersection(G)}')
    print(f'Intersection of F, G and I: {F.intersection(G).intersection(_I)}')
    # intersection() return a set containing the intersection of sets
    print(f'Union of I with Intersection of F and G: {F.intersection(G).union(_I)}')
    print(F.isdisjoint(G))
    # print(G.union(F)) # same result
    # print(G.intersection(F)) # same result
    # intersection and union or union and intersection
    # print(f"Union of I with Intersection of G and F: {G.intersection(F).union(I)}") # same result
    # print(f"Union of I with Intersection of F and G: {(F.intersection(G)).union(I)}") # same result
    # isdisjoint() method is used to determine if two sets have no common elements
    # print({1, 2, 3}.isdisjoint({4, 5})) # True
    # issubset() method is used to determine if one set is subset of another one
    print(F.issubset(G))
    return


@app.cell
def _():
    H = {1, 2, 3}
    _I = {1, 2, 3, 4, 5}
    print(H.issubset(_I))
    print(_I.issubset(H))
    print(_I.issuperset(H))
    print(H.issuperset(_I))
    return


@app.cell
def _():
    # difference() method returns a new set containing all elements present in the original set but not found in any of the specified iterable arguments. It is used to compute the mathematic set difference, A-(B ∪ C ∪....), without modifying the original set

    J = {1, 2, 3, 4, 5, 6, 8, 10}
    K = {2, 3, 4, 5, 7}
    L = {3, 5, 6, 7}
    # K ∪ L = {2, 3, 4, 5, 6, 7} then J - (K ∪ L) = {1, 8, 10, ....}

    J.difference(K, L)
    return (L,)


@app.cell
def _(L):
    # pop() remove an arbitrary element from the set since sets are unordered and don't support indexing

    print(L.pop())
    print(L)
    return


@app.cell
def _(L):
    # remove() method removes the specified element not index

    L.remove(5)
    print(L)
    return


@app.cell
def _():
    # symmetric_difference return a new set containing all elements that are not either in the first set or in the second set

    M = {2, 3, 4, 5, 6, 7}
    N = {6, 7, 8, 9, 10}

    print(M ^ N)
    return


if __name__ == "__main__":
    app.run()
