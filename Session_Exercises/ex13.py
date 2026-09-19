from sys import argv
# read the WYSS section for how to run this 
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

x = input("Who am I speaking with? ")

print(f"Hello {x}, how are you doing?")

