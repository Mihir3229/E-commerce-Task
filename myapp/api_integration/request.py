import requests
import json

# Base URL for the API
base_url = 'http://127.0.0.1:8000/api/'  # Replace with your actual base URL

def create_new_customer():
    url = base_url + 'customers/'

    # Data for creating a new customer
    new_customer_data = {
        'name': 'Rock',
        'contact_number': '1234567890',  # Replace with customer's contact number
        'email': 'rock@gmail.com'
    }

    headers = {'Content-Type': 'application/json'}

    # Sending a POST request to create a new customer
    response = requests.post(url, data=json.dumps(new_customer_data), headers=headers)

    if response.status_code == 201:
        print("New customer created successfully!")
        print("Customer details:", response.json())  # Print the response data
    else:
        print("Failed to create a new customer.")
        print("Status code:", response.status_code)  # Print the status code for debugging

def create_new_product():
    url = base_url + 'products/'

    # Data for creating a new product
    new_product_data = {
        'name': 'Pencil',
        'weight': 1.5  # Replace with the desired weight
    }

    headers = {'Content-Type': 'application/json'}

    # Sending a POST request to create a new product
    response = requests.post(url, data=json.dumps(new_product_data), headers=headers)

    if response.status_code == 201:
        print("New product created successfully!")
        print("Product details:", response.json())  
    else:
        print("Failed to create a new product.")
        print("Status code:", response.status_code)  

def create_new_order():
    url = base_url + 'orders/'

    # Example payload for order creation
    order_payload = {
        "customer": 5,  
        "order_date": "31/12/2023",
        "address": "California",
        "order_items": [
            {"product": 1, "quantity": 1},
            {"product": 7, "quantity": 2},
            {"product": 4, "quantity": 3}
        ]
    }

    headers = {'Content-Type': 'application/json'}

    # Sending a POST request to create a new order
    response = requests.post(url, data=json.dumps(order_payload), headers=headers)

    if response.status_code == 201:
        print("New order created successfully!")
        print("Order details:", response.json())  # Print the response data
    else:
        print("Failed to create a new order.")
        print("Status code:", response.status_code)  # Print the status code for debugging



# Uncomment the function call below to execute the desired request(s)
create_new_customer()
create_new_product()
create_new_order()




