import json

# Create an empty list to store orders


# Function to save the orders to a JSON file
def save_orders_to_json(orders):
    with open("orders.json", "w") as json_file:
        json.dump(orders, json_file)

# Function to load orders from the JSON file
def load_orders_from_json():
    try:
        with open("orders.json", "r") as json_file:
            orders = json.load(json_file)
            return orders
    except FileNotFoundError:
        # If the file doesn't exist, create an empty JSON fil
        return None

# Function to insert a new order
def insert_order(name, email, phone, address, items):
    orders=load_orders_from_json()
    order = {
        "user_id": len(orders) + 1,
        "name": name,
        "email": email,
        "phone": phone,
        "address": address,
        "products": items
    }
    
    orders.append(order)
    save_orders_to_json(orders)

# Function to fetch an order by user_id
def fetch_order_by_user_name(user_name):
    orders = load_orders_from_json()
    for order in orders:
        if order["name"] == user_name:
            return order
    return None



# if __name__ == "__main__":
#     # Load existing orders from the JSON file
#     load_orders_from_json()

#     # Insert a sample order
#     insert_order("John Doe", "john@example.com", "123-456-7890", "123 Main St, City", "Product A, Product B, Product C")

#     # Fetch an order by user_id
#     user_id_to_fetch = 1  # Replace with the user_id you want to fetch
#     order = fetch_order_by_user_name(user_id_to_fetch)

#     if order:
#         print(f"User ID: {order['user_id']}")
#         print(f"Name: {order['name']}")
#         print(f"Email: {order['email']}")
#         print(f"Phone: {order['phone']}")
#         print(f"Address: {order['address']}")
#         print(f"Items: {order['items']}")
#     else:
#         print(f"No order found for user ID {user_id_to_fetch}")
