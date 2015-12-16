from ex48 import lexicon
from ex48.parser import *

words = lexicon.scan("go north")
print words
x = parse_sentence(words)
print "subject:", x.subject
print "verb:", x.verb
print "object:", x.object

