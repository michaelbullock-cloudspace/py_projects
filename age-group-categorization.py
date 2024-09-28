# Name: Michael Bullock
# Class: Python on AWS
# Lab3: aws-account-id.py
# Prompt the user to enter their age as an interger and display the appropriate life stage.
# If the user enters a negative number or a non-realistic number (e.g., more than 150).
# display an "Invalid age" message.

user_age = int(input("Please enter you current age: "))

print(f"You entered : {user_age}")

if user_age == 0 or user_age == 1:
    print("Your current life stage is Infant")
elif user_age == 2 or user_age == 3:
    print("Your current life stage is Toddler") 
elif user_age >= 4 and  user_age <= 12:
    print("Your current life stage is Child")  
elif user_age >= 13 and  user_age <= 19:
    print("Your current life stage is Teenager") 
elif user_age >= 20 and  user_age <= 64:
    print("Your current life stage is Adult")
elif user_age >= 65 and  user_age <= 150:
    print("Your current life stage is Senior")
else:
    print("Invalid age")