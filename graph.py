from node import Node
from edge import Edge


class Graph:

    # constructor
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    # returns the weight of an edge, can also be used to check if two edges are connected
    def get_weight(self, node_a, node_b):

        for e in self.edges:
            if e.node_a == node_a:
                if e.node_b == node_b:
                    return e.weight
            if e.node_a == node_b:
                if e.node_b == node_a:
                    return e.weight
        return None

    # returns the shortest path between two nodes given a previous dictionary structure from the dijkstra algorithm
    def get_shortest_path(self,previous, start, end, path):
        if end == start:
            path.append(start)
            path.reverse()
            return path
        path.append(end)
        return self.get_shortest_path(previous, start, previous[end], path)

    # returns a list containing the nodes connected to *node*
    def adj_list(self, node):

        adj = []

        for e in self.edges:
            if node == e.node_a:
                adj.append(e.node_b)
            if node == e.node_b:
                adj.append(e.node_a)

        return adj

    # returns the shortest path between two nodes using dijkstra's algorithm
    def dijkstra(self, start_node, end_node, heuristic = None):

        # trivial
        if start_node == end_node:
            return [start_node]

        # initialization of the set of nodes that have not yet been visited
        not_visited_set = []

        for v in self.nodes:
                not_visited_set += [v.label]

        # initialization of the distance map, that keeps track of the minimum distance of a node from the starting point
        distance = {}

        for node in self.nodes:
            if node.label == start_node:
                distance[node.label] = 0
                continue
            distance[node.label] = None

        # inizialization of the previous map, that keeps track of which nodes need to be followed to get the shortest path
        previous = {}

        # start the loop from *start_node*
        current_node = start_node

        # while we did not visit all the nodes (or we found the end one)
        while len(not_visited_set) != 0:

            # for each node adjecent to the current one, if they have not already been visited, update distance and previous
            for v in self.adj_list(current_node):
                if v in not_visited_set:
                    if not distance[v]:
                        distance[v] = distance[current_node] + self.get_weight(v,current_node)
                        previous[v] = current_node
                    elif distance[v] > distance[current_node] + self.get_weight(v,current_node):
                        distance[v] = distance[current_node] + self.get_weight(v,current_node)
                        previous[v] = current_node

            # remove current node, since we already visited it
            not_visited_set.remove(current_node)

            min_dist = None
            min_node = None

            # determine which node to consider next (the one with the minimum distance from the start)
            for v in not_visited_set:
                # if a-star's algorithm heuristic is used
                if heuristic:
                    # check if the node has already been touched, then check if its path length is the current minimum
                    if distance[v]:
                        if not min_dist:
                            min_dist = distance[v] + heuristic[v]
                            min_node = v
                        elif distance[v] + heuristic[v] < min_dist:
                            min_dist = distance[v] + heuristic[v]
                            min_node = v
                else:
                    # check if the node has already been touched, then check if its path length plus the heuristic metric is the current minimum
                    if distance[v]:
                        if not min_dist:
                            min_dist = distance[v]
                            min_node = v
                        elif distance[v] < min_dist:
                            min_dist = distance[v]
                            min_node = v
            current_node = min_node

            # if we reached the end node, call get_shortest_path and return it
            if current_node == end_node:
                return self.get_shortest_path(previous, start_node, end_node, [])

        # if no path was found
        return None

    # str()
    def __str__(self):
        out_str = ''
        for node in self.nodes:
            out_str += str(node)
        return out_str
