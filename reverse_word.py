# Name: Michael Bullock
# Class: Python on AWS
# Lab4: reversing a word (FUN)

# Description: Write a program that will ask for a word and reverse the word.
# Display on the screen: your word is: word, and the reverse is:
# reverse_word
# Leverage methods: split, join and reversed

word = input("Please enter a word:  ")
reverse_word = word[::-1]

print(f"Your word is:  {word}, and the reverse is: {reverse_word}.")
