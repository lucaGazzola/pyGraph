from node import Node


class Graph:

    # constructor
    def __init__(self, nodes):
        self.nodes = nodes

    # returns the shortest path between two nodes given a previous dictionary structure from the dijkstra algorithm
    def get_shortest_path(self,previous, start, end, path):
        if end == start:
            path.append(start)
            path.reverse()
            return path
        path.append(end)
        return self.get_shortest_path(previous, start, previous[end], path)

    def get_node_by_label(self, label):
        for n in self.nodes:
            if n.label == label:
                return n
        return None

    # returns the shortest path between two nodes using dijkstra's algorithm
    def dijkstra(self, start_node, end_node, heuristic=None):

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
            distance[node.label] = None
        distance[start_node] = 0

        # inizialization of the 'previous' map, keeps track of which nodes need to be followed to get the shortest path
        # previous[node] = previous_node_on_shortest_path
        previous = {}

        # start the loop from *start_node*
        current_node = self.get_node_by_label(start_node)

        # while we did not visit all the nodes (or we found the end one)
        while len(not_visited_set) != 0:

            # for each node adjecent to the current one, if they have not already been visited, update distance and previous
            for v in current_node.edges:
                if v in not_visited_set:
                    if not distance[v]:
                        distance[v] = distance[current_node.label] + current_node.get_weight(v)
                        previous[v] = current_node.label
                    elif distance[v] > distance[current_node.label] + current_node.get_weight(v):
                        distance[v] = distance[current_node.label] + current_node.get_weight(v)
                        previous[v] = current_node.label

            # remove current node, since we already visited it
            not_visited_set.remove(current_node.label)

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
            current_node = self.get_node_by_label(min_node)

            # if we reached the end node, call get_shortest_path and return it
            if current_node.label == end_node:
                return self.get_shortest_path(previous, start_node, end_node, [])

        # if no path was found
        return None

    # str()
    def __str__(self):
        out_str = ''
        for node in self.nodes:
            out_str += str(node)
        return out_str
