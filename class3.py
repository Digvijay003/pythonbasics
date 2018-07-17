class Employee(): 
    x = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.x += 1

    def displaycount(self):
        print "%d"%Employee.x

    def displayEmployee(self):
        print "name:", self.name, "salary:", self.salary
        
emp1 = Employee("honey", 200000000000)
emp1.displayEmployee()
print "%d"%Employee.x

