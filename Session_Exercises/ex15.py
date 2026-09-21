# the below line gathers data from the user during execution of the application. These arguments must be input during the execution of the application
from sys import argv

# the below line places the input data into specific positions within the argv variable. Specifically, script is in position 0, and filename is in position 1 of the 
script, filename = argv

# the below line creates the variable txt and assigns it the data in filename after the function opens it up
txt = open(filename)

#the below line simply prints the statement in parenthesis
print(f"Here's your file {filename}:")

#the below line prints the data from the txt variable in read only format
print(txt.read())

# the below line simply prints the statement in parenthesis
#print("Type the filename again:")

# the below line creates the variable file_again and sets it to the value of the users input
#file_again = input("> ")

# the below line creates the variable txt_again and assigns it the data in file_again after the function opens it up
#txt_again = open(file_again)

# the below line prints the data from the txt_again variable in read only format
#print(txt_again.read())

phile = print("What is the name of the file that you are looking for?", input)
print(type(phile))
#txtn = open(phile)

print("Here is the file that you requested.")
#print(txtn.read())