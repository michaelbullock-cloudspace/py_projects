# Define Function
def get_even_numbers(numbers):
    """
    Returns a list of even numbers from the input list.

    Parameters:
    numbers (list): A list of integers.

    Returns:
    list: A list containing only the even numbers from the input list, or an empty list if an error occurs.
    """
    try:
        # Attempt to iterate through the list and filter even numbers
        even_numbers = [num for num in numbers if num % 2 == 0]
        return even_numbers

    except TypeError:
        print("Error: Input must be an iterable list of numbers.")
        return []

    except Exception as error:
        print(f"An unexpected error has occurred: {error}")
        return []
    

numbers = [8, 9, 11, 20,  25,, 32, 101, 100]
#numbers = [9, "tree", 13, 51]

# Call get_even_numbers function
print(get_even_numbers(numbers))  # print even numbers from numbers list [8, 20, 32, 100]

