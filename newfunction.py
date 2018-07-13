#ways to define functions
def x(*args):
    arg1,arg2,arg3 = args
    print "arg1:%r,arg2:%r,arg3:%r"%(arg1,arg2,arg3)

def y(arg4):
    print "arg4:%r"%arg4

x('as','sd','df')
y('dfg')

def add(a,b):
    print "adding %d+%d"%(a,b)
    return a+b

age = add(10,20)
print "%d"%age
