from pymongo import MongoClient

import uuid

client = MongoClient('mongodb://localhost:27017')
db = client['my-database']
users = db.users

# A function to define the user
def user_details(name, email_id):
    details = {}
    details["name"] = name
    details["email_id"] = email_id
    details["user_id"] = str(uuid.uuid4())
    details["purchase_history"] = []
    details["trust_score"] = 0
    details["review_chain"] = []

    return details

# Users list
users_list = [
    ['Tommy Shelby', 'tomsmith@gmail.com'],
    ['Mike Ross', 'mikeross@gmail.com'],
    ['Saul Goodman', 'saulgoodman@gmail.com'],
    ['Walter White', 'walterwhite@gmail.com'],
    ['Jesse Pinkman', 'jessepinkman@gmail.com'],
    ['Jon Snow', 'jonsnow@gmail.com'],
    ['Alfie Solomons', 'alfiesolomons@gmail.com'],
    ['Ganesh Gaitonde', 'ganeshgaitonde@gmail.com'],
    ['Frank Underwood', 'frankunderwood@gmail.com'],
    ['Michael Scott', 'mmichaelscott@gmail.com']
]

# Adding all the users to the data base
def add_users():
    users.insert_many([user_details(x[0], x[1]) for x in users_list])

# update the purchase details of the user
def update_purchase_detail(email, product):
    user_details = users.find_one({"email_id": email})

    purchase_history = user_details["purchase_history"]
    purchase_history.append(product)

    users.update_one({"email_id": email}, { "$set": { "purchase_history": purchase_history } })