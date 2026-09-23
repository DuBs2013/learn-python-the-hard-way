from sys import argv

script, filename = argv

User = input("Hello there, who am I speaking with?")

print(f"Hello again {User}, I am guessing that you would like to open {filename}.\n")

with open(filename, 'a+') as file:# by using the 'with' command, Python automatically closes the file as son as we exit the code block
   file.seek(0)
   existing_content = file.read()
   print("Existing Content:\n", existing_content)

   new_data = input("What would you like to add to this file?")

   file.write(f"\nThis is the new data:\n{new_data}")




