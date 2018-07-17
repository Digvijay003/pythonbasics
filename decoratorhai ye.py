"""python decorators """
import time 

def time(func):
    def wrapper(*args, **kwargs):
	    start = time.time()
	    result = func(*args,**kwargs)
	    end = time.time()
	    print(func.__name__ + str((end-start))*10000)
	    return result 
    return wrapper

@time 
def square(numbers):
    result = []
    for number in numbers:
	    result.append(number*number)
    return result 
	
array = range(1,100)
object = square(array)
