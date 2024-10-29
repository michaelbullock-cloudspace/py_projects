#Michael Bullock

''' Description: Write a Python program that writes the elements of a list to the file denoted by variable file.
    Each element should be written on a seperate line.
    The file should be new or ts existing content must be replaced by the new content.'''


my_list = [1,2,3,4,5]

#Creates and open file called michael-elements.txt in write mode
with open('michael-elements.txt', 'w') as file:
    for item in my_list:
        file.write(f"{str(item)}\n")     # loop write item from my_list as string and add \n escape 
                                         # character 