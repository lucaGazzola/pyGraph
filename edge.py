class Edge:

    def __init__(self, vertex_a, vertex_b, weight):
        self.vertex_a = vertex_a
        self.vertex_b = vertex_b
        self.weight = weight

    def __str__(self):
        return self.vertex_a+'-'+self.vertex_b+' '+str(self.weight)

