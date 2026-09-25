# the below lines are a function that has two arguments, when called executes print statements relative to the input arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
   print(f"you have {cheese_count} cheeses!")
   print(f"You have {boxes_of_crackers} boxes of crackers!")
   print("Man that's enough for a party!")
   print("Get a blanket.\n")


# the below lines simply print the identifying string and calls the functions using the hard coded numbers as the arguments for the function
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


# the below lines simply print the identifying string and create the variables listed
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# the below line calls the function and uses the variables identified just above as the arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# the below lines simply print the identifying string and calls the cheese_and_crackers function using the simple math as the arguments
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# the below lines simply print the identifying string and calls the cheese_and_crackers function using the variables identified further up in the code and math as the arguments
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

