from Graph import Graph
import Person as p
import random as rand

class Network(Graph):
    def get_index_by_name(self, name):
        for i in range(len(self.vertex_data)):
            if self.vertex_data[i].name.lower().strip()==name.lower().strip():
                return i

        return -1

    #override
    def add_edge(self, src_name, dest_name):
        i_src = self.get_index_by_name(src_name)
        i_dest = self.get_index_by_name(dest_name)
        self.matrix[i_src][i_dest] = 1

    def list_follows(self, name):
        index = self.get_index_by_name(name)
        print(f"{self.vertex_data[index].name} follows:")
        outgoing_row = self.matrix[index]
        for i in range(self.size):
            if outgoing_row[i]:
                print(self.vertex_data[i].name)

    def list_followers(self, name):
        index = self.get_index_by_name(name)
        print(f"{self.vertex_data[index].name} is followed by:")
        for i in range(self.size):
            if self.matrix[i][index]:
                print(self.vertex_data[i].name)

    def list_all_users(self):
        for person in self.vertex_data:
            print(person.name)

    def show_user(self, name):
        index = self.get_index_by_name(name)
        self.vertex_data[index].display()

n = Network(10)

for person in p.person_list:
    n.add_vertex(person)

#create random following
for _ in range(60):
    name1 = p.person_list[rand.randint(0,9)].name
    name2 = p.person_list[rand.randint(0, 9)].name
    if name1!=name2:
        n.add_edge(name1, name2)

n.list_all_users()
n.list_follows("Sarah Wong")
n.list_followers("Sarah Wong")
n.show_user("Sarah Wong")