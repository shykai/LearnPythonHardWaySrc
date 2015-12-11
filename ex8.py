# -*- coding: utf-8 -*-


formatter = "%r %r %r %r"

printer1 = (1,2,3,4)
printer2 = ("One", "Two", "Three", "Four")
printer3 = (True, True, False, True)
printer4 = (
	"I had this thing.中文",
	"That you could type up right.",
	"but it didn't sing.",
	"So I said goodnight."
)

print formatter % printer1
print formatter % printer2
print formatter % printer3
print formatter % printer4

#printerChn = (u"中", u"国", u"地", u"图")

#print formatter % printerChn

