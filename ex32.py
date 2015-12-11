hairs = ['brown', 'blond', 'red']
eyes = ['brown', 'blue', 'green']
weights = [1,2,3,4]


the_cound = [1,2,3,4,5]
fruits = ['apple', "oranges", "pears", "apricots"]
change = [1,"pennies", 2, "dimes", 3, "quartes"]

# this first kind of for-loop goes through a list
for number in the_cound:
	print "This is count %d" % number

for fruit in fruits:
	print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we hanve to use %r since we don't know what's in items
for i in change:
	print "I got %r" % i

for i in change:
	print "I also got" ,i

# we can also build lists, ifrst start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0,6):
	print "Adding %d to the list." % i
	#append is a function that lists understand
	elements.append(i)

# now we can print them out too
for i in elements:
	print "Element was: %d" % i