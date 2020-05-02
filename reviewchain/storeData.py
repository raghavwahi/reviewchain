import products
import users

def add_data():
    products.add_products()
    users.add_users()

# Store the data into database related to products and users
if __name__ == "__main__":
    add_data()