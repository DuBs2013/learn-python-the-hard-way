# this is the additional study drill for exercise 19
# I must write a function and call it 10 different ways

def halloween_approaches(decorations, candy):
   print("""Halloween is approaching. It is my favorite time of year.
   \b\b\bAre you ready for the holiday?""")
   print(f"""I have bought {decorations} decorations, and {candy} bags of candy in preparation for 
   \b\b\ball of the trick-or-treaters that will be stopping by our house.\n""")

# the below two lines declares the variables decorations and candy
decorations = 15
candy = 10

# 1 the below line calls the function and uses the variables declared above
halloween_approaches(decorations, candy)

# 2 the below line calls the function and uses hard coded values as the arguments
halloween_approaches(2,3)

# 3 the below line calls the function and uses the variables declared above and some math as the arguments
halloween_approaches(decorations + 2, candy - 7)

# 4 the below line uses hard coded math functions as the values for the arguments 
halloween_approaches(round(10 / 2), 4 * 4)

# 5 the below line uses string values as the arguments for the function
halloween_approaches("No", "Zero")

# the below two lines convert the initial variables into strings for further manipulation
decorations_str = str(decorations)
candy_str = str(candy)

# 6 the below line calls the function and uses the string conversions as arguments
halloween_approaches(decorations_str, candy_str)

# 7 the below line calls the function and uses string 
halloween_approaches(decorations_str + " scary" , candy_str + " big")

# the below lines reassign the values of decorations and candy to be strings
decorations = "spooky"
candy = "ten"

# 8 the below line calls the function and uses the reassigned string values of the variables
halloween_approaches(decorations, candy)

# 9 the below line calls the function and uses the reassigned string values of the variables and concatenates them with hard coded strings
halloween_approaches(decorations + " scary", candy + " expensive")

# 10 the below line calls the function and uses both the converted int values from lines 30 & 31 and concatenates them with the reassigned values of the original values from lines 40 and 41
halloween_approaches(decorations_str + " " + decorations, candy_str + " " + candy)






   