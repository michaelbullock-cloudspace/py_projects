# Name: Michael Bullock
# Class: Python on AWS
# DICTIONARY
# Lab1: Create an English to French translator program that takes a word from the user as an input and
# translates it using a dictionary data type as a vocabulary 
# Please add the translation of 'prune'
# If word is not in the code vocabulary print ([word] is not in my memory)
# The user will select the language they would like to translate to 
# Create a Python function

# Define a function
def translate_to_french():
    # Declare an empty dictionary
    french = {}

    # Add key-value pairs to the dictionary
    french["hammer"] = "marteau"
    french["fruit"] = "le fruit"
    french["book"] = "le livre"
    french["paper"] = "papier"
    french["pencil"] = "crayon"
    french["bathroom"] = "toilettes"
    french["desk"] = "Le bureau"
    french["printer"] = "l'imprimante"
    french["school"] = "école"
    french["church"] = "église"
    french["garden"] = "jardin"
    french["airport"] = "l'aéroport"
    french["spoon"] = "cuillère"
    french["fork"] = "La fourchette"
    french["taxi"] = "le taxi"
    french["subway"] = "métro"
    french["telephone"] = "le téléphone"
    french["doctor"] = "docteur"
    french["teacher"] = "professeur"
    french["pharmacist"] = "pharmacien"
    french["vacation"] = "vacances"
    french["mountain"] = "la montagne"
    french["money"] = "argent"
    french["sun"] = "soleil"
    french["moon"] = "lune"
    french["rain"] = "pluie"
    french["dance"] = "danse"
    french["celebration"] = "célébration"
    french["hello"] = "bonjour"
    french["boat"] = "bateau"
    french["cold"] = "froid"
    french["spicy"] = "épicée"

    # Print the dictionary
    print(french)

    # Get user input
    user_input = input("\nPlease enter an English word you would like translated: ")

    # Declaration for word not in memory
    not_in_memory = f'\nSorry, the word "{user_input.upper()}" is not in memory today, but we can add it in the future if it is a real word.'

    # Result message
    result_msg = f'\nThe French translation of "{user_input.upper()}" is:\t'

    # Get the translation from the dictionary
    french_translation = french.get(user_input)

    # Condition to check for word and print a result
    if french_translation:
        print(result_msg, french_translation)
    else:
        print(not_in_memory)

# Call the function
translate_to_french()
