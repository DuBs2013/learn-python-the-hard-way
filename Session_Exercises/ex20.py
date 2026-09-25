from sys import argv

script, input_file = argv

def print_all(f):
   print(f.read())

def rewind(f):
   f.seek(0)

def print_a_line(line_count, f):
   print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("\nNow let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

# the below line sets the current_line variable to 1
current_line = 1

# the below line calls the "print_a_line" function with the current_line variable is set to 1. When the function is called, current_line is used as the line_count argument
print_a_line(current_line, current_file)

# the below line increases the current_line by 1 - i.e. the variable goes from 1 to 2. 
current_line += current_line #original code current_line = current_line + 1

# the below line calls the "print_a_line" function with the current_line variable is set to 2. When the function is called, current_line is used as the line_count argument
print_a_line(current_line, current_file)

# the below line increases the current_line by 1 - i.e. the variable goes from 2 to 3. 
current_line += current_line #original code current_line = current_line + 1

# the below line calls the "print_a_line" function with the current_line variable is set to 3. When the function is called, current_line is used as the line_count argument
print_a_line(current_line, current_file)



