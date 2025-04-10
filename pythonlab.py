# Write a program that will:
## W3 Python String Method 
# Capitalize all first character of each word of msg1

msg1 = "welcome to aws python 101 class:strings"
msg2 = "The instructor here is Claudio"

# Add msg3
msg3 = "python script modified by Patrick TCHAMAGNIE"

# Capitalize all first character of each word in msg1
capitalized_string = msg1.title()  # Changed to title() to capitalize first letters of each word

print(capitalized_string)

# Reverse msg2
reverse_msg2 = msg2[::-1]
print(reverse_msg2)

# Write msg1 in lower case
print(msg1.lower())

# Write msg2 in upper case
uppercase_msg2 = msg2.upper()  # Changed to upper() to convert to uppercase
print(uppercase_msg2)

# Find how many "e" characters were used in msg2
x = msg2.count("e")
print(x)

# Replace "python" with "java" in msg1
x = msg1.replace("python", "java")
print(x)

# Create a new message "python is great" using msg1 characters.
new_msg1 = "".join([char for char in msg1 if char in "python is great"])
print(new_msg1)

# Create a new message "Java is well done" using msg1 characters.
new_msg2 = "".join([char for char in msg1 if char in "Java is well done"])
print(new_msg2)

# Print msg3
print(msg3)