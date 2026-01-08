import marimo

__generated_with = "0.17.8"
app = marimo.App()


@app.cell
def _():
    """List Comprehension Problem | Platform: Hackerrank | Link: https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true | Helping blog: https://python-course.eu/advanced-python/list-comprehension.php"""
    return


@app.cell
def _():
    x = int(input())
    y = int(input())
    z = int(input())
    _n = int(input())

    _lst = [[a, b, c] for a in range(0, x + 1) for b in range(0, y + 1) for c in range(0, z + 1) if a + b + c != _n]
    print(_lst)
    return


@app.cell
def _():
    """Nested List Problem | Link: https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true | Helping blog: https://discuss.python.org/t/for-loop-with-undersore/40538/3"""
    return


@app.cell
def _():
    students = []

    for _ in range(int(input())):
        _name = input()
        score = float(input())
        students.append([_name, score])
    
    second_lowest = sorted({x for _, x in students})[1]

    for _name in sorted([_n for _n, s in students if s == second_lowest]):
        print(_name)
    # names = sorted([n for n, s in students if s == second_lowest])
    # print(names)
    # print(sorted([n for n, s in students if s == second_lowest]))
    print(second_lowest)
    print(students)
    return


@app.cell
def _():
    """Dictionary Problem | Link: https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true"""
    return


@app.cell
def _():
    _n = int(input())
    student_marks = {}

    for _ in range(_n):
        _name, *line = input().split()
        '`name` gets the first word and `*line` gets all remaining values as a list'
        scores = list(map(float, line))
        student_marks[_name] = scores
    query_name = input()
    summation = 0
    # print(student_marks.values())
    for _name, _item in student_marks.items():
        length = len(_item)
        if _name == query_name:
            summation = sum(_item) / length
    print(format(summation, '.2f'))
    return


@app.cell
def _():
    N = int(input())
    _lst = []
    for _item in range(N):
        inputs = input()
        parts = inputs.split()
        cmd = parts[0]
        if cmd in ['insert', 'append', 'remove']:
            args = [int(x) for x in parts[1:]]
            getattr(_lst, cmd)(*args)
        elif cmd in ['sort', 'reverse', 'pop']:
            if len(parts) > 1:
                index = int(parts[1])
                getattr(_lst, cmd)(index)
            else:
                getattr(_lst, cmd)()
        elif cmd == 'print':
            print(_lst)
    print(_lst)
    return


@app.cell
def _():
    _n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))
    return


if __name__ == "__main__":
    app.run()
