# Write a program that will:    ## W3 Python String Method 
# Capitalize all first character of each work of msg1

msg1 = "welcome to aws python 101 class:strings"
msg2 = "The instructor here is Claudio"


capitalized_string = msg1.swapcase()

print(capitalized_string)

# Reverse msg2
reverse_msg2 = msg2[::-1]

print(reverse_msg2)


# Write msg1 in lower case

print(msg1.lower())

# Write msg2 in upper case

uppercase_msg2 = msg2.swapcase()

# Find how many "e" characters was used in msg2

x = msg2.count("e")

print(x)

# Replace "python" by "java" in msg1

x = msg1.replace("python", "java")

print(x)

# Create a new message "python is great" using msg1 characters.

# Create a new message "Java is well done" using msg1 characters.