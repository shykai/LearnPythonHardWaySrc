class ParserError(Exception):
	pass

class Sentence(object):
	
	def __init__(self,subject, verb, obj):
		# remember we take ('noun','priencess') tuples and convert them
		self.subject = subject[1]
		self.verb = verb[1]
		self.object = obj[1]
	
	def peek(word_list):
		if word_list:
			word = word_list[0]
			return word[0]
		else:
			return None
	
	def match(word_list, expecting):
		if word_list:
			word = word_list.pop(0)
			
			if word == expecting:
				return word
			else:
				return None
		else:
			return None