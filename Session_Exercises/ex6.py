#Strings and Text
# The following line creates an integer variable 
types_of_people = 10

#The following line creates a formatted string variable. a string with a format for the integer variable insertion
x = f"There are {types_of_people} types of people."

# The next two lines create simple string variables
binary = "binary"
do_not = "don't" 

# The following line creates a formatted string variable similar to the one on line 6
y = f"Those who know {binary} and those who {do_not}."

# These two print statements are simple print statements. Nothing out of the ordinary
print(x)
print(y)

# The following print statements utilize the "format" function to allow insertion to be applied to the respective print statements. note: {x} outputs the x variable without any quotation mark, where '{y}' outputs the y variable inside of single quotation marks
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Two variables one a boolean and one a sting
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# The following print state utilizes the .format() function to insert "False" into the sting
print(joke_evaluation.format(hilarious))

# Two stings set to the variables w and e respectively
w = "This is the left side of..."
e = "a sting with a right side."

# The following print state concatenates stings w and e
print(w + e)
