#!/usr/bin/python
class Employee:
	"Common base class for all employees"
	empCount = 0
        
        #Constructor
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1

	def displayCount(self):
		print ("Total Employee : " + Employee.empCount)

	def displayEmployee(self):
		print ("Name : ", self.name, ", Salary: ", self.salary)

	def __del__(self):
                class_name = self.__class__.__name__   # class name
                print (class_name, "destroyed")

def main():
	"This would create first object of Employee class"
	emp1 = Employee("Zara", 2000)

	"This would create second object of Employee class"
	emp2 = Employee("Manni", 5000)

	emp1.displayEmployee()
	emp2.displayEmployee()
	print ("Total Employee : " , Employee.empCount)
	print ("doc : ", emp1.__doc__)
	print ("function name : ", __name__)  # function name
#	print ("function line : ", __line__)  # function name
	print ("dict : ", emp1.__dict__)
	print ("module : ", emp1.__module__) # class function

	print ("dict : ", emp2.__dict__) # class members

	x = getattr(emp1, 'salary')
	print("salary of emp1 : ", x)
	setattr(emp1, 'salary',8000)

	x = getattr(emp1, 'salary')
	print("salary of emp1 : ", x)

if __name__ == main():
	main()
