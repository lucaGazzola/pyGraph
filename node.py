class Node:

    def __init__(self, label, edges):
        self.label = label
        self.edges = edges

    def get_weight(self, node_b):
        if node_b in self.edges:
            return self.edges[node_b]
        return None

    def __str__(self):
        out_str = 'Node '+self.label+', edges: '
        for key in self.edges:
            out_str += self.label+'-'+key+': '+str(self.edges[key])+' '
        return out_str
