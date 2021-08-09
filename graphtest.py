from tkinter import *
from tkinter import ttk 
import datetime
import time
class App:
    def __init__(self, master=None):
        self.defaultFont = ("Arial", "10")
        self.firstContainer = Frame(master)
        self.firstContainer["pady"] = 10 #desce em 10(px?)
        self.firstContainer.pack()

        self.secondContainer = Frame(master)
        self.secondContainer["padx"] = 20
        self.secondContainer.pack()

        self.thirdContainer = Frame(master)
        self.thirdContainer["padx"] = 20
        self.thirdContainer.pack()
        
        self.fourthContainer = Frame(master)
        self.fourthContainer['pady'] = 20
        self.fourthContainer.pack()

        self.fifthContainer = Frame(master)
        self.fifthContainer.pack()

        self.title = Label(self.firstContainer, text="Dados do Novo Empregado",font=self.defaultFont)
        self.title['font'] = ("Arial",'10','bold')
        self.title.pack()

        self.nameLabel = Label(self.secondContainer,text ='Nome',font=self.defaultFont)
        self.nameLabel.pack(side=LEFT)
        
        self.name = Entry(self.secondContainer)
        self.name['width'] = 30
        self.name['font'] = self.defaultFont
        self.name.pack(side=RIGHT)

        self.addressLabel = Label(self.thirdContainer, text='Endereço', font=self.defaultFont)
        self.addressLabel.pack(side=LEFT)
        
        self.address = Entry(self.thirdContainer)
        self.address['width'] = 30
        self.address['font'] = self.defaultFont
        self.address.pack(side=RIGHT)
        
        self.btnAddEmployee = Button(self.fourthContainer)
        self.btnAddEmployee['text'] = 'Adicionar Empregado'
        self.btnAddEmployee['font'] = ("Calibri","8")
        self.btnAddEmployee['width'] = 20
        self.btnAddEmployee['command'] = self.addEmployee
        self.btnAddEmployee.pack()

        self.msg = Label(self.fourthContainer,text='',font=self.defaultFont)
        self.msg.pack()

        self.btnCancel = Button(self.fifthContainer, command=self.clearWindow, text='Cancelar',foreground='red')
        self.btnCancel.pack(side=RIGHT, padx=20)
        
    def clearWindow(self):
        #self.
        pass
    def addEmployee(self):
        name = self.name.get()
        address = self.address.get()
        if not name == '':
            self.msg['text'] = f'{name}, {address}'
        else:
            self.msg['text'] = 'Dados inválidos.'

class DigitalClock(Toplevel):
    def __init__(self,master):
        super().__init__(master)

        # configure the root window
        self.title('Digital Clock')
        self.resizable(0, 0)
        self.geometry('250x80')
        self['bg'] = 'black'

        # change the background color to black
        self.style = ttk.Style(self)
        self.style.configure(
            'TLabel',
            background='black',
            foreground='red')

        # label
        self.label = ttk.Label(
            self,
            text=self.time_string(),
            font=('Digital-7', 40))

        self.label.pack(expand=True)

        # schedule an update every 1 second
        self.label.after(1000, self.update)

    def time_string(self):
        return time.strftime('%H:%M:%S')

    def update(self):
        """ update the label every 1 second """

        self.label.configure(text=self.time_string())

        # schedule another timer
        self.label.after(1000, self.update)


root = Tk()
root.title("Folha de Pagamento")
root.geometry("320x210")
App(root)
clock = DigitalClock(root)
root.mainloop()