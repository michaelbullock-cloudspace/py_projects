'''
Michael Bullock
Python on AWS
Description: Write a Python program that uses a list of four U.S. women athletes 
who have competed in the 400 meters at the Olympics.
Your program should do the following:'''

# Create a list of athletes with the following respective names
athletes  = ["Allyson Felix", "Sanya Richards-Ross", "Shaune Miller-Uibo", "Phyllis Francis"]

# Create a for loop to display each athlete's name along with the lap number the completed. 
for index in range(len(athletes)):
    print(f"Lap {index + 1}: {athletes[index]} has completed their lap!")

# Print status message outside of for loop
print("All athletes have completed their laps!")