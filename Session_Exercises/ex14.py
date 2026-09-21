from sys import argv

script, user_name = argv

answer = "> " # the greater than sign in the parenthesis is used as text

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(answer)

print(f"Where do you live {user_name}?")
lives = input(answer)

print("What kind of computer do you have?")
computer = input(answer)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer.  Nice.
""")

print("Please enter two names.")
first, second = argv #this line of code takes the value of script and saves it to first. It also takes the value of user_name and saves it to second.

print(f"So you think that {first} is better than me?")
print(f"Well to that I say that {second} is better than you. So there.")


