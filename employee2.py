import uuid

class Employee:
	def __init__(self,name,address,type, salary,commission=0,hourWage=0): #by default is a salaried
		self.name = name
		self.address = address
		self.type = type  #salaried,commissioned,hourist
		self.paymentMethod = 'Depósito em conta bancária'   #correios,cheque em mãos, depósito em conta bancária
		self.companyID = uuid.uuid4()
		self.unionID = None
		self.hourWage = hourWage
		self.salary = salary
		self.unionStatus = False
		self.unionFee = 0
		self.commission = commission
		print(f'Employee created. UUID: {self.companyID.hex}')

#getters 
	def getName(self):
		return self.name
	def getAddress(self):
		return self.address		
	def getType(self):
		return self.type
	def getID(self):
		return self.companyID
	def getPayment(self):
		return self.paymentMethod
	def getUnionStatus(self):
		return self.unionStatus
	def getUnionFee(self):
		return self.unionFee
	def getUnionID(self):
		return self.unionID
	def getCommission(self):
		return self.commission
#setters
	def setName(self, newName):
		self.name = newName
		print('Name changed successfully.')
	def setAddress(self, newAddress):
		self.address = newAddress
		print('Address changed successfully.')
	def setUnionID(self, newID):
		self.unionID = newID
		print('UnionID changed successfully.')
	def setHourWage(self, newWage):
		self.hourWage = newWage
		print('Hour wage changed successfully.')
	def setSalary(self,newSalary):
		self.salary = newSalary
		print('Salary changed successfully.')
	def setUnionStatus(self, status):
		self.unionStatus = status
		print('Union status changed successfully.')
	def setUnionFee(self, newTax):
		self.sidicateTax = newTax
		print('Union tax changed successfully')
	def setComission(self, newCom):
		self.commission = newCom
		print('Commission changed successfully.')

#type changers
	def setType(self, newType, newSalary, newHourWage, newCommission):
			self.salary = newSalary
			self.commission = newCommission
			self.hourWage = newHourWage
			self.type = newType