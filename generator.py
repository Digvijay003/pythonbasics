""" generators """
def fib():
    a,b = 0,1
    while True:
	    a,b = b,a+b
		
for f in fib():
	if f>100:
		break 
    print(f)
		
		
		
""" genertors are simple way of creating iterartors """
""" when u call a return function it always retuen value by deleting its local variables """
