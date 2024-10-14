'''
Michael Bullock
Python on AWS
Description Write a Python program that works with the list called laura_things using slicing or a loop'''

# Create List called laura_things containning the respective items
laura_things = ["sewing machine", "scissor", "cutting mat", "television"]

# create variable called reversed_list with the value of laura_things list in reverse order
reversed_list = laura_things[::-1]

# Print reversed list
print(reversed_list)  

# Print success confirmation message
print("The list has been successfully reversed!")