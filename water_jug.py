import copy

class Jug:
    def __init__(self, max: int) -> None:
        self.MAX = max
        self.value = 0

    def fill(self) -> None:
        self.value = self.MAX
    
    def empty(self) -> None:
        self.value = 0
    
    def clip(self) -> None:
        if (self.value > self.MAX): 
            self.value = self.MAX
        elif (self.value < 0):
            self.value = 0

    def __str__(self) -> str:
        return str(self.value)

def transfer(one: Jug, other: Jug) -> None:
    old_value = other.value
    other.value += one.value
    other.clip()
    
    difference = other.value - old_value
    one.value -= difference
    one.clip()

def get_states(one: Jug, other: Jug) -> list:
    states = list()

    jugA = copy.deepcopy(one)
    jugB = copy.deepcopy(other)
    if (jugA.value < jugA.MAX):
        jugA.fill()
        states.append((jugA, jugB))

    jugA = copy.deepcopy(one)
    jugB = copy.deepcopy(other)
    if (jugB.value < jugB.MAX):
        jugB.fill()
        states.append((jugA, jugB))

    jugA = copy.deepcopy(one)
    jugB = copy.deepcopy(other)
    if (jugA.value > 0):
        jugA.empty()
        states.append((jugA, jugB))
    
    jugA = copy.deepcopy(one)
    jugB = copy.deepcopy(other)
    if (jugB.value > 0):
        jugB.empty()
        states.append((jugA, jugB))

    jugA = copy.deepcopy(one)
    jugB = copy.deepcopy(other)
    if (jugA.value > 0 and jugB.value < jugB.MAX):
        transfer(jugA, jugB)
        states.append((jugA, jugB))

    jugA = copy.deepcopy(one)
    jugB = copy.deepcopy(other)
    if (jugB.value > 0 and jugA.value < jugA.MAX):
        transfer(jugB, jugA)
        states.append((jugA, jugB))

    return states

def DFS(start:tuple, goal:tuple) -> None:
    print('(' + str(start[0]) + ', ' + str(start[1]) + ')', end=' ')
    
    if (start[0].value == goal[0].value and start[1].value == goal[1].value): return
    
    visited = False
    for item in closed:
        if (item[0].value == start[0].value and item[1].value == start[1].value):
            visited = True

    if (not visited):
        closed.append(start)
        states = get_states(start[0], start[1])
        for item in states: open.append(item)
    
    # POP
    top = open[len(open)-1]
    open.remove(open[len(open)-1])

    DFS(top, goal)

def BFS(start:tuple, goal:tuple) -> None:
    print('(' + str(start[0]) + ', ' + str(start[1]) + ')', end=' ')
    
    if (start[0].value == goal[0].value and start[1].value == goal[1].value): return
    
    visited = False
    for item in closed:
        if (item[0].value == start[0].value and item[1].value == start[1].value):
            visited = True

    if (not visited):
        closed.append(start)
        states = get_states(start[0], start[1])
        for item in states: open.append(item)
    
    # DEQUEUE
    top = open[0]
    open.remove(open[0])

    BFS(top, goal)

if __name__ == "__main__":
    one = Jug(5)
    other = Jug(4)
    
    goal1 = Jug(5)
    goal1.value = 2
    goal2 = Jug(4)
    goal2.value = 0

    open = list()
    closed = list()
    print('DFS:', end=' ')
    DFS((one, other), (goal1, goal2))
    print('\nBFS:', end=' ')
    BFS((one, other), (goal1, goal2))
    print()
