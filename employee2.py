import uuid

class Employee:
	def __init__(self,name,address,type, salary,commission,hourWage):
		self.name = name
		self.address = address
		self.type = type 
		self.companyID = uuid.uuid4()
		self.sindicateID = uuid.uuid4()
		self.hourWage = hourWage
		self.salary = salary
		self.sindicateStatus = False
		self.sindicateTax = 0
		self.commission = commission
		print(f'Employee created. UUID: {self.companyID}')

#getters 
	def getName(self):
		return self.name
	def getAddress(self):
		return self.address		
	def getType(self):
		return self.type
	def getID(self):
		return self.companyID
		
#setters
	def setName(self, newName):
		self.name = newName
		print('Name changed successfully.')
	def setAddress(self, newAddress):
		self.address = newAddress
		print('Address changed successfully.')
	def setSindicateID(self, newID):
		self.sindicateID = newID
		print('SindicateID changed successfully.')
	def setHourWage(self, newWage):
		self.hourWage = newWage
		print('Hour wage changed successfully.')
	def setSalary(self,newSalary):
		self.salary = newSalary
		print('Salary changed successfully.')
	def setSindicateStatus(self, status):
		self.sindicateStatus = status
		print('Sindicate status changed successfully.')
	def setSindicateTax(self, newTax):
		self.sidicateTax = newTax
		print('Sindicate tax changed successfully')
	def setComission(self, newCom):
		self.commission = newCom
		print('Commission changed successfully.')

#type changers
	def setType(self, companySystem, newType, newSalary, newHourWage, newCommission):
			self.salary = newSalary
			self.commission = newCommission
			self.hourWage = newHourWage
			self.type = newType