# UNDERSTANDING MODULES
"""
how we access in a dictionary
"""
x = {'a':"hello"}
print x['a']
"""
how we access in modules the same thing
"""
import x # first we import that module where we defined all functions inside of it
x.a()
# basically a is function which we defined in module named x
# def a():
   # print "hello"
"""
how we access this using class method
"""
# class is better than  modules coz we can use the functions inside of class many times but in case of module we have to import it whenever we want to use it
class X(object):
    def _init_(self):#this is inbulit function of python 

    def a(self):
        print "hello"

"""
when we create a class we get a object """

a = x()# this is how a object is created 
a.y()

# we get things from things in each dictionary, module and class 
