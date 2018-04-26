os(16.04,ubuntu,2000,1000,['lxml', 'gcc', 'foo', 'bar'],64,200).
os(23,fedore,1500,700,['lib_a', 'lib_b', 'lib_image', 'bar'],32,201).
machine(6144,200,16384,physical,16,120).
machine(256,201,4096,virtual,2,121).
softwareapp(mysql+server,['lxml', 'gcc', 'foo', 'bar'],[200, 201],4,2,512,300).
softwareapp(apache+web+server,['lib_a', 'gcc', 'lib_b', 'bar'],[200],1,2,512,301).
softwareapp(imageprocessing+server,['keras', 'gcc', 'lib_image', 'bar'],[200],100,8,2,302).

compare(P,I) :- P=<I.
all_from_first_in_second(List1, List2) :-
    forall(member(Element,List1), member(Element,List2)).

list(S) :- softwareapp(_,L,O,D,C,R,S),member(O1,O),machine(Da,O1,Ra,_,Cp,Y),compare(R,Ra),compare(D,Da),compare(C,Cp),os(_,_,_,_,L1,_,O1),all_from_first_in_second(L,L1),writeln(Y).
newlist(S,Y) :- softwareapp(_,L,O,D,C,R,S),member(O1,O),machine(Da,O1,Ra,_,Cp,Y),compare(R,Ra),compare(D,Da),compare(C,Cp),os(_,_,_,_,L1,_,O1),all_from_first_in_second(L,L1),writeln(Y).
