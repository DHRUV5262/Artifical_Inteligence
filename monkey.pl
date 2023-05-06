move(state(middle,onbox,middle,hasnot),
    grasp,
    state(middle,onbox,middle,has)).
move(state(P,onfloor,P,H),
    climb,
    state(P,onbox,P,H)).
move(state(P,onfloor,P,H),
    drag(P,P1),
    state(P1,onfloor,P1,H)).
move(state(P,onfloor,Z,H),
    walk(P,P1),
    state(P1,onfloor,Z,H)).

canget(state(_,_,_,has)).
canget(State1):-
    move(State1,_,State2),
    canget(State2).
