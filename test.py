from graph import Graph
from edge import Edge
from node import Node

# nodes

s = Node('s',{'a':7,'b':2,'c':3})
a = Node('a',{'s':7,'b':3,'d':4})
b = Node('b',{'a':3,'s':2,'d':4,'h':1})
c = Node('c',{'s':3,'l':2})
d = Node('d',{'a':4,'b':4,'f':5})
e = Node('e',{'g':2,'k':5})
f = Node('f',{'h':3,'d':5})
g = Node('g',{'e':2,'h':2})
h = Node('h',{'f':3,'g':2,'b':1})
k = Node('k',{'e':5,'i':4,'j':4})
i = Node('i',{'k':4,'j':6,'l':4})
j = Node('j',{'k':4,'i':6,'l':4})
l = Node('l',{'c':2,'i':4,'j':4})

nodes = [a,b,c,d,e,f,g,h,k,l,i,j,s]

# graph

graph = Graph(nodes)

# test

print(graph)

start = 's'
end = 'e'

heuristic = dict({('a',9),('b',7),('c',8),('d',8),('e',0),('f',6),('g',3),('h',6),('k',3),('l',6),('i',4),('j',4),('s',10)})

print('shortest path from '+start+' to '+end+': '+str(graph.dijkstra(start,end,heuristic)))
