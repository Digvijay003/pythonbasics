from sys import argv
script, filename = argv

print "erase file %r"%filename
print "hit enter"

raw_input("?")

print "opening file "
target = open(r'C:\Python27\abc.txt', 'w')

print "truncate"
target.truncate()

line1 = raw_input("line1:")

print "write these lines"
target.write(line1)

print "close ot"
target.close()
