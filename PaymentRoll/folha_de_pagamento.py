#TODO 1 função getPaid(type,salary,comission,methodOfPayment)
import uuid
from PaymentRoll import employee

class System:
    def __init__(self,date) -> None:
        self.date = date
        pass


#Function to remove an employee based on his name 
def removeEmployee(employed,employee):
    counter = 0
    for obj in employed:
        if obj.name == employee:
            del employed[counter]
            print(f'Empregado {employee} removido com sucesso.')
            break
        else:
            counter += counter

#Function to add an employee
def addEmployee(employed,name,address,type):
    employed.append(Employee(name,address,type))


#   ███╗   ███╗ █████╗ ██╗███╗   ██╗     ██████╗ ██████╗ ██████╗ ███████╗
#   ████╗ ████║██╔══██╗██║████╗  ██║    ██╔════╝██╔═══██╗██╔══██╗██╔════╝
#   ██╔████╔██║███████║██║██╔██╗ ██║    ██║     ██║   ██║██║  ██║█████╗  
#   ██║╚██╔╝██║██╔══██║██║██║╚██╗██║    ██║     ██║   ██║██║  ██║██╔══╝  
#   ██║ ╚═╝ ██║██║  ██║██║██║ ╚████║    ╚██████╗╚██████╔╝██████╔╝███████╗

employed = [] #creates a list of employed

addEmployee(employed,"antonio","rua","rico") #adds employee to "employed" list
addEmployee(employed,"barbara","casa","pobre")
addEmployee(employed,"carlos","casa2","ok")

#printing for verification
print("\nNAME\tADDRESS\tTYPE")
for obj in employed:
    print(obj.name, obj.address, obj.type)


removeEmployee(employed,"antonio")

print("\nNAME\tADDRESS\tTYPE")
for obj in employed:
    print(f'{obj.name}\t{obj.address}\t{obj.type}')
