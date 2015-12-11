Direction_Words=["north","south","east","west","down","up","left","right","back"]
Verb_Words=["go","stop","kill","eat"]
Stop_Words=["the","in","of","from","at","it"]
Noun_Words=["door","bear","princess","cabinet"]

def convert_number(s):
	try:
		return ('number',int(s))
	except ValueError:
		return ('error', s)
		
def convert_object(s):
	if s in Direction_Words:
		return ('direction', s)
	elif s in Verb_Words:
		return ('verb', s)
	elif s in Stop_Words:
		return ('stop', s)
	elif s in Noun_Words:
		return ('noun', s)
	else:
		return convert_number(s)

def scan(s):
	out = []
	words = s.split()
	for word in words:
		out.append(convert_object(word))
	return out

