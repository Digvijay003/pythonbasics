#override explicitly inheritance
class Parent():
    def override(self):
        print "override explicitly inheritance ko samjo"

class Child(Parent):
    def override(self):
        print "samjo samjo yar"

dad = Parent()
son = Child()

dad.override()
son.override()
