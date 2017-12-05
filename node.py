class Node:

    def __init__(self, label, edges):
        self.label = label
        self.edges = edges

    def __str__(self):
        out_str = 'Node '+self.label+', edges: '
        for edge in self.edges:
            out_str += str(edge)+' '
        return out_str
