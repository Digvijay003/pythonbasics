"""iterators """
class Remotecontrol():
    def __init__(self):
	    self.channels = ['a','b','c','d','e']
	    self.index = -1
		
    def __iter__(self):
	    return self 
		
    def __next__(self):
	    self.index += 1
	    if self.index == len(self.channels):
		    raise StopIteration
	    return self.channels[self.index]
		
r = Remotecontrol()
iter = iter(r)
print(iter)
