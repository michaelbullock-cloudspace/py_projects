# Name: Michael Bullock
# Class: Python on AWS
# DICTIONARY
# Lab2: Print out the last name of the second employee.  Please search through the dictionary below:

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"oweners":[{"firstName":  "Jack", "lastName": "Petter"},
           {"firstName":  "Jessy", "lastName": "Petter"}]}


# access the variable d to get to the "employees" dictionary which is made up of a list
# once you access the employee dictionary map to index 1 and extract the value of the lastName Key.
print(d['employees'][1]["lastName"])