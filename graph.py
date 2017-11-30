from vertex import Vertex
from edge import Edge


class Graph:

    # constructor
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

    # returns the weight of an edge, can also be used to check if two edges are connected
    def get_weight(self, vertex_a, vertex_b):

        for e in self.edges:
            if e.vertex_a == vertex_a:
                if e.vertex_b == vertex_b:
                    return e.weight
            if e.vertex_a == vertex_b:
                if e.vertex_b == vertex_a:
                    return e.weight
        return None

    # returns the shortest path between two vertices given a previous dictionary structure from the dijkstra algorithm
    def get_shortest_path(self,previous, start, end, path):
        if end == start:
            path.append(start)
            path.reverse()
            return path
        path.append(end)
        return self.get_shortest_path(previous, start, previous[end], path)

    # returns a list containing the vertices connected to *vertex*
    def adj_list(self, vertex):

        adj = []

        for e in self.edges:
            if vertex == e.vertex_a:
                adj.append(e.vertex_b)
            if vertex == e.vertex_b:
                adj.append(e.vertex_a)

        return adj

    # returns the shortest path between two vertices using dijkstra's algorithm
    def a_star(self, start_vertex, end_vertex, heuristic=None):

        # trivial
        if start_vertex == end_vertex:
            return [start_vertex]

        # initialization of the set of vertices that have not yet been visited
        not_visited_set = []

        for v in self.vertices:
                not_visited_set += [v.label]

        # initialization of the distance map, that keeps track of the minimum distance of a vertex from the starting point
        distance = {}

        for vertex in self.vertices:
            if vertex.label == start_vertex:
                if heuristic:
                    distance[vertex.label] = heuristic[vertex.label]
                else:
                    distance[vertex.label] = 0
                continue
            distance[vertex.label] = None

        # inizialization of the previous map, that keeps track of which vertices need to be followed to get the shortest path
        previous = {}

        # start the loop from *start_vertex*
        current_vertex = start_vertex

        # while we did not visit all the nodes (or we found the end one)
        while len(not_visited_set) != 0:

            # for each vertex adjecent to the current one, if they have not already been visited, update distance and previous
            for v in self.adj_list(current_vertex):
                if v in not_visited_set:
                    if heuristic:
                        if not distance[v]:
                            distance[v] = distance[current_vertex] + self.get_weight(v,current_vertex) + heuristic[v]
                            previous[v] = current_vertex
                        elif distance[v] > distance[current_vertex] + self.get_weight(v,current_vertex) + heuristic[v]:
                            distance[v] = distance[current_vertex] + self.get_weight(v,current_vertex) + heuristic[v]
                            previous[v] = current_vertex
                    else:
                        if not distance[v]:
                            distance[v] = distance[current_vertex] + self.get_weight(v,current_vertex)
                            previous[v] = current_vertex
                        elif distance[v] > distance[current_vertex] + self.get_weight(v,current_vertex):
                            distance[v] = distance[current_vertex] + self.get_weight(v,current_vertex)
                            previous[v] = current_vertex

            # remove current vertex, since we already visited it
            not_visited_set.remove(current_vertex)

            min_dist = None
            min_vertex = None

            # determine which vertex to consider next (the one with the minimum distance from the start)
            for v in not_visited_set:

                # here get_weight is used to check if two vertices are connected
                if self.get_weight(v,current_vertex):
                    if not min_dist:
                        min_dist = distance[v]
                        min_vertex = v
                    elif distance[v] < min_dist:
                        min_dist = distance[v]
                        min_vertex = v

            current_vertex = min_vertex

            # if we reached the end vertex, call get_shortest_path and return it
            if current_vertex == end_vertex:
                return self.get_shortest_path(previous, start_vertex, end_vertex, [])

        # if no path was found
        return None

    # str()
    def __str__(self):
        out_str = ''
        for vertex in self.vertices:
            out_str += str(vertex)
        return out_str
