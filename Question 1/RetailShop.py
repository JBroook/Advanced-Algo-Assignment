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

    def display(self):
        print(f"ID: {self.data['id']}")
        print(f"Name: {self.data['name']}")
        print(f"Description: {self.data['description']}")
        print(f"Price: ${self.data['price']:.2f}")
        print(f"Stock: {self.data['stock']} units")
        print(f"Category: {self.data['category']}")


class RetailShop(HashTable):
    def add_product(self, product):
        self.insert(product.data['name'], product)

    def search(self, key):
        return self.get_item(key).val

    def delete_product(self, key):
        hash_key = self.hash(key)
        item_list = self.table[hash_key]
        for i in range(len(item_list)):
            if item_list[i].key==key:
                item_list.pop(i)
                return True
        return False

    def view_all_products(self):
        for key in self.table:
            item_list = self.table[key]
            for item in item_list:
                item.val.display()
                print('')


shop = RetailShop(10)
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

if __name__ =='__main__':
    shop.add_product(p1)
    shop.add_product(p2)
    shop.add_product(p3)

    print('Welcome to your retail shop system.\n')
    while True:
        print('What would you like to do?')
        print('1. Create new product')
        print('2. Search product')
        print('3. View all products')
        print('4. Delete a product')
        print('5. Edit a product')
        action_choice = input('Enter your choice (1/2/3/4/5): ')
        print('')
        match(action_choice):
            case "1":#create new product
                id = input("Product ID: ")
                name = input("Product name: ")
                description = input("Description: ")
                price = float(input("Price (RM): "))
                stock = int(input("Stock: "))
                category = input("Category: ")
    
                new_product = Product(name, description, price, stock, id, category)
                shop.add_product(new_product)
                print(f"Product \'{new_product.data['name']}\' has been successfully added\n")
            case "2":#search products
                product_name = input("Enter product name: ")
                search_result = shop.search(product_name)
                if search_result:
                    search_result.display()
                else:
                    print('Product with that name not found.')
                print('')
            case "3":#view all products
                print('********************\n')
                shop.view_all_products()
                print('********************')
            case "4":#delete a product
                target_name = input('Enter name of the product to be deleted: ')
                if shop.delete_product(target_name):
                    print("Product deleted successfully")
                else:
                    print("Failed to delete: No product was found with this name")
                print('')
            case "5":#edit a product
                target_name = input("Enter name of product to be edited: ")
                search_result = shop.search(target_name)
                if search_result:
                    print("Enter new details, or leave a field blank to skip")
                    id = input(f"Product ID (Original: {search_result.data['id'] }): ")
                    name = input(f"Product name (Original: {search_result.data['name'] }): ")
                    description = input(f"Description (Original: {search_result.data['description'] }): ")

                    price_input = input(f"Price (Original: {search_result.data['price'] }): ")
                    price = float(price_input) if price_input!="" else ""

                    stock_input = input(f"Stock (Original: {search_result.data['stock']}): ")
                    stock = int(stock_input) if stock_input!="" else ""

                    category = input(f"Category (Original: {search_result.data['category'] }): ")

                    new_details = {
                        'id' : id,
                        'name': name,
                        'description': description,
                        'price': price,
                        'stock': stock,
                        'category': category,
                    }

                    key_changed = False
                    for key in new_details:
                        if new_details[key]!="" and new_details[key]!=search_result.data[key]:
                            if key=='name':#change position in hash table
                                key_changed = True
                                shop.delete_product(search_result.data['name'])

                            search_result.data[key] = new_details[key]

                    if key_changed: shop.add_product(search_result)

                    print("Product edited successfully\n")
                else:
                    print("No product with this name.\n")