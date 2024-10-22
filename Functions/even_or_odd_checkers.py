# Name: Michael Bullock
# Lab-cake1: Check for even or odd
# Description: Write a program that will ask user for a number that check
# whether that number is EVEN or ODD
# Please enter a number between 1-100
# Your number user_nmber is even/odd

# Define a function
def num_check():
    user_number = int(input("Please enter a number between 1-100:  "))
    # Conditional Statement
    if (user_number % 2) == 0:
        print("{0} is Even".format(user_number))
    else:
        print("{0} is Odd".format(user_number))


# Call function
num_check()