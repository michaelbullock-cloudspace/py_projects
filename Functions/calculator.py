# Name: Michael Bullock
# Class: Python on AWS
# Lab1: sum-calculatory.py

# Description: Write a program that will ask for two numbers (interger or float)
# and calculate the sume of those two numbers
# Display on the screen:  the sum of number 1 and number2 is: sum

# Define a function
def calc_num():
    # This function will calculate the sum of 2 numbers
    
    # Get user input inside the function
    answer1 = int(input("Please provide a whole number:  "))
    answer2 = float(input("Please provide a decimal number:  "))
    
    # Calculate the result
    result = answer1 + answer2
    
    # Return the formatted result
    return f"The sum of {answer1} and {answer2} is: {result}"

# Main
print(calc_num())