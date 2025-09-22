class Graph:
    def __init__(self, size):
        self.adjacency_list = {}
        self.size = size
        self.vertex_data = {}

    def add_vertex(self, key, val):
        if len(self.vertex_data)<self.size:
            self.vertex_data[key] = val
            self.adjacency_list[key] = []
        else:
            raise ValueError("No space left in the graph")

    def add_edge(self, src, dest):
        if dest not in self.adjacency_list[src]:
            self.adjacency_list[src].append(dest)

    def list_outgoing_vertex(self, vertex):
        outgoing_list = self.adjacency_list[vertex]
        for i in range(len(outgoing_list)):
            print(outgoing_list[i])

    def remove_edge(self, src, dest):
        outgoing_vertexes = self.adjacency_list[src]
        if dest in outgoing_vertexes:
            outgoing_vertexes.pop(outgoing_vertexes.index(dest))
            return True

        return False

    def display(self):
        for key in self.adjacency_list:
            print(key+": "+str(self.adjacency_list[key]))

# g = Graph(4)
# g.add_vertex("A", "A")
# g.add_vertex("B", "B")
# g.add_vertex("C", "C")
# g.add_vertex("D", "D")
# g.add_edge("A", "B")
# g.add_edge("A", "C")
# g.add_edge("D", "A")
# g.add_edge("C", "B")
#
# g.display()
# print('')
# g.list_outgoing_vertex("A")