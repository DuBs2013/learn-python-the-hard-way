print("How old are you?", end='')
age = input()
print("How tall are you?", end='')
height = input()
print("How much do you weigh?", end='')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# The below lines are additional exercises found on w3schools.com/python
print("Enter your name:")
name = input()
print(f"Hello {name}")

name = input("Enter thoust call sign:")
print(f"Welcome {name} to the valley of the REAL...")
fav1 =input("Where do you hail from?")
fav2 =input("What is it that you seek?")
fav3 =input("What is your favorite color?")
print(f"Well {name} from {fav1}, since you are seeking {fav2}, you must give me a {fav3} shrubbery in order to pass this bridge.")


# This section is designed to switch an input string (because all input from a user is treated as a string) to a number
x = input("Enter a number:") #Note: if you fail to put a number when requested here, it will throw a "ValueError: could not convert string to float: '' "
y = round(float(x) * 10)
print(f"You have entered the number {x} and 10 times that value is {y}.")

# This section is from Zed's book concerning number allocation from a user
x = int(input("Enter a number:"))
print(f"The number that you gave me was: {x}, correct?")

# This section is about input validation
