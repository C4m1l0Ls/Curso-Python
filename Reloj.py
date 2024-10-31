from tkinter import *
from time import strftime

root = Tk()
root.title("Reloj")

# funcion para actualizar hora 
def time ():
    string = strftime ("%H:%M:%S %p")
    Label.config (text=string)
    Label.after(1000, time)
# mostrar Hora 
Label = Label(root,
              font=("arial",40),
              background="black",
              foreground= "red")
Label.pack(anchor="center")

time() # inicar reloj

root.mainloop()

