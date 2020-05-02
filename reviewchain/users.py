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

    return details

# Products list
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

users.insert_many([user_details(x[0], x[1]) for x in users_list])