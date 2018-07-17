#use of super function in class inheritance
class Parent(object):
    def altered(self):
        print "parent altered ho gya "

class Child(Parent):
    def altered(self):
        print "child parent altered honse se pehle ka "
        super(Child,self).altered()
        print "ye hai baad ka child "

dad = Parent()
son = Child()

dad.altered()
son.altered()
