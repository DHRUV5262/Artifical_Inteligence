import copy

def get_states(state: list) -> list:
    states = list()
    
    for row in range(0, len(state)):
        for col in range(0, len(state[row])):
            if(state[row][col] == 0):
                if(row==0 or row==1):
                    tmp_state = copy.deepcopy(state)
                    tmp_state[row][col], tmp_state[row+1][col] = tmp_state[row+1][col], tmp_state[row][col]
                    states.append(tmp_state)

                if(row==1 or row==2):
                    tmp_state = copy.deepcopy(state)
                    tmp_state[row][col], tmp_state[row-1][col] = tmp_state[row-1][col], tmp_state[row][col]
                    states.append(tmp_state)
                
                if(col==0 or col==1):
                    tmp_state = copy.deepcopy(state)
                    tmp_state[row][col], tmp_state[row][col+1] = tmp_state[row][col+1], tmp_state[row][col]
                    states.append(tmp_state)

                if(col==1 or col==2):
                    tmp_state = copy.deepcopy(state)
                    tmp_state[row][col], tmp_state[row][col-1] = tmp_state[row][col-1], tmp_state[row][col]
                    states.append(tmp_state)
    return states

def DFS(start:list, goal:list) -> None:
    print(start)
    
    if (start == goal): return

    if (start not in closed):
        closed.append(start)
        states = get_states(start)
        for state in states: open.append(state)
    
    # POP
    top = open[len(open)-1]
    open.remove(open[len(open)-1])

    DFS(top, goal)

def BFS(start:list, goal:list) -> None:
    print(start)
    if (start == goal): return
    
    if (start not in closed):
        closed.append(start)
        states = get_states(start)
        for state in states: open.append(state)
    
    # DEQUEUE
    top = open[0]
    open.remove(open[0])

    BFS(top, goal)


if __name__ == "__main__":
    goal = [
        [1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]
    ]
    
    puzzle = [
        [2, 8, 1],
        [0, 4, 3],
        [7, 6, 5]
    ]

    open = list()
    closed = list()

    BFS(puzzle, goal)
