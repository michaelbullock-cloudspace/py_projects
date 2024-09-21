# Name: Michael Bullock
# Class: Python on AWS
# Lab3: aws-account-id.py

# Description: Write a program that will display the account id from the arn below:
# arn:aws:iam::123456789012:user/Development/product_1234/*
# Display on the screen:  the aws account id is: account_id.

aws_arn = "aws:iam::123456789012:user/Development/product_1234/*"
arn_account_id = aws_arn[9:21]

print(f"The aws account id is:  {arn_account_id}.")