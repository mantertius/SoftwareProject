import datetime
from tkinter import *
from tkinter import ttk


asciiTitle ="""           
                                   _   _ 
  _ __   __ _   _  _   _ _   ___  | | | |
 | '_ \ / _` | | || | | '_| / _ \ | | | |
 | .__/ \__,_|  \_, | |_|   \___/ |_| |_|
 |_|            |__/            
 """           
class checkbar(Frame):
    """It's the checkbar's class!"""
    def __init__(self, parent=None, picks=[],side=LEFT,anchor=W):
        Frame.__init__(self,parent)
        self.vars = []
        for pick in picks:
            var = IntVar()
            chk = Checkbutton(self, text=pick, variable=var)
            chk.pack(side=side,anchor=anchor,expand=YES)
            self.vars.append(var)
    def state(self):
        return map(lambda var:var.get(),self.vars)
class addWindow():
    def __init__(self,root) -> None:
        self.root = root
        self.root.title("Add an employee")
        lbl1 = Label(self.root,text="Name").pack(side=LEFT)
        entry1 = Entry(self.root,width=15).pack(side=RIGHT)
    
        
        lbl2 = Label(self.root, text='Address').pack(side=LEFT)
        entry2 = Entry(self.root,width=25).pack(side=RIGHT)
        self.root.mainloop()

def destroyWin(self):
    quit(self)

def submit(win,data):
    
    
    #send the data to the database?
    pass

def showComission(container,lbl,entry,type):

    selected = type.get()
    if selected == 'commissioned':
        container.pack()
        lbl.pack(side=LEFT)
        entry.pack(side=RIGHT)
    else:
        container.pack_forget()
        lbl.pack_forget()
        entry.pack_forget()

def employeeRemover(id) -> bool:
    #search for (uuid) 
    # if uuid = found -> kill -> return true
    # else -> return false
    pass

def employeeChanger(id,dictionary) -> bool:
    #dictonary shows what needs to be changed {'name':"new_name"}
    #sends to change stuff
    pass
class Menu(Frame):
    """ It's the class that shows the MENU."""
    def __init__(self,master=None):
        self.root = Frame.__init__(self,master)
        # ---- default settings ----
        timeNow = datetime.datetime.now()
        self.defaultFont = ("Arial", "10")
        self.titleFont = ("Arial",'10','bold')
# MENU #########################################################################################
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
        self.btnExit = Button(self.exitButtonContainer,text='Exit',command=lambda arg1=self:destroyWin(self))
        self.btnExit.pack(side=BOTTOM)

