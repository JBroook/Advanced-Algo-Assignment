class Graph:
    def __init__(self, size):
        self.matrix = [ [None]*size for _ in range(size)]
        self.size = size
        self.insert_index = 0
        self.vertex_data = {}
        self.vertex_arr = []

    def add_vertex(self, val):
        if self.size-self.insert_index>0:
            self.vertex_data[val] = self.insert_index
            self.vertex_arr.append(val)
            self.insert_index += 1
        else:
            raise ValueError("No space left in the graph")

    def add_edge(self, src, dest):
        self.matrix[self.vertex_data[src]][self.vertex_data[dest]] = 1

    def display(self):
        for i in self.matrix:
            print(i)

    def list_outgoing_vertex(self, vertex):
        outgoing_row = self.matrix[self.vertex_data[vertex]]
        for i in range(len(outgoing_row)):
            if outgoing_row[i]:
                print(self.vertex_arr[i])

g = Graph(4)
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("D", "A")
g.add_edge("C", "B")

g.display()

g.list_outgoing_vertex("A")