from employee2 import *
class CompanySystem:
	def __init__(self):
		self.employedList = {}
		self.accumulatedWage= {}

	def searchEmployeeByName(self, employeeName):
		if employeeName in self.employedList.name:
			return True
		else:
			return False
	
	def searchEmployeeByID(self, _employeeID):
		"""Returns the object if found. If not found, returns False"""
		if self.employedList.get(_employeeID) != None:
			return self.employedList[_employeeID]
		else:
			return False

	#recieves the object employee
	def addEmployee(self, newEmployeeObject):
		"""Adds an employee based on the EmployeeObject."""
		self.employedList[newEmployeeObject.companyID] = newEmployeeObject  #appends the whole object
		self.accumulatedWage[newEmployeeObject.companyID] = 0 # every new employee begins with zero money
		print(f'Employee {newEmployeeObject.getID()} added to the database')
	
	def removeEmployee(self, _employeeID):
		"""Removes an employee after searching for his name. DEPRECATED"""
		if self.searchEmployeeByID(_employeeID) != False:
			return self.employedList.pop(_employeeID)
		else:
			return False

	def removeEmployeeByID(self,employeeID):
		"""Removes an employee after searching for his ID."""
		if self.searchEmployeeByID(employeeID):
			print('Employee removed.')
			self.employedList.pop(employeeID)

CompanySystem = CompanySystem()
test = Employee('blue','blim','h',32,13,55)
test2 = Employee('zaga','blim','h',32,13,55)

id1 = test.getID()
id2 = test2.getID()
print(type(id1))
CompanySystem.addEmployee(test)
CompanySystem.addEmployee(test2)


print(CompanySystem.searchEmployeeByID(id1.hex))
print(CompanySystem.searchEmployeeByID(id2))

CompanySystem.removeEmployeeByID(id1)