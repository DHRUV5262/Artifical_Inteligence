len([],0).
len([_|T],R):-
    len(T,R1),
    R is R1+1.


rev([],[]).
rev([H|T],R):-
    rev(T,R1),
    append(R1,[H],R).
