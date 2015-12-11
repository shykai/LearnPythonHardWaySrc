from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
filename = raw_input("> ")

txt = open(filename)
print txt.read()