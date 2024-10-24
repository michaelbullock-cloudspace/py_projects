# Define the order dictionary
Order = {
    'tomato': 30,
    'thyme': 4.50,
    'garlic': 7.5,
    'rice': 10,
    'onions': 4,
    'fish': 9.99
}

# Function to add items to the cart and write to a receipt
def add_items_to_cart(order):
    cart = []
    total = 0.0

    # Add items to the cart
    for item, price in order.items():
        cart.append((item, price))
        total += price

    # Write the receipt to a file
    with open('grocery_receipt.txt', 'w') as receipt_file:
        receipt_file.write("Grocery Cart Receipt\n")
        receipt_file.write("-------------------------------\n")
        for item, price in cart:
            receipt_file.write(f"{item}: ${price:.2f}\n")
        receipt_file.write("-------------------------------\n")
        receipt_file.write(f"Total: ${total:.2f}\n")

# Example use
add_items_to_cart(Order)
print("Receipt generated: 'grocery_receipt.txt'")