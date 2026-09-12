# The below line sets a variable named formatter and gives it 4 elements
formatter = "{} {} {} {}"

# The below lines print the formatter variable and formats it accordingly for each print command that call it. Different output for each command
print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
   "Try your", 
   "Own text here",
   "Maybe a poem",
   "Or a song about fear"
))

# The below line sets a variable named fatmatter and gives it 3 elements. The word fatmatter is also squiggly underlined because it is not a recognized word in VSCode
fatmatter = "{} {} {}"

# The below line prints the fatmatter variable and formats it with the elements that I asked it to format. Note: it will only print the number of elements that it is formatted for i.e. it will only print the first three elements in sequence
print(fatmatter.format("True", "False", "True", "False"))

# The below line will throw an error 
# "IndexError: Replacement index 2 our of range for positional args tuple" 
# because the fatmatter.format calls for 3 elements and we only provided 2
print(fatmatter.format("in", "the"))
