from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
from idlelib.tooltip import Hovertip

class Form(object):
    def __init__(self, title:str, size:str):
        self.base = Tk()
        self.base.geometry(size)    # example: '500x320'
        self.base.title(title)
    
    def ExtendForm(self):
        pass

class FileSelectorForm(Form):
    def __init__(self, title:str):
        super().__init__(title, "380x100")
        self.file_name = StringVar()

        self.label_subtitle = Label(master=self.base, text="Selecciona el archivo a procesar", width=26, font=("Calibri", 15, "normal"))
        self.label_subtitle.place(x=5, y=0)

        self.entry_file_name = Entry(master=self.base, width=60)
        self.entry_file_name.place(x=10, y=40)

        self.button_file_name = Button(self.base, text='Seleccionar', width=15, bg='#0d6efd', fg='white')
        self.button_file_name.config(command=self.GetFileName)
        self.button_file_name.place(x=10, y=70)

        self.button_process = Button(self.base, text='Procesar', width=15, bg='#198754', fg='white')
        self.button_process.config(command = self.Process)
        self.button_process.place(x=130, y=70)

        self.button_close = Button(self.base, text='Cerrar', width=15, bg="#dc3545", fg='white')
        self.button_close.config(command=self.base.destroy)
        self.button_close.place(x=250, y=70)

        self.base.mainloop()
    
    def Process(self):
        print(self.entry_file_name.get())
    
    def GetFileName(self):
        self.file_name = fd.askopenfilename()
        self.entry_file_name.delete(0, len(self.entry_file_name.get()))
        self.entry_file_name.insert(0, self.file_name.split('/')[::-1][0])
form = FileSelectorForm("Prueba")
