# Michael Bullock
# Course: Python on AWS Couse
# Lab2: This Python program defines 2 variables with both string and integer values formated using f-string


# Create variable named city with a string value 
city = "Belize City"

# Create variable name temperature with the interger value 29
temperature = 29

# Create variable formated string which has a string value that uses formating used by f-string to display specified variables
formated_string = f"The current temperature in {city} is {temperature:.0f}°C."

# print statement that displays value for the formated_string variable
print(formated_string)