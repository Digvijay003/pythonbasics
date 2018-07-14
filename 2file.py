from sys import argv
script, filename = argv
txt = open(r'C:\Python27\2.txt')
print "ur file is %r"%filename
print txt.read()
print "type filename again "
file_again = raw_input("> ")

txt_again = open(r'C:\Python27\2.txt')
print txt_again.read()


