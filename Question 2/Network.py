from Graph import Graph
import Person as p
import random as rand

class Network(Graph):
    def list_follows(self, name):
        if name in self.adjacency_list:
            print(f"{name} follows:")
            outgoing_row = self.adjacency_list[name]
            for follower in outgoing_row:
                print(follower)
        else:
            print(f"No user found with the name \'{name}\'")

    def list_followers(self, name):
        if name in self.adjacency_list:
            print(f"{name} is followed by:")
            for user in self.adjacency_list:
                if name in self.adjacency_list[user]:
                    print(user)
        else:
            print(f"No user found with the name \'{name}\'")

    def list_all_users(self):
        count = 1
        for user in self.adjacency_list:
            print(f"{count}. {user}")
            count += 1

    def show_user(self, name):
        user = self.vertex_data[name]
        user.display()

    def get_user(self, name):
        for user in self.vertex_data:
            if user.strip().lower()==name.strip().lower():
                return self.vertex_data[user]
        return None

#cli operations for when we're looking at a specific user
def individual_cli(network, user):
    while True:
        print('*' * 10)
        print('Options for this user:')
        print('1. View all follows')
        print('2. View all followers')
        print('3. Follow new user')
        print('4. Unfollow an existing user')
        print('5. Return')
        action_input = input("Enter your choice (1/2/3/4/5): ")
        match action_input:
            case "1":
                network.list_follows(user.name)
            case "2":
                network.list_followers(user.name)
            case "3":
                new_follow = input("Enter name of user to follow: ")
                new_follow = n.get_user(new_follow)
                if new_follow:
                    n.add_edge(user.name, new_follow.name)
                    print('User followed successfully')
                    break
                else:
                    print('No such user.')
            case "4":
                to_unfollow = input("Enter name of user to unfollow: ")
                to_unfollow = n.get_user(to_unfollow)
                if to_unfollow:
                    if n.remove_edge(user.name, to_unfollow.name):
                        print('User unfollowed successfully')
                    else:
                        print('User was already not followed')
                        break
                else:
                    print('No such user.')
            case "5":
                break

if __name__=="__main__":
    # setting up the network
    n = Network(10)

    for person in p.person_list:
        n.add_vertex(person.name, person)

    connections = [
        ('John Clark', 'Nurul Aini'),
        ('Ahmad Zulkifli', 'Rajesh Kumar'),
        ('Rajesh Kumar', 'David Lim'),
        ('Nurul Aini', 'Rajesh Kumar'),
        ('Emily Tan', 'John Clark'),
        ('John Clark', 'Ahmad Zulkifli'),
        ('Ahmad Zulkifli', 'David Lim'),
        ('Sarah Wong', 'Rajesh Kumar'),
        ('Nurul Aini', 'Chong Mei Ling'),
        ('David Lim', 'Chong Mei Ling'),
        ('Rajesh Kumar', 'Sarah Wong'),
        ('Ahmad Zulkifli', 'Chong Mei Ling'),
        ('Emily Tan', 'Benjamin Lee'),
        ('John Clark', 'Ahmad Zulkifli'),
        ('Sarah Wong', 'Benjamin Lee'),
        ('Chong Mei Ling', 'John Clark'),
        ('Nurul Aini', 'John Clark'),
        ('Rajesh Kumar', 'Sarah Wong'),
        ('Emily Tan', 'Benjamin Lee'),
        ('Chong Mei Ling', 'Emily Tan'),
        ('Sarah Wong', 'Benjamin Lee'),
        ('Emily Tan', 'Rajesh Kumar'),
        ('Sarah Wong', 'John Clark'),
        ('Sarah Wong', 'John Clark'),
        ('Nurul Aini', 'Ahmad Zulkifli'),
        ('Chong Mei Ling', 'Rajesh Kumar')
    ]

    for connection in connections:
        n.add_edge(connection[0],connection[1])

    print('Welcome to CLIgram')
    while True:
        print('')
        print('What would you like to do?')
        print('1. View all users')
        print('2. View specific user')
        print('3. Add new user')
        action_input = input("Enter your choice (1/2/3): ")
        match action_input:
            case "1":
                n.list_all_users()
                print('')
            case "2":
                username = input("Enter user's name: ")
                user = n.get_user(username)
                if user:
                    if user.public:
                        user.display()
                        individual_cli(n, user)
                    else:
                        print('This user\'s profile is private.')
                else:
                    print('This user doesn\'t exist')
            case "3":
                print("Enter new user details")
                name = input("User's name: ")
                gender = input("Gender (Male/Female): ")
                address = input("Address: ")
                public = input("Public profile (yes/no): ")
                biography = input("Biography: ")