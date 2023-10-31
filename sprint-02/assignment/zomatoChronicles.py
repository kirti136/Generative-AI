import json
from prettytable import PrettyTable


# Load menu data from menu.json
with open('menu.json', 'r') as menu_file:
    menu = json.load(menu_file)

# Load orders data from orders.json
with open('orders.json', 'r') as orders_file:
    orders = json.load(orders_file)

# Save menu data to menu.json
with open('menu.json', 'w') as menu_file:
    json.dump(menu, menu_file, indent=4)

# Save orders data to orders.json
with open('orders.json', 'w') as orders_file:
    json.dump(orders, orders_file, indent=4)

# Define roles and initial user data
roles = {
    "user": {"username": "user", "password": "userpass"},
    "staff": {"username": "staff", "password": "staffpass"}
}

# Initialize the user role as "guest" (not authenticated)
user_role = "guest"

# Function to authenticate a user
def authenticate_user():
    global user_role
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in roles and roles[username]["password"] == password:
        user_role = username
        print(f"Welcome, {username}!")
    else:
        print("Invalid credentials. You are logged in as a guest.")

# Define a function to view the menu.
def view_menu():
    table = PrettyTable()
    table.field_names = ["ID", "NAME", "PRICE"]
    
    for dish in menu:
        if dish["available"]:
            table.add_row([dish['_id'], dish['name'], f"${dish['price']}"])

    print("Menu:")
    print(table)

# Define a function to place an order.
def place_order():
    customer_name = input("Enter your name: ")
    order_items = []

    while True:
        print("\nMenu:")
        for dish in menu:
            if dish["available"]:
                print(f"{dish['_id']}. {dish['name']} - ${dish['price']}")

        dish_id = input("Enter the ID of the dish you want to order (0 to finish): ")

        if dish_id == '0':
            break

        dish_id = int(dish_id)

        # Find the selected dish by its '_id' in the menu list
        selected_dish = next((dish for dish in menu if dish['_id'] == dish_id), None)

        if selected_dish and selected_dish["available"]:
            quantity = int(input("Enter the quantity: "))
            order_items.append({"dish_id": dish_id, "quantity": quantity})
        else:
            print("Invalid dish ID or dish is not available.")

    if order_items:
        order_id = len(orders) + 1
        orders.append({
            "order_id": order_id,
            "customer_name": customer_name,
            "items": order_items,
            "status": "received"
        })
        print(f"Order for {customer_name} has been received with order ID {order_id}.")

        # Save the updated orders to "orders.json"
        with open('orders.json', 'w') as orders_file:
            json.dump(orders, orders_file, indent=4)
    else:
        print("No items in the order.")

# Define a function to add a new dish to the menu.
def add_dish():
    dish_id = len(menu) + 1
    dish_name = input("Enter the name of the new dish: ")
    dish_price = float(input("Enter the price of the new dish: "))
    dish_available = input("Enter the availability of the new dish (True or False): ").strip().lower()
    if dish_available == 'true':
        dish_available = True
    elif dish_available == 'false':
        dish_available = False
    else:
        print("Invalid input for availability. Please use 'True' or 'False'.")
        return

    menu.append({
            "_id": dish_id,
            "name": dish_name,
            "price": dish_price,
            "available": dish_available
    })
    print(f"{dish_name} has been added to the menu.")

    # Save the updated menu data to "menu.json"
    with open('menu.json', 'w') as menu_file:
        json.dump(menu, menu_file, indent=4)

# Define a function to remove a dish from the menu.
def remove_dish():
    print("Menu:")
    for dish in menu:
        print(f"{dish['_id']}. {dish['name']}")

    dish_id = int(input("Enter the ID of the dish to remove: "))

    # Find the index of the dish with the given '_id'
    dish_index = next((index for index, dish in enumerate(menu) if dish['_id'] == dish_id), None)

    if dish_index is not None:
        dish_name = menu[dish_index]['name']
        del menu[dish_index]  # Remove the dish from the menu list
        print(f"{dish_name} has been removed from the menu.")

        # Save the updated menu data to "menu.json"
        with open('menu.json', 'w') as menu_file:
            json.dump(menu, menu_file, indent=4)
    else:
        print("Invalid dish ID. No dish with that ID found.")

