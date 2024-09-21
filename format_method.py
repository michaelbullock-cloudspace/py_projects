# Michael Bullock
# Course: Python on AWS Couse
# Lab1: This Python program defines 3 variables with both string and integer values utilized by a format() method



# Create variable named first_name that has string value Michael
first_name = "Michael"

# Create variable named age that has a integer value 42 
age = 42 

# Create variable named favorite_color that has string value black
favorite_color = "black"

# Create variable named sentence that has a string value which use the format() Method that displays the value of variables 
# as specified within the format() Method
sentence = "Hello, my name is {}. I am {} years old, and my favorite color is {}.".format(first_name, age, favorite_color)

# print statement that displays value for the sentence variable
print(sentence)