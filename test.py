from graph import Graph
from edge import Edge
from node import Node

# edges

sa = Edge('s','a',7)
sb = Edge('s','b',2)
sc = Edge('s','c',3)
ad = Edge('a','d',4)
ab = Edge('a','b',3)
df = Edge('d','f',5)
db = Edge('d','b',4)
bh = Edge('b','h',1)
hf = Edge('h','f',3)
hg = Edge('h','g',2)
ge = Edge('g','e',2)
ek = Edge('e','k',5)
ki = Edge('k','i',4)
jk = Edge('j','k',4)
ij = Edge('i','j',6)
li = Edge('l','i',4)
jl = Edge('j','l',4)
lc = Edge('l','c',2)

edges = [sa,sb,sc,ad,ab,df,db,bh,hf,hg,ge,ek,ki,jk,ij,li,jl,lc]

# vertices

s = Node('s',[sa,sb,sc])
a = Node('a',[sa,ad,ab])
b = Node('b',[db,ab,bh,sb])
c = Node('c',[sc,lc])
d = Node('d',[ad,df,db])
e = Node('e',[ek,ge])
f = Node('f',[df,hf])
g = Node('g',[ge,hg])
h = Node('h',[hf,hg,bh])
k = Node('k',[ek,ki,jk])
l = Node('l',[li,jl,lc])
i = Node('i',[li,ij,ki])
j = Node('j',[jl,ij,jk])

vertices = [a,b,c,d,e,f,g,h,k,l,i,j,s]

# graph

graph = Graph(vertices,edges)

# test

print(graph)

start = 's'
end = 'e'

heuristic = dict({('a',9),('b',7),('c',8),('d',8),('e',0),('f',6),('g',3),('h',6),('k',3),('l',6),('i',4),('j',4),('s',10)})

print('shortest path from '+start+' to '+end+': '+str(graph.dijkstra(start,end,heuristic)))
