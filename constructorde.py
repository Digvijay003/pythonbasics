"""constructots and dde"""
class Person(Object):
    def __init__(self):
	    print("this is constructots")
		
	def __del__(self):
	    print("this is deconstructor")
		
Person_name = Person()
Person_name.__del__()
