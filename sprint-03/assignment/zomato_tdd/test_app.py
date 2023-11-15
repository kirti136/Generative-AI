import unittest
import json
from app import app


class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_menu(self):
        response = self.app.get('/menu')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('menu' in json.loads(response.get_data(as_text=True)))

    def test_add_dish(self):
        new_dish = {
            "dish_id": 3,
            "name": "Pasta",
            "price": 10.99,
            "available": True
        }
        response = self.app.post('/menu/add', json=new_dish)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.get_data(as_text=True))[
                         'message'], "Dish added successfully")

    def test_remove_dish(self):
        dish_id = 1  # Assuming dish_id 1 exists in the menu
        response = self.app.delete(f'/menu/remove/{dish_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.get_data(as_text=True))[
                         'message'], "Dish removed successfully")

    def test_update_availability(self):
        dish_id = 2  # Assuming dish_id 2 exists in the menu
        updated_availability = {
            "available": False
        }
        response = self.app.put(
            f'/menu/update/{dish_id}', json=updated_availability)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.get_data(as_text=True))[
                         'message'], f"Availability for Dish ID {dish_id} updated successfully")

    def test_get_orders(self):
        response = self.app.get('/orders')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('orders' in json.loads(
            response.get_data(as_text=True)))

    def test_place_order(self):
        new_order = {
            "customer_name": "John Doe",
            "order_items": [1, 2]
        }
        response = self.app.post('/orders/place', json=new_order)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.get_data(as_text=True))[
                         'message'], "Order placed successfully")

    def test_update_order_status(self):
        order_id = 1
        updated_status = {
            "status": "preparing"
        }
        response = self.app.put(
            f'/orders/update/{order_id}', json=updated_status)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.get_data(as_text=True))[
                         'message'], f"Order ID {order_id} status updated successfully")

if __name__ == '__main__':
    unittest.main()
