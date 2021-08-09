class CompanySystem:
	
	def __init__(self):
		self.employedList = []
		self.accumulatedWage= {}

	def searchEmployeeByName(self, employeeName):
		if employeeName in self.employedList.companyID:
			return True
		else:
			return False

	#recieves the object employee
	def addEmployee(self, newEmployeeObject):
		self.employedList.append(newEmployeeObject) #appends the whole object
		self.accumulatedWage[newEmployeeObject] = 0 # every new employee begins with zero money
	
	def removeEmployee(self, firedEmployeeObject):
		if not self.searchEmployeeByName(firedEmployeeObject.name):
			poppedEmployee = self.employedList.pop(firedEmployeeObject)
			print(f'Fired:{firedEmployeeObject.companyID}')
			return poppedEmployee
		else:
			print("Employee not found.")