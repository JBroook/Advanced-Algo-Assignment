class Graph:
    def __init__(self, size):
        self.matrix = [ [None]*size for _ in range(size)]
        self.size = size
        self.vertex_data = []

    def add_vertex(self, val):
        if len(self.vertex_data)<self.size:
            self.vertex_data.append(val)
        else:
            raise ValueError("No space left in the graph")

    def add_edge(self, src, dest):
        i_src = self.vertex_data.index(src)
        i_dest = self.vertex_data.index(dest)
        self.matrix[i_src][i_dest] = 1

    def display(self):
        for i in self.matrix:
            print(i)

    def list_outgoing_vertex(self, vertex):
        i_vertex = self.vertex_data.index(vertex)
        outgoing_row = self.matrix[i_vertex]
        for i in range(len(outgoing_row)):
            if outgoing_row[i]:
                print(self.vertex_data[i])

# g = Graph(4)
# g.add_vertex("A")
# g.add_vertex("B")
# g.add_vertex("C")
# g.add_vertex("D")
# g.add_edge("A", "B")
# g.add_edge("A", "C")
# g.add_edge("D", "A")
# g.add_edge("C", "B")
#
# g.display()
#
# g.list_outgoing_vertex("A")