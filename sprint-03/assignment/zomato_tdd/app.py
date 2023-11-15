from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data for menu and orders (for demonstration purposes)
menu = [
    {"dish_id": 1, "name": "Pizza", "price": 12.99, "available": True},
    {"dish_id": 2, "name": "Burger", "price": 8.99, "available": True},
    # Add more dishes here
]

orders = []

# Menu Routes
@app.route('/menu', methods=['GET'])
def get_menu():
    return jsonify({"menu": menu})

@app.route('/menu/add', methods=['POST'])
def add_dish():
    data = request.get_json()
    new_dish = {
        "dish_id": data.get("dish_id"),
        "name": data.get("name"),
        "price": data.get("price"),
        "available": data.get("available")
    }
    menu.append(new_dish)
    return jsonify({"message": "Dish added successfully"})

@app.route('/menu/remove/<int:dish_id>', methods=['DELETE'])
def remove_dish(dish_id):
    global menu
    menu = [dish for dish in menu if dish["dish_id"] != dish_id]
    return jsonify({"message": "Dish removed successfully"})

@app.route('/menu/update/<int:dish_id>', methods=['PUT'])
def update_availability(dish_id):
    data = request.get_json()
    available = data.get("available")

    dish = next((dish for dish in menu if dish["dish_id"] == dish_id), None)
    if dish:
        dish["available"] = available
        return jsonify({"message": f"Availability for Dish ID {dish_id} updated successfully"})
    else:
        return jsonify({"message": f"Dish ID {dish_id} not found in the menu"})

# Order Routes
@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify({"orders": orders})

@app.route('/orders/place', methods=['POST'])
def place_order():
    data = request.get_json()
    customer_name = data.get("customer_name")
    order_items = data.get("order_items")

    # Check if all dishes in the order are available in the menu
    available_dish_ids = [dish["dish_id"] for dish in menu if dish["available"]]
    unavailable_dishes = [item for item in order_items if item not in available_dish_ids]

    if unavailable_dishes:
        return jsonify({"message": f"Dish IDs {', '.join(map(str, unavailable_dishes))} not available in the menu"})

    # Process the order
    order_id = len(orders) + 1
    order = {
        "order_id": order_id,
        "customer_name": customer_name,
        "order_items": order_items,
        "status": "received"
    }
    orders.append(order)
    return jsonify({"message": f"Order placed successfully with ID {order_id}"})

@app.route('/orders/update/<int:order_id>', methods=['PUT'])
def update_order_status(order_id):
    data = request.get_json()
    new_status = data.get("status")

    order = next((order for order in orders if order["order_id"] == order_id), None)
    if order:
        order["status"] = new_status
        return jsonify({"message": f"Order ID {order_id} status updated successfully"})
    else:
        return jsonify({"message": f"Order ID {order_id} not found"})

if __name__ == '__main__':
    app.run(debug=True)
