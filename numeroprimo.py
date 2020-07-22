#Numeros primos
#Sophia Pinto


    
# Importações de bibliotecas
import tkinter as tk 
from tkinter import *

# -----------------------------------------------
# funções

def numeroprimo ():
    
    numprimo = int (textbox1.get())

    saberprimo = numprimo % 2
  
    if saberprimo ==1 :
     labelfinal ["text"] = numprimo,"é número primo."

    else:
      labelfinal ["text"] =  numprimo,"não é número primo."

#Deseja realizar a operação novamente?


# -----------------------------------------------
# GUI
root = Tk ()
root.title ("Aplicação")

# -----------------------------------------------
# widgets/ janelas
label1 = Label (root, text = "Digite um número para saber se ele é primo.")
labelfinal = Label (root, text= "Resultado:" )

textbox1 = Entry (root)

button1= Button (root, text= "Calcular", command= numeroprimo)

# -----------------------------------------------
# layout
label1.grid (row=0,column=0)
labelfinal.grid (row=3,column=0)

textbox1.grid (row=0,column=1)

button1.grid (row=5,column=1)
# -----------------------------------------------
root.mainloop ()