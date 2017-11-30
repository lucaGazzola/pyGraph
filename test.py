from graph import Graph
from edge import Edge
from vertex import Vertex

# edges

ab = Edge('a','b',4)
ae = Edge('a','e',7)
ac = Edge('a','c',1)
cb = Edge('c','b',6)
ce = Edge('c','e',1)
cd = Edge('c','d',11)
ed = Edge('e','d',2)
bd = Edge('d','b',5)
eg = Edge('e','g',5)
dg = Edge('g','d',10)
df = Edge('d','f',2)
gf = Edge('g','f',3)

edges = [ab,ae,ac,cb,ce,cd,ed,bd,eg,dg,df,gf]

# vertices

a = Vertex('a',[ab,ae,ac])
b = Vertex('b',[ab,bd,cb])
c = Vertex('c',[ac,cd,cb,ce])
d = Vertex('d',[bd,cd,dg,ed,df])
e = Vertex('e',[eg,ce,ae,ed])
f = Vertex('f',[df,gf])
g = Vertex('g',[eg,gf,dg])

vertices = [a,b,c,d,e,f,g]

# graph

graph = Graph(vertices,edges)

# test

print(graph.dijkstra('a','f'))
