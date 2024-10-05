# Name: Michael Bullock
# Class: Python on AWS
# DICTIONARY
# Lab1: Create an English to French translator program that takes a word from the user as an input and
# translates it using a dictionary data type as a vocabulary 
# Please add the translation of 'prune'
# If word is not in the code vocabulary print ([word] is not in my memory)
# The user will select the language they would like to translate to 

english_word = input("Please enter a English word you would like translated: ")

language_choice = input("What language would you like to translate it to? ")

translation = {
    "French": "elaguer",
    "Spanish": "ciruela pasa",
    "Italian": "fesso"
}

french_translation = translation.get("French")
spanish_translation = translation.get("Spanish")
italian_translation = translation.get("Italian")


if english_word == "prune" and language_choice == "French":
    print(f"The word prune translated in French is:  {french_translation}")
elif english_word == "prune" and language_choice == "Spanish":
    print(f"The word prune translated in Spanish is:  {spanish_translation}")
elif english_word == "prune" and language_choice == "Italian":
    print(f"The word prune translated in Italian is:  {italian_translation}")    
else:
    print(f"The word {english_word} is not in memory")