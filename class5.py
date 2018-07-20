#override explicitly inheritance
class Parent():
    def override(self):
        print "override explicitly inheritance "

class Child(Parent):
    def override(self):
        print "heloo"

dad = Parent()
son = Child()

dad.override()
son.override()