# Define a function to update the availability of a dish.
def update_availability():
    print("Menu:")
    for dish in menu:
        print(f"{dish['_id']}. {dish['name']} (Available: {dish['available']})")

    dish_id = int(input("Enter the ID of the dish to update: "))

    # Find the dish with the given '_id' in the menu
    selected_dish = next((dish for dish in menu if dish['_id'] == dish_id), None)

    if selected_dish:
        selected_dish['available'] = not selected_dish['available']  # Toggle the availability
        availability = "available" if selected_dish['available'] else "unavailable"
        print(f"{selected_dish['name']} is now {availability}.")

        # Save the updated menu data to "menu.json"
        with open('menu.json', 'w') as menu_file:
            json.dump(menu, menu_file, indent=4)
    else:
        print("Invalid dish ID. No dish with that ID found.")

# Define a function to take a new order.
def take_order():
    customer_name = input("Enter customer name: ")
    print("Menu:")
    for dish in menu:
        if dish["available"]:
            print(f"{dish['_id']}. {dish['name']} - ${dish['price']}")

    order_items = []
    while True:
        dish_id = input("Enter the ID of the dish to order (0 to finish): ")
        if dish_id == '0':
            break

        dish_id = int(dish_id)

        # Find the selected dish by its '_id' in the menu list
        selected_dish = next((dish for dish in menu if dish['_id'] == dish_id), None)

        if selected_dish and selected_dish["available"]:
            quantity = int(input("Enter the quantity: "))
            order_items.append({"dish_id": dish_id, "quantity": quantity})
        else:
            print("Invalid dish ID or dish is not available.")

    if order_items:
        order_id = len(orders) + 1
        orders.append({
            "order_id": order_id,
            "customer_name": customer_name,
            "items": order_items,
            "status": "received"
        })
        print(f"Order for {customer_name} has been received with order ID {order_id}.")

        # Save the updated orders to "orders.json"
        with open('orders.json', 'w') as orders_file:
            json.dump(orders, orders_file, indent=4)
    else:
        print("No items in the order.")

# Define a function to update the status of an order.
def update_order_status():
    order_id = int(input("Enter order ID to update: "))
    for order in orders:
        if order["order_id"] == order_id:
            print("Current Status:", order["status"])
            new_status = input("Enter the new status (preparing, ready for pickup, delivered): ")
            order["status"] = new_status
            print(f"Order {order_id} status has been updated to {new_status}.")

            # Save the updated orders to "orders.json"
            with open('orders.json', 'w') as orders_file:
                json.dump(orders, orders_file, indent=4)
            break
    else:
        print("Invalid order ID.")


# Define a function to review orders with optional status filter.
def review_orders():
    while True:
        filter_menu = PrettyTable()
        filter_menu.field_names = ["Option", "Filter Description"]
        filter_menu.add_row(["1", "All Orders"])
        filter_menu.add_row(["2", "Ready for Pickup"])
        filter_menu.add_row(["3", "Preparing"])
        filter_menu.add_row(["4", "Delivered"])
        filter_menu.add_row(["5", "Exit"])
        print("Filter Options:")
        print(filter_menu)

        filter_choice = input("Enter your filter choice (1-5): ")

        if filter_choice == '1':
            status_filter = None
        elif filter_choice == '2':
            status_filter = "ready for pickup"
        elif filter_choice == '3':
            status_filter = "preparing"
        elif filter_choice == '4':
            status_filter = "delivered"
        elif filter_choice == '5':
            break
        else:
            print("Invalid choice. Please choose a valid option (1-5).")
            continue

        order_table = PrettyTable()
        order_table.field_names = ["Order ID", "Customer Name", "Status", "Items"]

        for order in orders:
            customer_name = order["customer_name"]
            order_id = order["order_id"]
            status = order["status"]
            items = []

            if isinstance(order["items"], list):
                for item in order["items"]:
                    dish = next((dish for dish in menu if dish["_id"] == item["dish_id"]), None)
                    if dish:
                        items.append(f"{dish['name']} x{item['quantity']}")
            elif isinstance(order["items"], dict):
                for dish_id, quantity in order["items"].items():
                    dish = next((dish for dish in menu if dish["_id"] == int(dish_id)), None)
                    if dish:
                        items.append(f"{dish['name']} x{quantity}")

            items_str = ", ".join(items)

            # Apply status filter
            if status_filter is None or status == status_filter:
                order_table.add_row([order_id, customer_name, status, items_str])

        print("Filtered Orders:")
        print(order_table)

