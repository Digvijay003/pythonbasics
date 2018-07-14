from sys import argv
from os.path import exists

script , from_file, to_file = argv

print "copying from %s to %s"%(from_file, to_file)
in_file = open(r'C:\Python27\2.txt')
indata = in_file.read()

print "input file is %d bytes long"%len(indata)
print "does output file exists %r"%exists(to_file)

print "hit enter"
raw_input()

out_file = open(r'C:\Python27\abc.txt', 'w')
out_file.write(indata)

print"ok"

out_file.close()
in_file.close()
