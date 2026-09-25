from sys import argv

script, input_file = argv

def print_a_line(line_count, f):
   # Rewind to the start of the file first so the target line calculation is consistent
   f.seek(0)

   # Read and discard lines leading up to the target line
   for _ in range(line_count - 1):
      f.readline()

   # Read and print the target line
   print(f.readline())
   print("\n")

def print_all(f):
   print(f.read())
   print("\n")
   

current_file = open(input_file)

print_all(current_file)

line_count = int(input("What line would you like to re-read? "))
print("\n")
print_a_line(line_count, current_file)

