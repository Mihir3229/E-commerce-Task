ef create_new_product():
    url = base_url + 'products/'

    # Data for creating a new product
    new_product_data = {
        'name': 'New Name',
        'weight': 1.5  # Replace with the desired weight
    }

    headers = {'Content-Type': 'application/json'}

    # Sending a POST request to create a new product
    response = requests.post(url, data=json.dumps(new_product_data), headers=headers)

    if response.status_code == 201:
        print("New product created successfully!")
        print("Product details:", response.json())  # Print the response data
    else:
        print("Failed to create a new product.")
        print("Status code:", response.status_code)  # Print the status code for debugging

def create_new_order():
   