import users, products, products_purchased

def purchase_all_products():
    for user in users.get_users_list():
        for product in products.get_product_list():
            products_purchased.product_purchased(user[1], product)

purchase_all_products()