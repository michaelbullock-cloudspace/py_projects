# Name: Michael Bullock
# Class: Python on AWS
# Lab1: sum-calculatory.py

# Description: Write a program that will ask for two numbers (interger or float)
# and calculate the sume of those two numbers
# Display on the screen:  the sume of number 1 and number2 is: sum

answer1 = int(input("Please provide a whole number:  "))
answer2 = float(input("Please provide a decimal number:  "))
result = answer1 + answer2

print(f"The sum of {answer1} and {answer2} is:  {result}")