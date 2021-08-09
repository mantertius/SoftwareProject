import datetime
from tkinter import *
from typing import Container 

asciiTitle ="""           
                                   _   _ 
  _ __   __ _   _  _   _ _   ___  | | | |
 | '_ \ / _` | | || | | '_| / _ \ | | | |
 | .__/ \__,_|  \_, | |_|   \___/ |_| |_|
 |_|            |__/            
 """           
def destroyWin(self):
    quit(self)

class addWindow():
    def __init__(self,root) -> None:
        self.root = root
        self.root.title("Add an employee")
        lbl1 = Label(self.root,text="Name").pack(side=LEFT)
        entry1 = Entry(self.root,width=15).pack(side=RIGHT)
    
        
        lbl2 = Label(self.root, text='Address').pack(side=LEFT)
        entry2 = Entry(self.root,width=25).pack(side=RIGHT)
        self.root.mainloop()
        
class Menu(Frame):
    """ It's the class that shows the MENU."""
    def __init__(self,master=None):
        self.root = Frame.__init__(self,master)
        # ---- default settings ----
        timeNow = datetime.datetime.now()
        self.defaultFont = ("Arial", "10")
        self.titleFont = ("Arial",'10','bold')

    # ---- title ----
        self.titleContainer = Frame(master,pady=20)
        self.titleContainer.pack(fill='x')
        self.title = Label(self.titleContainer,justify=LEFT, text=asciiTitle,font=('Courier','10','bold'))
        self.title.pack()

    # ----- date -----       
        self.dateContainer = Frame(master,pady=20).pack()
        self.date = Label(self.dateContainer,text=f'Today is {timeNow.strftime("%x")}',pady=20).pack()
        
    # ----- add employee -----
        self.addEmployeeContainer = Frame(master).pack(pady=0)
        self.btnAddEmployee = Button(self.addEmployeeContainer,text='Add Employee', command=self.addEmployee).pack()
        
    # ----- remove employee -----       
        self.removeEmployeeContainer = Frame(master,pady=0)
        self.removeEmployeeContainer.pack()
        self.btnRemoveEmployee = Button(self.removeEmployeeContainer,text='Remove Employee', command=self.rmvEmployee)
        self.btnRemoveEmployee.pack()

    # ----- change employee -----       
        self.changeEmployeeContainer = Frame(master, pady=0).pack()
        self.btnChangeEmployee = Button(self.changeEmployeeContainer, text='Change Employee', command=self.changeEmployee).pack(pady=0)

    # ----- placeholder -----
        self.spacer=Frame(master,pady=20).pack()
        self.spacerLbl=Label(self.spacer,text='').pack()

    # ----- send point ----      
        self.sendPointContainer = Frame(master,pady=20).pack()
        self.btnSendPoint = Button(self.sendPointContainer,text='Send Electronic Point Data',command=self.sendPoint).pack()
        
    # ----- send Sale ----       
        self.sendSaleContainer = Frame(master,pady=20).pack()
        self.btnSendSale = Button(self.sendSaleContainer,text='Send Sale Data',command=self.sendSale).pack()
        
    # ----- send tax -----       
        self.sendTaxContainer = Frame(master,pady=20).pack()
        self.btnSendTax = Button(self.sendTaxContainer,text='Send Service Tax',command=self.sendTax).pack()
    
    # ----- spacer -----
        self.spacerLbl=Label(self.spacer,text='').pack()

    # ----- change payday -----       
        self.changePaydayContainer = Frame(master,pady=20).pack()
        self.btnChangePayday = Button(self.changePaydayContainer,text='Change Payday',command=self.changePayday).pack()

    # ----- create payday -----       
        self.createPaydayContainer = Frame(master,pady=20).pack()
        self.btnCreatePayday = Button(self.createPaydayContainer, text='Create Payday',command=self.createPayday).pack()
        
    # ----- run payroll -----       
        self.runPayrollContainer = Frame(master,pady=20)
        self.runPayrollContainer.pack()
        self.btnRunPayroll = Button(self.runPayrollContainer,text='Run Payroll',font=('Arial','11','bold'),command=self.runPayroll).pack()

    # ----- exit -----       
        self.exitButtonContainer = Frame(master,pady=20,borderwidth=2,relief=RAISED)
        self.exitButtonContainer.pack(side=BOTTOM,fill=BOTH,expand=TRUE)
        self.btnExit = Button(self.exitButtonContainer,text='Exit',command=self.destroyWindow)
        self.btnExit.pack(side=BOTTOM)

    def addEmployee(self):
        win = Toplevel(menu)
        master = win
        win.after(1000,win.update)
        # ----- settings -----
        win.title("Add Employee")
        options = ['','hourly', 'salaried', 'commissioned']
        # ----- brief explanation of the function
        container1 = Frame(win,pady=20)
        container1.pack()
        title = Label(container1,text='Fill the data of the new employee then press the button.',font=self.titleFont)
        title.pack()

        # ----- name ------
        container2 = Frame(win,pady=0)
        container2.pack()
        lbl1 = Label(container2, text='Name')
        lbl1.pack(padx=5,side=LEFT)
        entry1 = Entry(container2,width=25)
        entry1.pack(side=RIGHT)

        # ----- address -----   
        container3 = Frame(win,pady=0)
        container3.pack()
        lbl2 = Label(container3,text='Address')
        lbl2.pack(padx=5,side=LEFT)
        entry2 = Entry(container3,width=25)
        entry2.pack(side=RIGHT)

        # ----- type dropdown ------
        container4 = Frame(win,pady=0)
        container4.pack()
        lbl3 = Label(container4,text='Type')
        lbl3.pack(side=LEFT,pady=5)
        type = StringVar(master)
        type.set(options[0])
        typeChooser = OptionMenu(container4,type,*options)
        typeChooser.pack(side=RIGHT)

        # ----- salary bonus based on type set -----
        if type.get() == 'salaried':
            container4 = Frame(win,pady=0)
            container4.pack()
            salary = Label(container4,text='Salary')
            salary.pack(side=LEFT)
            entry3 = Entry(container4,width=25)
            entry3.pack()
        elif type.get() == 'hourly':
            container4 = Frame(win,pady=0)
            container4.pack()
            salary = Label(container4,text='Salary')
            salary.pack(side=LEFT)

        
        # ----- exit ------
        self.exitButtonContainer = Frame(master,pady=5,borderwidth=1,relief=RAISED)
        self.exitButtonContainer.pack(side=BOTTOM,fill=X)
        self.btnExit = Button(self.exitButtonContainer,text='Exit',command=win.destroy)
        self.btnExit.pack(side=LEFT)
    
    def rmvEmployee(self):
        pass
    
    def changeEmployee(self):
        pass

    def sendPoint(self):
        pass
    
    def sendSale(self):
        pass
    
    def sendTax(self):
        pass
    
    def changePayday(self):
        pass

    def createPayday(self):
        pass

    def runPayroll(self):
        pass

    def destroyWindow(self):
        destroyWin(self)


menu = Tk()
app = Menu(menu)
menu.title("Payroll System")
menu.mainloop()