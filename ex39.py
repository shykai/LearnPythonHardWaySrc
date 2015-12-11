# Create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	"Florida":"FL",
	"California":"CA",
	"New York": "NY",
	"Michigan": "MI",
	}
	
# Create a basic set of states and some cities in them
cities = {
	"CA": "San Francisco",
	"MI": "Detroit",
	"FL": "Jacksonville",
}

def printlines():
	print "-"*10

# add some more cities
cities["NY"] = "New York"
cities["OR"] = "Portland"

# print out some cities
printlines()
print "NY State has: ", cities["NY"]
print "OR State has: ", cities["OR"]

# print some states
printlines()
print "Michigan's abbreviation is:",  states["Michigan"]
print "Florida's abbreviation is:",  states["Florida"]

#print do it by using the state then cites dict
printlines()
print "Michigan has:",  cities[states["Michigan"]]
print "Florida has:",  cities[states["Florida"]]

# print every state abbreviation
printlines()
for state, abbrev in states.items():
	print "%s is abbreviated %s" %(state, abbrev)
	
# print every city in state
printlines()
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)
	
# now do both at the same time
printlines()
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" %(state, abbrev, cities[abbrev])
	
printlines()
# safely get abbreviation by state that might not be there
state = states.get("Texas")

if not state:
	print "Sorry, no Texas."
print state
# get a city with default value
city = cities.get("TX", "Does Not Exist")
print "The city for the state 'TX' is: %s" % city