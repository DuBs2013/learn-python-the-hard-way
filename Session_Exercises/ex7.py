#More Printing

#Line 4 is a standard print statement
print("Mary had a little lamb.")

#Line 7 is a formatted print statement where the .format function is added at the end instead of using the 'f' before the double quotes. This is a cleaner form of code.
print("Its fleece was white as {}.".format('snow'))

#Line 10 is also a standard print statement
print("And everywhere that Mary went.")

#Line 13 is a print statement that prints multiple copies of the object in a row on the same line
print("." * 10)

#Lines 16 through 27 are just variables 
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u" 
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. Try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
