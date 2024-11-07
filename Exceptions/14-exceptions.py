# Define function
def divide_by(a , b):
    try: # Attempt
        total = a / b
        return total
    except ZeroDivisionError as error:
        return "Sorry you cannot divide a {a} by Zero! becaus"
        #raise error   
    return total    

# MAIN
num1 = float(input('Abeg give me a number:  '))
num2 = float(input('Abeg give another me a number: '))

# calling the function and store the result in division_result
division_result = divide_by(num1, num2)

print(f"{num1} divided by {num2} is {division_result}")
