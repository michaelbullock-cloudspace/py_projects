# Name: Michael Bullock
# Class: Python on AWS
# Lab2:  body-weight-convetor.py

# Description: Write a program that will ask for a user body weight in pound
# (lbs) and covert it in kilogram (kg)
# Display on the screen:  your body wight is: weight in lbs, and the 
# equivalent in kgs is: weight kg.  Thank you!

body_weight_lb = float(input("Please provide you body weight in pounds:   "))
body_weight_kg = (body_weight_lb * 0.453592)

print(f"Your body weight is: {body_weight_lb} in lbs, and the equivalent kgs is {body_weight_kg:0,.3f}.  Thank you!")