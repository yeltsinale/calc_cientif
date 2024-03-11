from tkinter import *
import math
import tkinter.messagebox

root = Tk()
root.title("Calculadora Científica")
root.resizable(width=False, height=False)
root.geometry("400x492+460+40")

#frame -> marco contenedor
MainFrame = Frame(root, bd=20, pady = 2 , relief = RIDGE).grid()
#grid rejilla

calc = Frame(MainFrame, bd=20, pady = 2 , relief = RIDGE)
calc.grid()

menubar = Menu(calc)
#tearoff -> abre otra ventan
filemenu = Menu(menubar, tearoff= 0)
menubar.add_cascade(label = "Archivo", menu =filemenu)
filemenu.add_command(label = "Standard")
filemenu.add_separator()
filemenu.add_command(label = "Científica")
filemenu.add_separator()
filemenu.add_command(label = "Salir")

root.config(menu = menubar)
root.mainloop()




