from sys import argv
from os.path import exists

script, from_file, to_file = argv

in_file = open(from_file, 'r').read()

print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(in_file)

print("Alright, all done.")

out_file.close()