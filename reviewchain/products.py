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
    details["sold_count"] = 0

    return details

# Products list
products_list = [
    'Acer Swift 3 (Laptop)',
    'Whirlpool Refrigrator X4323',
    'Oneplus 8 pro 256 gb',
    'JBL T160BT in ear headphones'
]

# Adding all the products to the data base
def add_products():
    products.insert_many([product_details(x) for x in products_list])

# Fetches a products information based on the name
def product_info(name):
    return products.find_one({"name": name})

# Get the product list
def get_product_list():
    return ''.join([x +': product(' + str(products_list.index(x) + 1) + ') \n' for x in products_list])

# Get product name
def get_product_name(number):
    return products_list[number]

# Update the sold count of the user
def sold_count(name):
    product_details = products.find_one({"name": name})
    product_count = product_details["sold_count"]

    products.update_one({"name":name}, { "$set": {"sold_count": product_count + 1}})