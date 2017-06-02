'''#!/usr/bin/env python
import Tkinter as tk
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(row=2, column=1)
        self.createWidgets()
    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',command=self.quit)
        self.quitButton.grid()

app = Application()
app.master.title('Sample application')
app.mainloop()'''
from easygui import *
from numpy import zeros
import sys, os
from time import sleep

mat1 = None
mat2 = None
valorMostrar = None
suma = None
tituloProg = 'Generador de matrices'
def mostrar():
    global valorMostrar
    choices = [ "Matriz 1",
                "Matriz 2"]
    msg ="Elige una matriz"
    choice = choicebox(msg, tituloProg, choices)
    if choice == 'Matriz 1':
        valorMostrar = 1
    elif choice == 'Matriz 2':
        valorMostrar = 2
def cambiarValores(matriz):
    for j in range(len(matriz)):
        for k in range(len(matriz[j])):
            valor = '\n Usted se encuentra en la posicion {0}, {1} que valor desea: '.format((j+1),(k+1))
            matriz[j][k]= float(enterbox(valor,tituloProg))
def crearMatriz():
    global mat1
    global mat2
    if mat1 is not None:
        if mat2 is not None:
            msgbox('Ya alcanzo el maximo de matrices que puede crear que es 2',tituloProg)
        elif mat2 is None:
            filas = int(enterbox('Cuantas filas desea que tenga la matriz',tituloProg))
            col = int(enterbox('Cuantas columnas desea que tenga la matriz',tituloProg))
            mat2 = zeros((filas,col))
            msgbox('Matriz creada exitosamente',tituloProg)
    elif mat1 is None:
        filas = int(enterbox('Cuantas filas desea que tenga la matriz',tituloProg))
        col = int(enterbox('Cuantas columnas desea que tenga la matriz',tituloProg))
        mat1 = zeros((filas,col))
        msgbox('Matriz creada exitosamente',tituloProg)
def mostrarMatriz():
    global mat1
    global mat2
    if mat1 is not None and mat2 is not None:
        mostrar()
        if valorMostrar == 1:
            msgbox(mat1,tituloProg)
        elif valorMostrar == 2:
            msgbox(mat2,tituloProg)
    elif mat1 is None:
        if mat2 is None:
            msgbox('No existe ninguna matriz',tituloProg)
        elif mat2 is not None:
            msgbox(mat2,tituloProg)
    elif mat1 is not None:
        msgbox(mat1,tituloProg)
def menu():
    global choice
    msg ="Elige una opcion"
    choices = [ "Crear una matriz nula(max 2)",
                "Mostrar Contenido de la matriz",
                "Cambiar valores de una matriz",
                "Cambiar dimension de una matriz",
                "Sumar matrices",
                "Mostrar resultado de la suma" ]
    choice = choicebox(msg,tituloProg, choices)
def llenarMatriz():
    global mat1
    global mat2
    if mat1 is None and mat2 is None:
        msgbox('No existe ninguna matriz',tituloProg)
    elif mat1 is not None and mat2 is not None:
        mostrar()
        if valorMostrar == 1:
            cambiarValores(mat1)
        elif valorMostrar == 2:
            cambiarValores(mat2)
    elif mat2 is not None:
        cambiarValores(mat2)
    elif mat1 is not None:
        cambiarValores(mat1)
def cambiarDimension():
    def seguro():
        global mat1
        global mat2
        elegir = enterbox('\n Esta funcion borrara la matriz elegida y la llenara de zeros\n Desea seguir(s/n)',tituloProg)
        if elegir == 's':
            mostrar()
            if valorMostrar == 1:
                mat1 = None
                filas = int(enterbox('Cuantas filas desea que tenga la matriz',tituloProg))
                col = int(enterbox('Cuantas columnas desea que tenga la matriz',tituloProg))
                mat1 = zeros((filas,col))
                msgbox('Matriz re-dimensionada exitosamente',tituloProg)
            elif valorMostrar == 2:
                mat2 = None
                filas = int(enterbox('Cuantas filas desea que tenga la matriz',tituloProg))
                col = int(enterbox('Cuantas columnas desea que tenga la matriz',tituloProg))
                mat2 = zeros((filas,col))
                msgbox('Matriz re-dimensionada exitosamente',tituloProg)
        elif elegir == 'n':
            os.system('cls')
            pass

    if mat1 is not None:
        if mat2 is not None:
            seguro()
        elif mat2 is None:
            msgbox('Antes de usar esta funcion necesita tener creada el maximo de matrices',tituloProg)
    elif mat1 is None:
        msgbox('Antes de usar esta funcion necesita tener creada el maximo de matrices',tituloProg)
def sumarMatriz():
    global mat1
    global mat2
    global suma
    if mat1 is not None and mat2 is not None:
        for j in range(len(mat1)):#determino cuantas filas contiene la matriz
            for k in range(len(mat1[j])):#determino cuantas columnas contiene la matriz
                mat1Col = len(mat1[j])
            mat1Fil = len(mat1)
        for j in range(len(mat2)):#determino cuantas filas contiene la matriz
            for k in range(len(mat2[j])):#determino cuantas columnas contiene la matriz
                mat2Col = len(mat2[j])
            mat2Fil = len(mat2)

        if mat1Fil == mat2Fil:
            if mat1Col == mat2Col:
                suma = mat1 + mat2
                msgbox('Suma realizada',tituloProg)
        else:
            msgbox('No es posible sumar matrices de diferentes dimensiones:\n matriz 1 tiene {0} filas y {1} columnas mientras que\n matriz 2 tiene {2} filas y {3} columnas.'.format(mat1Fil,mat1Col,mat2Fil,mat2Col),tituloProg)
    else:
        msgbox('Necesita tener al menos 2 matrices creadas para poder sumar',tituloProg)
while 1:
    menu()
    if choice is None:
        os.system('cls')
        sys.exit(0)
        salir = msgbox('Saliendo del generador de matrices',tituloProg)
        time.sleep(1)
        sys.exit(0)
    elif choice[0]:
        if choice == 'Crear una matriz nula(max 2)':
            crearMatriz()
        elif choice == 'Mostrar Contenido de la matriz':
            mostrarMatriz()
        elif choice == 'Cambiar valores de una matriz':
            llenarMatriz()
        elif choice == 'Cambiar dimension de una matriz':
            cambiarDimension()
        elif choice == 'Sumar matrices':
            sumarMatriz()
        elif choice == 'Mostrar resultado de la suma':
            if suma is not None:
                msgbox(suma,'Generador de matrices')
            else:
                msgbox('Usted no ha realizado ninguna suma',tituloProg)
                
