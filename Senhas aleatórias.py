from tkinter import  *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop()
    def tela(self):
        self.root.title('Gerador de Senhas!!')
        self.root.configure(background='#FFDEAD')

Application()