# Name: Michael Bullock
# Lab-cake1: Check for even or odd
# Description: Write a program that will ask a student for their grade in 5 subjects
# Calculate your average grade and print grade from A - E.

math_grade = float(input("Please enter math grade:  "))
english_grade = float(input("Please enter english grade:  "))
spanish_grade = float(input("Please enter spanish grade:  "))
history_grade = float(input("Please enter history grade:  "))
economics_grade = float(input("Please enter economics grade:  "))

grade_average = (math_grade + english_grade + spanish_grade + history_grade + economics_grade) / 5

print(f"Your grade average is:   {grade_average:.2f}")

if grade_average >= 90:
    print("Your grade is A")
elif grade_average >= 80 and grade_average < 90:
    print("Your grade is B")
elif grade_average >= 70 and grade_average < 80:
    print("Your grade is C")
elif grade_average >= 60 and grade_average < 70:
    print("Your grade is D")    
else:
    print("Your grade is E === FAILED :( ")