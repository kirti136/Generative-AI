# Initialize an empty list to store the snack inventory.
snack_inventory = []
# Initialize an empty list to store sales records.
sales_records = []

# Handle User's Choice
def menu():
    while True:
        print("\nChoose option for operation:")
        print("1 - Add a new snack to the inventory")
        print("2 - Remove an existing snack from the inventory")
        print("3 - Update the availability of a specific snack")
        print("4 - Sell a particular snack")
        print("5 - Display all available snacks")
        print("6 - Display all records")
        print("7 - Exit")

        choice = input("Enter your choice: ")

        if choice == '1':  # Add
            add_snack()
        elif choice == '2':  # Remove
            snack_id = input("Enter Snack ID to remove: ")
            remove_snack(snack_id)
        elif choice == '3':  # Update Snack Availability
            snack_id = input("Enter Snack ID to update availability: ")
            is_available = input("Is the snack available now? (yes/no): ")
            update_snack_availability(snack_id, is_available.lower() == "yes")
        elif choice == '4':  # Sale Records
            sale_id = input("Enter Snack ID sold: ")
            record_sale(sale_id)
        elif choice == '5':  # Print all Snacks
            print_snack_inventory()
        elif choice == '6':  # Print all Sales Records
            print_sales_records()
        elif choice == '7':  # Exit
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

# Print Data
def print_snack_inventory():
    if not snack_inventory:
        print("Inventory is empty.")
    else:
        print("Snack Inventory:")
        for snack in snack_inventory:
            print(
                f"ID: {snack['ID']}, Name: {snack['Name']}, Price: {snack['Price']}, Available: {'Yes' if snack['Available'] else 'No'}")

# Print Sales
def print_sales_records():
    if not sales_records:
        print("No sales have been recorded.")
    else:
        print("Sales Records:")
        for sale in sales_records:
            print(
                f"ID: {sale['ID']}, Name: {sale['Name']}, Price: {sale['Price']}, Available: {'Yes' if sale['Available'] else 'No'}")

# Add Snack
def add_snack():
    snack_id = input("Enter Snack ID: ")
    snack_name = input("Enter Snack Name: ")
    snack_price = float(input("Enter Snack Price: "))
    snack_available = input("Is the snack available? (yes/no): ")

    snack = {
        "ID": snack_id,
        "Name": snack_name,
        "Price": snack_price,
        "Available": snack_available.lower() == "yes"
    }

    snack_inventory.append(snack)
    print("Snack added to inventory.")

# Remove Snack
def remove_snack(snack_id):
    for snack in snack_inventory:
        if snack["ID"] == snack_id:
            snack_inventory.remove(snack)
            print(f"Snack with ID {snack_id} removed from inventory.")
            return
    print(f"Snack with ID {snack_id} not found in inventory.")

# Update Snack Availability
def update_snack_availability(snack_id, is_available):
    for snack in snack_inventory:
        if snack["ID"] == snack_id:
            snack["Available"] = is_available
            print(
                f"Snack with ID {snack_id} availability updated to {is_available}.")
            return
    print(f"Snack with ID {snack_id} not found in inventory.")

# Record Sales
def record_sale(snack_id):
    for snack in snack_inventory:
        if snack["ID"] == snack_id:
            if snack["Available"]:
                sales_records.append(snack)
                print(f"Sale recorded for snack with ID {snack_id}.")
            else:
                print(f"Snack with ID {snack_id} is not available for sale.")
            return
    print(f"Snack with ID {snack_id} not found in inventory.")


# Test the menu function
menu()