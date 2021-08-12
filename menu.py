import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from employee2 import *
from companySystem import *
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

def Container(master,txt):

    """Creates a Frame that holds a label and an entry.

    Is attatched to master and shows txt on the label."""

    container = Frame(master,pady=0)
    container.pack()
    lbl = Label(container, text=txt) 
    lbl.pack(padx=25,side=LEFT)
    entry = Entry(container,width=25) #input
    entry.pack(side=RIGHT)
    
    return entry

def destroyWin(self):
    quit(self)

def submit(win,name,address,type,salary,commission):
    print([name+salary+address])
    if name != '' and address !='' and salary!="":
        if type == 'commissioned':
            newemployee = Employee(name=name, salary=salary, address=address, type=type, commission=commission)
            CompanySystem.addEmployee(newemployee)
            
            employeeID = newemployee.getID()
            print(employeeID.hex)
            str = f"""
            Successfully added the new employee!
                                ID:{employeeID.hex}"""
            #send the data to the database?
            a = mb.showinfo(title='Success!',message=str)
        
        else:
            newemployee = Employee(name=name,salary=salary,address=address,type=type,commission=commission)
            CompanySystem.addEmployee(newemployee)
            
            employeeID = newemployee.getID()
            print(employeeID.hex)
            str = f"""
            Successfully added the new employee!
                                ID:{employeeID.hex}"""
            #send the data to the database?
            a = mb.showinfo(title='Success!',message=str)

    else:
        mb.showerror(title='Failure.',message='Could not create an employee. Try again, but remember to fill everything.')

def windowTitleAndSearch(master,txt) -> None:
    """Creates a Frame with a Title and a Entry to search Employee. Creates a separator too."""
    titleContainer = Frame(master)
    titleContainer.pack()
    title = Label(titleContainer,text=txt,font=('Arial','11','bold'))
    title.pack()
    idTxt = Frame(master)
    _id = Entry(idTxt)
    idTxt.pack()
    _id.pack()
    searchBtn = Button(idTxt,text='Search',command=lambda arg1=_id.get() : employeeSearcher(_id.get()))
    searchBtn.pack(side=RIGHT)
    sep = ttk.Separator(master,orient='horizontal')
    sep.pack(fill=BOTH,pady=5)

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

def employeeSearcher(master,id) -> bool:
    if id != '':
        realID = uuid.UUID(id)
        a = CompanySystem.searchEmployeeByID(realID)
        name = a.getName()
        address = a.getAddress()
        payment = a.getPayment()
        status = a.getUnionStatus()
        uID = a.getUnionID()
        commission = a.getCommission()
        uFee = a.getUnionFee()
        type = a.getType()
        #TODO #6 FIX this container and fix the change button
        container=Frame(master)
        txt1 = Label(container,text=f'Name:{name}| Address:{address} | Type: {type} | Payment: {payment} | Union Status: {status} | Union ID: {uID} | Union Fee: {uFee} | Commision: {commission}')
        container.pack(side=TOP)
        txt1.pack()
        master.update()
    else:
        mb.showerror(title='Failure.',message='Something went wrong. Maybe you forgot to fill the field?')
    pass

def employeeRemover(id) -> bool:
    if id != "":
        a = CompanySystem.removeEmployeeByID(uuid.UUID(id))
        if a != False:
            b=mb.showinfo(title='Success!',message=f'Employee with ID: {id} removed.')
        else:
            c=mb.showerror(title="Failure.",message="Employee could not be removed.")
        pass
    else:
        mb.showerror(title='Fill the ID!',message="Don't forget to fill the ID field.")

def employeeChanger(id,dictionary) -> bool:
    uuidID = uuid.UUID(id)

    pass

def showChangeable(win, list):
    
    for a in list:
        if(a):
            print(a)
class Menu(Frame):
    """ It's the class that shows the MENU."""
    def __init__(self,master=None):
        self.root = Frame.__init__(self,master)
        # ---- default settings ----
        timeNow = datetime.datetime.now()
        self.defaultFont = ("Arial", "10")
        self.titleFont = ("Arial",'10','bold')
