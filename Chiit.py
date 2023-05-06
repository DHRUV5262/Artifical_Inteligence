# BFS wdwdawdawd

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

open = list()
closed = list()

def BFS(start:str, goal:str) -> None:
    print(start, end=' ')
    if (start == goal): return
    if (start not in closed):
        closed.append(start)
        for item in graph[start]: open.append(item)
    # DEQUEUE
    front = open[0]
    open.remove(open[0])

    BFS(front, goal)

BFS(start=0, goal=4)

# DFS 

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

# Eight pUzzel

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

# waterjug

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


# Reverse list 

reverse_list_length([], 0, []).
reverse_list_length([H|T], N, R) :-
   reverse_list_length(T, N1, R1),
   N is N1 + 1,
   append(R1, [H], R).

main :-
   write('Enter a list: '),
   read(List),
   reverse_list_length(List, Length, Reversed),
   write('Length of the list is '), write(Length), nl,
   write('Reversed list is '), write(Reversed), nl.


# main.



# Monkey 

move(state(middle,onbox,middle,hasnot),
     grasp,
     state(middle,onbox,middle,has)).

move(state(P,onfloor,P,H),
     climb,
     state(P,onbox,P,H)).

move(state(P1,onfloor,P1,H),
     push(P1,P2),
     state(P2,onfloor,P2,H)).

move(state(P1,onfloor,B,H),
     walk(P1,P2),
     state(P2,onfloor,B,H)).

canget(state(_,_,_,has)).

canget(State1):-
    move(State1,_,State2),
    canget(State2).

# trace.
# canget(state(atdoor,onfloor,atwindow,hasnot)).

# Sum

sum_series(0, 0).
sum_series(N, Sum) :-
   N > 0,
   N1 is N - 1,
   sum_series(N1, Sum1),
   Sum is Sum1 + N.

main :-
    write('Enter the number: '),
    read(N),
    sum_series(N, Sum),
    write('Sum of the series is '), write(Sum), nl.


# main.

# factorial

factorial(0, 1).
factorial(N, F) :-
   N > 0,
   N1 is N - 1,
   factorial(N1, F1),
   F is N * F1.

main :-
   write('Enter a number: '),
   read(N),
   factorial(N, F),
   write('Factorial of '), write(N), write(' is '), write(F), nl.

# main. 
# or
# factorial(5,F)

# Box Problem

%Ann and Bill have boxes with the same colour.
%Don and Eric have boxes with the same colour.
%Charlie and Don have boxes with the same size.
%Eric's box is smaller than Bill's

% Define numbers for each box
getbox(1). getbox(2). getbox(3). getbox(4). getbox(5).

% Define Box numbers, colour, size
box(1,black,3).
box(2,black,1).
box(3,white,1).
box(4,black,2).
box(5,white,3).

owners(A,B,C,D,E):-
 getbox(A), getbox(B), getbox(C), getbox(D), getbox(E),
 A\=B, A\=C, A\=D, A\=E,
 B\=C, B\=D, B\=E,
 C\=D, C\=E,
 D\=E,
 box(A,ColorA,_), box(B,ColorA,_), 
 box(D,ColorD,_), box(E,ColorD,_),
 box(C,_,SizeC), box(D,_,SizeC),
 box(E,_,SizeE), box(B,_,SizeB),
 SizeE < SizeB.

#  owners(Ann, Bill, Charlie, Don, Eric).