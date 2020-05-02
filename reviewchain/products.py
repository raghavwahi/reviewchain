from pymongo import MongoClient
import uuid

client = MongoClient('mongodb://localhost:27017')
db = client['my-database']
products = db.products

# A function to define the product
def product_details(name):
    details = {}
    details["name"] = name
    details["id"] = str(uuid.uuid4())
    details["reviews"] = []
    details["rating"] = 0

    return details

# Products list
products_list = [
    'Acer Swift 3 (Laptop)',
    'Whirlpool Refrigrator X4323',
    'Oneplus 8 pro 256 gb',
    'JBL T160BT in ear headphones'
]

# Adding all the products to the data base
products.insert_many([product_details(x) for x in products_list])