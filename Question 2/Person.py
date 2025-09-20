from Graph import Graph

class Person:
    def __init__(self, name, gender, address, public, biography):
        self.name = name
        self.gender = gender
        self.address = address
        self.public = public
        self.biography = biography

    def display(self):
        print(f"Name: {self.name}")
        print(f"Gender: {self.gender}")
        print(f"Address: {self.address}")
        print(f"Public: {self.public}")
        print(f"Biography: {self.biography}")

p1 = Person(
    name='John Clark',
    gender='Male',
    address='10A Jalan Sok Lye Hin, Georgetown, 11800, Penang',
    public=True,
    biography='Mechanical Engineer at Boston Dynamics. Father of two'
)

p2 = Person(
    name='Emily Tan',
    gender='Female',
    address='45 Jalan Cempaka 3, Taman Cempaka, 68000, Ampang',
    public=True,
    biography='Freelance UX Designer. Loves hiking and painting.'
)

p3 = Person(
    name='David Lim',
    gender='Male',
    address='22 Jalan Setia 4/3, Setia Alam, 40170, Shah Alam',
    public=False,
    biography='Data Scientist with a background in epidemiology.'
)

p4 = Person(
    name='Sarah Wong',
    gender='Female',
    address='18 Jalan Delima, Taman Desa, 58100, Kuala Lumpur',
    public=True,
    biography='Teacher and writer. Advocates for early childhood education.'
)

p5 = Person(
    name='Ahmad Zulkifli',
    gender='Male',
    address='5 Lorong Merdeka, Kampung Baru, 50300, Kuala Lumpur',
    public=True,
    biography='Civil Engineer working on green infrastructure projects.'
)

p6 = Person(
    name='Nurul Aini',
    gender='Female',
    address='11A Jalan Seri Impian 2, Taman Impian Emas, 81300, Skudai',
    public=False,
    biography='Dentist with a passion for volunteer work in rural areas.'
)

p7 = Person(
    name='Benjamin Lee',
    gender='Male',
    address='8 Jalan Pelangi 9, Taman Pelangi, 80200, Johor Bahru',
    public=True,
    biography='Marketing executive at a tech startup. Avid cyclist.'
)

p8 = Person(
    name='Chong Mei Ling',
    gender='Female',
    address='33 Jalan Bukit Indah 5/2, Taman Bukit Indah, 81200, Johor Bahru',
    public=True,
    biography='Interior designer who loves modern minimalist aesthetics.'
)

p9 = Person(
    name='Rajesh Kumar',
    gender='Male',
    address='27 Jalan SP 3/4, Taman Subang Perdana, 40150, Subang',
    public=False,
    biography='IT consultant and part-time coding tutor.'
)

p10 = Person(
    name='Lisa Ong',
    gender='Female',
    address='9 Jalan Alor, Bukit Bintang, 50200, Kuala Lumpur',
    public=True,
    biography='Pastry chef at a boutique bakery. Shares recipes online.'
)

person_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
