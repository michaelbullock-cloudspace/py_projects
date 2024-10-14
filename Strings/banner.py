# Michael Bullock
# Course: Python on AWS Couse
# Project: This Python program displays a custom banner using the # symbol and escape metacharacters for 
# formating the banner which include a message.

# Create Variable named horizontal_line that contain string value that adds a sequence of 60 "#" special characters
horizontal_line = "#" * 49

# Create Variable named side_bar that has a value of 1 "#" special character"
side_bar = "#"

# Create variable named open_space that have a metacharacter "\t" that add 10 tab spaces
open_space = "\t" * 6

# Create variable named first_name that store the string value of Michael
first_name = "Michael"

# Create a variable named title that has a string value "WELCOME TO STEET FIGHTER:  "
title = "WELCOME TO STREET FIGHTER:  " 


print(horizontal_line + "\n")
print(side_bar + open_space + side_bar + "\n")
print(side_bar + "\t" + title + first_name + "\t" + side_bar + "\n")
print(side_bar + open_space + side_bar + "\n")
print(horizontal_line)