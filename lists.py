# understanding python lists
list1 = ['a','b',56,'c',100]
print list1[0]
print "list1[1:5]" , list1[1:5]
list1[2] = 'honey'
print list1[2]
print list1
del list1[2]
print list1
print len(list1)
print max(list1)
list1.append(54654)
print list1
list1.insert(4,'hello')
print list1
list1.reverse()
print list1
print "below this is dictionary conecpts "
# understanding dictionatry concepts

dict = {'name':'honey','age':'21','class':'first class','address':'gurgaon'}
print dict['name']
dict2 = dict.copy()
print str(dict2)
print dict.keys()
print dict.get('age')
print dict.get('sex')

