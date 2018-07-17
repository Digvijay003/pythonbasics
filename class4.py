#class inheritance concepts
class Parent():
    def implicit(self):
        print"implicit inheritance samjo"

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