# Function to calculate the total price of an order
def calculate_total_price(order, menu):
    total_price = 0
    items = order["items"]
    
    if isinstance(items, list):
        for item in items:
            dish = next((dish for dish in menu if dish["_id"] == item["dish_id"]), None)
            if dish:
                total_price += dish["price"] * item["quantity"]
    elif isinstance(items, dict):
        for dish_id, quantity in items.items():
            dish = next((dish for dish in menu if dish["_id"] == int(dish_id)), None)
            if dish:
                total_price += dish["price"] * quantity
    
    return total_price

# Function to generate bills for delivered orders
def generate_bills(orders, menu):
    total_billing_cost = 0
    
    for order in orders:
        if order["status"] == "delivered":
            total_price = calculate_total_price(order, menu)
            total_billing_cost += total_price

    # Save the billing cost to "bills.json"
    with open('bills.json', 'w') as bills_file:
        json.dump({"total_billing_cost": total_billing_cost}, bills_file, indent=4)

    print(f"Total billing cost for delivered orders: ${total_billing_cost}")
    print("Billing details saved in bills.json")

# Main Program 
while True:
    if user_role == "guest":
        guest_menu = PrettyTable()
        guest_menu.field_names = ["Option", "Description"]
        guest_menu.add_row(["1", "Login"])
        guest_menu.add_row(["2", "Exit"])

        print("\nZesty Zomato Management System (Guest Mode):")
        print(guest_menu)

        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            authenticate_user()
        elif choice == '2':
            print("Thank you for using Zesty Zomato Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option (1 or 2).")
    # USER
    elif user_role == "user":
        user_menu = PrettyTable()
        user_menu.field_names = ["Option", "Description"]
        user_menu.add_row(["1", "View Menu"])
        user_menu.add_row(["2", "Place an Order"])
        user_menu.add_row(["3", "Exit"])

        print("\nZesty Zomato Management System (User):")
        print(user_menu)

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            view_menu()
        elif choice == '2':
            place_order()
        elif choice == '3':
            user_role = "guest"
        else:
            print("Invalid choice. Please choose a valid option (1-3).")
    # STAFF
    elif user_role == "staff":
        staff_menu = PrettyTable()
        staff_menu.field_names = ["Option", "Description"]
        staff_menu.add_row(["1", "Add a new dish to the menu"])
        staff_menu.add_row(["2", "Remove a dish from the menu"])
        staff_menu.add_row(["3", "Update dish availability"])
        staff_menu.add_row(["4", "Take a new order"])
        staff_menu.add_row(["5", "Update order status"])
        staff_menu.add_row(["6", "Review all orders"])
        staff_menu.add_row(["7", "Generate Bills"])
        staff_menu.add_row(["8", "Exit"])

        print("\nZesty Zomato Management System:")
        print(staff_menu)

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            add_dish()
        elif choice == '2':
            remove_dish()
        elif choice == '3':
            update_availability()
        elif choice == '4':
            take_order()
        elif choice == '5':
            update_order_status()
        elif choice == '6':
            review_orders()
        elif choice == '7':
            generate_bills(orders, menu)
        elif choice == '8':
            print("Thank you for using Zesty Zomato Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option (1-8).")