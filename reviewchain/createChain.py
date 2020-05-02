from pymongo import MongoClient
from hashlib import sha256
import time, pprint

client = MongoClient('mongodb://localhost:27017')
db = client['my-database']
users = db.users

# A Genesis block
def genesis_block(user, product):
    my_str = str(time.time()) + product["id"] + user["user_id"]

    block = {}
    block["email_id"] = user["email_id"]
    block["id"] = user["user_id"]
    block["hash"] = sha256(my_str.encode()).hexdigest()
    block["prev_hash"] = '0'

    return block

# A block
def new_block(user, product, prev_hash ):
    my_str = str(time.time()) + product["id"] + user["user_id"]

    block = {}
    block["email_id"] = user["email_id"]
    block["id"] = user["user_id"]
    block["hash"] = sha256(my_str.encode()).hexdigest()
    block["prev_hash"] = prev_hash

    return block

# If count is zero then genesis_block otherwise normal function to update block chain
def compute_block_chain(user_details, product_details):
    my_block = []
    chain = []

    if product_details["sold_count"] == 1:
        # Create the genesis block
        my_block.append(genesis_block(user_details, product_details))

        # Check if the chain is there or not
        email = product_details["users_purchased"][0]
        new_user = users.find_one({"email_id": email})
        
        curr_chains = new_user["review_chain"]
        if product_details["name"] not in curr_chains.keys(): 
            curr_chains[product_details["name"]] = []
            users.update_one({"email_id": email},{"$set": {"review_chain": curr_chains}})

        # create the chain
        email = product_details["users_purchased"][0]
        new_user = users.find_one({"email_id": email})
        curr_chain = new_user["review_chain"][product_details["name"]]
        curr_chain += my_block

        # Update the ldger
        users.update_one({"email_id": email},{"$set": {"review_chain."+product_details["name"]: curr_chain}})

    else:
        # Get the id of previous user
        prev_user = users.find_one({"email_id": product_details["users_purchased"][-2]})
        prev_hash = prev_user['review_chain'][product_details["name"]][-1]["hash"]

        # Create the next block
        my_block.append(new_block(user_details, product_details, prev_hash))

        # Update the ledger accross all users
        for email in product_details["users_purchased"][:-1]:
            
            user = users.find_one({"email_id": email})
            curr_chain = user["review_chain"][product_details["name"]]
            curr_chain += my_block
            users.update_one({"email_id": email}, {"$set": {"review_chain."+product_details["name"]: curr_chain}})

        first_user = users.find_one({"email_id": product_details["users_purchased"][0]})

        chain = first_user['review_chain'][product_details["name"]]
        
        user = users.find_one({"email_id": product_details["users_purchased"][-1]})
        curr_chain = user["review_chain"]
        curr_chain[product_details["name"]] =  chain
        users.update_one({"email_id": user["email_id"]}, {"$set": {"review_chain": curr_chain}})


def validate_chain():
    pass