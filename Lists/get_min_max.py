# Michael Bullock
# Pythong on AWS
# Description:  Write a Python program that prints the largest and smallest values in a list
# Print the two values on the same line, seperated by a space
# The largest value should appear first and the smallest value should appear second
# You may assume that the list only contains numeric values
# If the list is empty print none.

# Enter the values in the list below in the brackets seperated by comma

# Value Options
# [3,4,5,6]
# [-1-2-3-4]
# [0,0,0,0]

values_list = [3,4,5,6]


if len(values_list) == 0:
    print(values_list)
else:
    print(max(values_list),min(values_list))
