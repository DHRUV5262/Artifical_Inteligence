graph = {
    0 : [1, 2],
    1 : [0, 3, 4],
    2 : [0],
    3 : [1],
    4 : [2, 3]
}

tree = {
    1 : [2, 3, 4],
    2 : [5, 6],
    3 : [],
    4 : [7, 8],
    5 : [9, 10],
    6 : [],
    7 : [11, 12],
    8 : [],
    9 : [],
    10 : [],
    11 : [],
    12 : []
}

open = []
closed = []

def DFS(start:str, goal:str) -> None:
    print(start, end=' ')
    if (start == goal): return
    if (start not in closed):
        closed.append(start)
        for item in tree[start]: open.append(item)
    # POP
    top = open[len(open)-1]
    open.remove(open[len(open)-1])

    DFS(top, goal)

DFS(start=1, goal=10)
