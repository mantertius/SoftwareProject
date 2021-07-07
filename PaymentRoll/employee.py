import uuid


#Class that creates an employee by it's attributes
class Employee:
    def __init__(self,name,address,type,salary,comission):
        self.name = name
        self.address = address
        self.type = type
        self.salary = salary
        self.commission = comission
        self.paymentMethod = 'Depósito em conta bancária'   #correios,cheque em mãos, depósito em conta bancária
        #self.salaryType = type                             #hourly, salaried, commissioned
        self.companyNumber = uuid.uuid4()
        self.sindicateNumber = uuid.uuid4()
        self.sindicateAffiliated = False                    #not affiliated by default
        self.sindicateTax = 0
        self.sindicateServiceTax = 0
        print(f'Empregado criado. Número de matrícula: {self.companyNumber}')

    def getID(self):
        return self.companyNumber

    def setName(self,newName):
        self.name = newName

    def setAddress(self,newAdress):
        self.address = newAdress

    def setPayment(self,paymentMethod):
        self.paymentMethod = paymentMethod

    def setSindicateNumber(self,newNumber):
        self.sindicateNumber = newNumber

    def setType(self, newType, newSalary, newComission):
        self.type = newType
        self.salary = newSalary
        self.commission = newComission
        #print("Dados alterados com sucesso.")

    def setSindicateAffiliation(self, boolean):
        self.sindicateAffiliated = boolean
        #if boolean == false, set sindicate tax to zero

    def setSindicateTax(self,newtax):
        self.sindicateTax = newtax


class CompanySystem:
    def __init__(self) -> None:
        self.employedList = []
        self.accumulatedWage = {} #stores how much the employee is going to recieve in the next payment

    def addEmployee(self, employee):
        self.employedList.append(employee)
        id = employee.getID()
        #print(id)
        self.accumulatedWage[id] = employee.salary
    
    def show(self):
        print()
        print("\nNUM\tNAME\t\tADDRESS\t\tPARCIALWAGE\tTYPE")
        i = 0
        for employee in self.employedList:
            print(f'{i}\t{employee.name}\t\t{employee.address}\t\t{self.accumulatedWage.get(employee.getID())}\t\t{employee.type}')
            i +=1
        print()
    
    def fireEmployee(self, employee):
        a = self.employedList.pop(self.employedList.index(employee))
        return a

    def dayWage(self, arrival, leaving, employeeName):
        try:
            employee = self.employedList[self.getEmployeeIndexByName(employeeName)]
            id = employee.getID()
            print(f"Encontrado {employee.name}, id: {employee.getID()}!!")
            workedHours = leaving - arrival
            print(f"Horas trabalhadas: {workedHours}")
            total = workedHours
            if workedHours > 8:
                extra = workedHours - 8
                total = employee.hourWage*8 + employee.hourWage*extra*1.5
                print(f'Horas extras: {extra}. Total a ser pago: {total}')

                ##something is wrong with the get.id() and the accumulatedWage.
            self.accumulatedWage[id] += total
            print(f'{total} adicionado em sua carteira.')
        except Exception:
            print("dayWage: Employee not found.")

    def getEmployeeIndexByName(self,employeeName):
        for index,employee in enumerate(self.employedList):
            if employee.name == employeeName:
                return index
        raise(f"getEmployeeIndexByName: Employee {employeeName} not found.")
    
    def addSaleToEmployee(self,employeeName,saleValue):
        try:
            employee = self.employedList[self.getEmployeeIndexByName(employeeName)]
            self.accumulatedWage[UUID('employee.getID()')] += saleValue*employee.comission
            print(f'Venda de {saleValue} realizada por {employeeName}.')
        except Exception:
            print(f'addSaleToEmployee: Employee {employeeName} not found')


#   ███╗   ███╗ █████╗ ██╗███╗   ██╗     ██████╗ ██████╗ ██████╗ ███████╗
#   ████╗ ████║██╔══██╗██║████╗  ██║    ██╔════╝██╔═══██╗██╔══██╗██╔════╝
#   ██╔████╔██║███████║██║██╔██╗ ██║    ██║     ██║   ██║██║  ██║█████╗  
#   ██║╚██╔╝██║██╔══██║██║██║╚██╗██║    ██║     ██║   ██║██║  ██║██╔══╝  
#   ██║ ╚═╝ ██║██║  ██║██║██║ ╚████║    ╚██████╗╚██████╔╝██████╔╝███████╗

system = CompanySystem()

antonio = Employee(name='Antonio',address='rua1',type ='comissioned',salary=100,comission=0.4) #por venda
baba = Employee('Barbara','rua2','hourist',1,0) #por hora
cece = Employee('Carlos','rua3','salaried',55500,0) #tanto faz


system.addEmployee(antonio)
system.addEmployee(baba)
system.addEmployee(cece)
print()
system.show()

#newname = None
#antonio.setSettings(name = newname)

a = system.fireEmployee(cece)
print(f'\nEmpregado demitido.{a.getID()}')
system.show()

#print(system.accumulatedWage)
system.dayWage(6,16,'Barbara')

cleiton = Employee('Cleiton','rua4','comissioned',1000, 0.06)
system.addEmployee(cleiton)

system.addSaleToEmployee('Cleiton',50000)
system.show()

#TODO change from a type to another