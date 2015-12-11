class lexicon(object):
	Direction_Words=["north","south","east","west","down","up","left","right","back"]
	Verb_Words=["go","stop","kill","eat"]
	Stop_Words=["the","in","of","from","at","it"]
	Noun_Words=["door","bear","princess","cabinet"]

	def convert_number(s):
		try:
			return int(s)
		except ValueError:
			return None
			
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
			return None

	def scan(s):
		out = []
		words = s.split(s)
		for word in words:
			obj = convert_object(word)
			if obj:
				out.append(obj)
			obj = convert_number(word)
			if obj:
				out.append(obj)
		return out