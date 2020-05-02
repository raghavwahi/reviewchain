import products
import users

# Computations on product being purchased
def product_purchased(user_email, product_name):
    # Update the purchase history of the user
    users.update_purchase_detail(user_email, product_name)

    # Update the sold_count of the product
    products.sold_count(product_name)

    # Compute the block chain

if __name__ == "__main__":
    
    # Purchase the product
    user_email = input("Enter your email id: ")
    product_num = int(input(f"Enter the product number which you want to buy :\n{products.get_product_list()}"))

    product_purchased(user_email, products.get_product_name(product_num-1))