from HashTable import HashTable

class Product:
    def __init__(self, name, description, price, stock, id, category):
        self.data = {
            'name' : name,
            'description' : description,
            'price' : price,
            'stock' : stock,
            'id' : id,
            'category' : category
        }
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.id = id
        self.category = category

    def display(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Price: ${self.price:.2f}")
        print(f"Stock: {self.stock} units")
        print(f"Category: {self.category}")


class RetailShop:
    def __init__(self):
        self.storage = HashTable(10)

    def insert(self, product):
        self.storage.insert(product.name, product)

    def search(self, key, val):
        return self.storage.get_item(key, val)

shop = RetailShop()
p1 = Product(
    name='Bottle',
    description='Glass bottle with plastic cap',
    price=10,
    stock=100,
    id='P101',
    category='appliance'
)
p2 = Product(
    name='Toy',
    description='Soft plushie',
    price=25,
    stock=100,
    id='P102',
    category='toy'
)
p3 = Product(
    name='Stroller',
    description='Black baby stroller',
    price=200,
    stock=100,
    id='P103',
    category='equipment'
)

shop.insert(p1)
shop.insert(p2)
shop.insert(p3)

# shop.search('name','Toy').display()

if __name__ =='__main__':
    print('Welcome to your retail shop system.')
    while True:
        print('What would you like to do?')
        print('1. Create new product')
        print('2. Search product')
        print('3. View all products')
        action_choice = input('Enter your choice (1/2/3): ')
        if action_choice=="1":
            id = input("Product ID: ")
            name = input("Product name: ")
            description = input("Description: ")
            price = float(input("Price (RM): "))
            stock = int(input("Stock: "))
            category = input("Category: ")

            new_product = Product(name, description, price, stock, id, category)
            shop.insert(new_product)
            print(f"Product \'{new_product.name}\' has been successfully added")
        elif action_choice=="2":
            product_name = input("Enter product name: ")
            search_result = shop.search('name', product_name)
            if search_result:
                search_result.display()
            else:
                print('Product with that name not found')