# FEATURES  #######################################################################
    
    def addEmployee(self):
        menu.withdraw()
        win = Toplevel(menu)
        master = win
        # ----- settings -----
        win.title("Add Employee")
        options = ['hourly', 'salaried', 'commissioned']
        # ----- brief explanation of the function
        container1 = Frame(win,pady=20)
        container1.pack()
        title = Label(container1,text='Fill the data of the new employee then press the button.',font=self.titleFont)
        title.pack()

        # ----- name ------
        container2 = Frame(win,pady=0)
        container2.pack()
        lbl1 = Label(container2, text='Name')
        lbl1.pack(padx=25,side=LEFT)
        entry1 = Entry(container2,width=25)
        entry1.pack(side=RIGHT)

        # ----- address -----   
        container3 = Frame(win,pady=0)
        container3.pack()
        lbl2 = Label(container3,text='Address')
        lbl2.pack(padx=25,side=LEFT)
        entry2 = Entry(container3,width=25)
        entry2.pack(side=RIGHT)

        # ----- type dropdown ------
        container4 = Frame(win,pady=0)
        container4.pack()
        lbl3 = Label(container4,text='Type')
        lbl3.pack(side=LEFT,pady=5)
        type = StringVar(master)
        type.set(options[0])
            #typeChooser = OptionMenu(container4,type,*options)
        typeChooser = ttk.Combobox(container4,state='readonly',values=options,textvariable=type)
        typeChooser.pack(side=RIGHT)
        #----- salary ------
        salarycontainer = Frame(win,pady=0)
        salarytxt   = Label(salarycontainer,text='Salary')
        salaryentry = Entry(salarycontainer)
        salaryentry.pack(side=RIGHT)
        salarycontainer.pack()
        salarytxt.pack(side=LEFT)
        
        # ------ comission or not ------
        container5 = Frame(win,pady=0)
        lbl4=Label(container5,text='Comission')
        entry4=Entry(container5,width=25)
        type.trace_add('write',lambda arg1=container5,arg2=lbl4,arg3=entry4,arg4=type:showComission(container5,lbl4,entry4,type))

        data = {'salary': salaryentry.get(),'name':entry1.get(), 'address':entry2.get(), 'comission':entry4.get(),'type': type.get()}
        
        # ----- log ------
        #TODO #1 create a way to make the user see the new employee ID.
        # separator = ttk.Separator(win,orient=HORIZONTAL)
        # separator.pack()
        # dataframe = Frame(win,pady=0)
        # datatxt = Label(win,text=f'{data}')
        # dataframe.pack()
        # datatxt.pack()
        # ----- exit ------
        exitButtonContainer = Frame(master,pady=5,borderwidth=1)
        exitButtonContainer.pack(side=BOTTOM,fill=X)
        btnExit = Button(exitButtonContainer,text='Back',command=win.destroy)
        btnExit.pack(side=LEFT)
        menu.wm_deiconify()

        # ----- submit -----
        btnSubmit = Button(exitButtonContainer, text='Submit',command=lambda arg1=win,arg2=data: submit(win,data))
        btnSubmit.pack(side=RIGHT)
        menu.wm_deiconify()

    def rmvEmployee(self):
        win = Toplevel(menu)
        master = win
        win.title("Remove Employee")
        win.geometry('300x150')
        win.resizable(False,False)


        titleContainer = Frame(win)
        titleContainer.pack()
        title = Label(titleContainer,text='Insert employee ID',font=('Arial','11','bold'))
        title.pack()
        idTxt = Frame(win)
        _id = Entry(idTxt)
        idTxt.pack(pady=5)
        _id.pack()

        exitButtonContainer = Frame(master,pady=5,borderwidth=1)
        exitButtonContainer.pack(side=BOTTOM,fill=X)
        btnExit = Button(exitButtonContainer,text='Back',command=win.destroy)
        btnExit.pack(side=LEFT)
        menu.wm_deiconify()

        #TODO #2 show who has been removed
        # ----- submit -----
        btnSubmit = Button(exitButtonContainer, text='Remove',command=lambda arg1=_id.get(): employeeRemover(id))
        btnSubmit.pack(side=RIGHT)
        pass
    
    def changeEmployee(self):
        win = Toplevel(menu)
        master = win
        win.title("Change Employee")
        win.resizable(False,False)
        
        #title + idsearch
        titleContainer = Frame(win)
        titleContainer.pack()
        title = Label(titleContainer,text='Insert employee ID',font=('Arial','11','bold'))
        title.pack()
        idTxt = Frame(win)
        _id = Entry(idTxt)
        idTxt.pack()
        _id.pack()






        exitButtonContainer = Frame(master,pady=5,borderwidth=1)
        exitButtonContainer.pack(side=BOTTOM,fill=X)
        btnExit = Button(exitButtonContainer,text='Back',command=win.destroy)
        btnExit.pack(side=LEFT)
        menu.wm_deiconify()

        #TODO #3 show what has been changed
        # ----- submit -----
        btnSubmit = Button(exitButtonContainer, text='Remove',command=lambda arg1=_id.get(): employeeChanger(id))
        btnSubmit.pack(side=RIGHT)
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

menu = Tk()
app = Menu(menu)
menu.title("Payroll System")
menu.geometry('340x620+40+40')
#print(a)
menu.resizable(False,True)
menu.mainloop()