class Edge:

    def __init__(self, node_a, node_b, weight):
        self.node_a = node_a
        self.node_b = node_b
        self.weight = weight

    def __str__(self):
        return self.node_a+'-'+self.node_b+' '+str(self.weight)

