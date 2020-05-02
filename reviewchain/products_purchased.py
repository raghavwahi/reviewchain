import products, users, createChain

# Computations on product being purchased
def product_purchased(user_email, product_name):
    # Update the purchase history of the user
    user_details = users.update_purchase_detail(user_email, product_name)

    # Update the sold_count of the product
    product_details = products.sold_count(user_email, product_name)

    # Compute the block chain
    createChain.compute_block_chain(user_details, product_details)

if __name__ == "__main__":
    
    # Purchase the product
    user_email = input("Enter your email id: ")
    product_num = int(input(f"Enter the product number which you want to buy :\n{products.get_product_string()}"))

    product_purchased(user_email, products.get_product_name(product_num-1))