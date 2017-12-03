from graph import Graph
from edge import Edge
from vertex import Vertex

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

s = Vertex('s',[sa,sb,sc])
a = Vertex('a',[sa,ad,ab])
b = Vertex('b',[db,ab,bh,sb])
c = Vertex('c',[sc,lc])
d = Vertex('d',[ad,df,db])
e = Vertex('e',[ek,ge])
f = Vertex('f',[df,hf])
g = Vertex('g',[ge,hg])
h = Vertex('h',[hf,hg,bh])
k = Vertex('k',[ek,ki,jk])
l = Vertex('l',[li,jl,lc])
i = Vertex('i',[li,ij,ki])
j = Vertex('j',[jl,ij,jk])

vertices = [a,b,c,d,e,f,g,h,k,l,i,j,s]

# graph

graph = Graph(vertices,edges)

# test

print(graph)

start = 's'
end = 'e'

print('shortest path from '+start+' to '+end+': '+str(graph.dijkstra('s','e')))