# MENU      #######################################################################
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
        win = Toplevel(menu)
        #menu.withdraw()
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
        entry1.get()

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
        lbl4=Label(container5,text='Commission')
        entry4=Entry(container5,width=25)
        entry4.insert(END,'')
        type.trace_add('write',lambda arg1=container5,arg2=lbl4,arg3=entry4,arg4=type:showComission(container5,lbl4,entry4,type))
        
        # ----- exit ------
        exitButtonContainer = Frame(master,pady=5,borderwidth=1)
        exitButtonContainer.pack(side=BOTTOM,fill=X)
        btnExit = Button(exitButtonContainer,text='Back',command=win.destroy)
        btnExit.pack(side=LEFT)
        
        # ----- submit -----
        
        # data= {}
                                                                                                                                                                                        # data['salaryentry'] = salaryentry.get()
                                                                                                                                                                                        # data['address'] = entry2.get()
                                                                                                                                                                                        # data['type'] = type.get()
                                                                                                                                                                                        # data['name'] = entry1.get()
                                                                                                                                                                                        # data['commission'] = entry4.get()
                                                                                                                                                                                        # master.after(1000,master.update)
        
        # data = {'salary': salaryentry.get(),'name':entry1.get(), 'address':entry2.get(), 'type': type.get()}
        #btnSubmit = Button(exitButtonContainer, text='Submit',command=lambda arg1=win,arg2=data: submit(win,data))
        btnSubmit = Button(exitButtonContainer, text='Submit', command=lambda arg1=salaryentry.get(), arg2=entry2.get(),arg3=type.get(), arg4=entry1.get(),arg5=master : submit(name=entry1.get(),address=entry2.get(),type=type.get(),commission=entry4.get(),win=master,salary=salaryentry.get()))
        btnSubmit.pack(side=RIGHT)

        #'commission':entry4.get()
        # print([entry4.get()])
        # print([entry1.get()])


    def rmvEmployee(self):
        win = Toplevel(menu) #creates a new window
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
        idTxt.pack(pady=5,fill=X)
        _id.pack(fill=X,expand=TRUE,padx=5)
        print([_id.get()])

        exitButtonContainer = Frame(master,pady=5,borderwidth=1)
        exitButtonContainer.pack(side=BOTTOM,fill=X)
        btnExit = Button(exitButtonContainer,text='Back',command=win.destroy)
        btnExit.pack(side=LEFT)
        menu.wm_deiconify()

        #TODO #2 show who has been removed
        # ----- submit -----
        #btnSubmit = Button(exitButtonContainer, text='Remove',command=lambda arg1=_id.get(): employeeRemover(_id.get()))
        btnSubmit = Button(exitButtonContainer, text='Remove',command=lambda arg1=_id.get(): print(_id.get()))
        btnSubmit.pack(side=RIGHT)
        pass
    
    def changeEmployee(self):
        win = Toplevel(menu)
        master = win
        win.title("Change Employee")
        win.resizable(TRUE,False)
        
        #title + idsearch
        titleContainer = Frame(win)
        titleContainer.pack()
        title = Label(titleContainer,text=' Insert employee ID',font=('Arial','11','bold'))
        title.pack()
        idContainer = Frame(win)
        _id = Entry(idContainer)
        idContainer.pack(side=TOP)
        _id.pack(padx=5,fill=X,expand=TRUE)
        searchBtn = Button(idContainer,text='Search',command=lambda arg1 = master,arg2=_id.get() : employeeSearcher(master,_id.get()))
        searchBtn.pack(side=RIGHT)
        
        # ----- checkbar -----
            # numbers                   0      1        2           3              4             5              6
            #chk = checkbar(master,['Name','Address','Type,'Method of Payment','Union Status','Union ID','Union Fee'])
            #chk.pack()
            #chk.state()
        sep = ttk.Separator(master,orient='horizontal')
        sep.pack(fill=BOTH,pady=5)
        lbl1 = Label(master,text='Type what you want to change and leave the rest blank',font=('Arial','10','bold'))
        lbl1.pack(pady=5,padx=5)
        c1 = Container(master,'Name')
        c2 = Container(master,'Address')
        c3 = Container(master,'Type')
        c8 = Container(master,'Salary' )
        c9 = Container(master,'Commission')
        c4 = Container(master,'Payment')
        c5 = Container(master,'Union Status')
        c6 = Container(master,'Union ID')
        c7 = Container(master,'Union Fee')

        
    
        # ----- exit button ------
        exitButtonContainer = Frame(master,pady=5,borderwidth=1)
        exitButtonContainer.pack(side=BOTTOM,fill=X)
        btnExit = Button(exitButtonContainer,text='Back',command=win.destroy)
        btnExit.pack(side=LEFT)

        #TODO #3 show what has been changed
        # ----- submit -----
        
        btnSubmit = Button(exitButtonContainer, text='Change',command=lambda arg1=_id.get(): employeeChanger(_id.get()))
        btnSubmit.pack(side=RIGHT)

    def sendPoint(self):
        master = Toplevel(menu)
        master.title('Send Electronic Point Data')
        master.resizable(False,False)

        title = windowTitleAndSearch(master,'Insert ID of the employee')

        arrival = Container(master,"Arrival")
        leaving = Container(master,"Leaving")

        exitButtonContainer = Frame(master,pady=5,borderwidth=1)
        exitButtonContainer.pack(side=BOTTOM,fill=X)
        btnExit = Button(exitButtonContainer,text='Back',command=master.destroy)
        btnExit.pack(side=LEFT)

        # ----- submit -----
        #TODO #4 create a button that commands a function to send the point data
        #btnSubmit = Button(exitButtonContainer, text='Change',command=lambda arg1=_id.get(): employeeChanger(_id.get()))
        #btnSubmit.pack(side=RIGHT)
        pass
    
    def sendSale(self):
        master = Toplevel(menu)
        master.title('Send Sale Data')
        master.resizable(False,False)

        title = windowTitleAndSearch(master,'Insert ID of the employee')

        sale = Container(master,"Sale Price")

        exitButtonContainer = Frame(master,pady=5,borderwidth=1)
        exitButtonContainer.pack(side=BOTTOM,fill=X)
        btnExit = Button(exitButtonContainer,text='Back',command=master.destroy)
        btnExit.pack(side=LEFT)

        # ----- submit -----
        #TODO config submit button
        #btnSubmit = Button(exitButtonContainer, text='Change',command=lambda arg1=_id.get(): employeeChanger(_id.get()))
        #btnSubmit.pack(side=RIGHT)
    
    def sendTax(self):
        master = Toplevel(menu)
        master.title('Send Union Service Fee')
        master.resizable(False,False)

        title = windowTitleAndSearch(master,'Insert ID of the employee')

        sale = Container(master,"Fee")

        exitButtonContainer = Frame(master,pady=5,borderwidth=1)
        exitButtonContainer.pack(side=BOTTOM,fill=X)
        btnExit = Button(exitButtonContainer,text='Back',command=master.destroy)
        btnExit.pack(side=LEFT)

        # ----- submit -----
        #TODO config submit button
        #btnSubmit = Button(exitButtonContainer, text='Change',command=lambda arg1=_id.get(): employeeChanger(_id.get()))
        #btnSubmit.pack(side=RIGHT)
    
    def changePayday(self):
        master = Toplevel(menu)
        master.title('Change Payday')
        master.resizable(False,False)
        master.geometry('300x250+30+30')

        title = windowTitleAndSearch(master,'Insert ID of the employee')

        container4 = Frame(master)
        container4.pack()
        #TODO #5 add new options dinamically using some sort of database
        options = ['Weekly','Monthly','Bi-Weekly']
        payday = StringVar()
        payday.set(options[0])
        paydayChooser = ttk.Combobox(container4,state='readonly',values=options,textvariable=payday)
        paydayChooser.pack(side=RIGHT)

        exitButtonContainer = Frame(master,pady=5,borderwidth=1)
        exitButtonContainer.pack(side=BOTTOM,fill=X)
        btnExit = Button(exitButtonContainer,text='Back',command=master.destroy)
        btnExit.pack(side=LEFT)

        # ----- submit -----
        #todo config submit button
        #btnSubmit = Button(exitButtonContainer, text='Change',command=lambda arg1=_id.get(): employeeChanger(_id.get()))
        #btnSubmit.pack(side=RIGHT)pass

    def createPayday(self):
        master = Toplevel(menu)
        master.title('Create Payday')
        master.resizable(False,False)

        title = windowTitleAndSearch(master,'Insert ID of the employee')

        sale = Container(master,"New Payday")

        exitButtonContainer = Frame(master,pady=5,borderwidth=1)
        exitButtonContainer.pack(side=BOTTOM,fill=X)
        btnExit = Button(exitButtonContainer,text='Back',command=master.destroy)
        btnExit.pack(side=LEFT)

        # ----- submit -----
        #todo config submit button
        #btnSubmit = Button(exitButtonContainer, text='Change',command=lambda arg1=_id.get(): employeeChanger(_id.get()))
        #btnSubmit.pack(side=RIGHT)

    def runPayroll(self):
        master = Toplevel(menu)
        master.title('Make Payments')
        master.resizable(False,False)

        container1 = Frame(master)
        lbl1 = Label(master,text='Here are the employees that are to recieve today:')
        container1.pack()
        lbl1.pack()

        

        exitButtonContainer = Frame(master,pady=5,borderwidth=1)
        exitButtonContainer.pack(side=BOTTOM,fill=X)
        btnExit = Button(exitButtonContainer,text='Back',command=master.destroy)
        btnExit.pack(side=LEFT)

        # ----- submit -----
        #todo config submit button
        #btnSubmit = Button(exitButtonContainer, text='Change',command=lambda arg1=_id.get(): employeeChanger(_id.get()))
        #btnSubmit.pack(side=RIGHT)

menu = Tk()
app = Menu(menu)
menu.title("Payroll System")
menu.geometry('340x620+600+40')
#print(a)
menu.resizable(False,True)
menu.mainloop()