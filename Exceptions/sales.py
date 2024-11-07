# Define the order dictionary
Order = {
    'tomatoes': 30,
    'thyme': 4.50,
    'garlic': 7.5,
    'rice': 10,
    'onions': 4,
    'fish': 9.99
}

def add_items_to_cart(order):
    """
    Adds items to a cart and generates a receipt file.

    Parameters:
    order dictionary: A dictionary with items as keys and prices as values.

    Writes:
    A file named 'grocery_receipt.txt' containing the items, their prices, and the total.

    Raises:
    TypeError: If the order is not a dictionary or contains non-numeric prices.
    ValueError: If the order is empty or contains invalid data types.
    Exception: For any other unexpected errors.
    """
    cart = []
    total = 0.0

    try:
        # Verify that `order` has content to process
        if not order:
            raise ValueError("The order is empty.")

        # Process each item in the order
        for item, price in order.items():
            if not isinstance(price, (int, float)):
                raise TypeError(f"The price for '{item}' must be a number.")
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
        print("Receipt generated: 'grocery_receipt.txt'")

    except TypeError as type_error:
        print(f"TypeError: {type_error}")    # Raise if any price is not a numerical value
    except ValueError as value_error:
        print(f"ValueError: {value_error}")   # Raised if the order is empty or contains an invalid structure
    except Exception as error:
        print(f"An unexpected error occurred: {error}")  # Catches any unexpected error that might occur.

# Example use
add_items_to_cart(Order)
