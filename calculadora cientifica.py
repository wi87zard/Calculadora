"""para importar una libreria que se llama tkinter para 
trabajar python de forma grafica"""

import tkinter as tk
from tkinter import ttk
import math

#Crear la ventana de la aplicación
ventana = tk.Tk()
ventana.title('Calculadora Cientifica')
ventana.geometry('320x400')
ventana.configure(background='#ececec') # Fondo gris claro
ventana.resizable(False, False) # Es para evitar redimensionar la ventana.

# Crear la entrada de los valores
entrada = tk.Entry(ventana, width = 15, font=('Arial', 24), justify = tk.RIGHT)
entrada.grid(column= 0 , row= 0, columnspan= 5, pady= 10, padx= 10, sticky= 'nsew')

# Funcion para actualizar la entrada
def actualizar_entrada(texto):
    entrada.insert(tk.END, texto)
    
# Funsion para evaluar la expresión
def evaluar():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")
        
# Funsion para limpiar la entrada
def limpiar():
    entrada.delete(0, tk.END)
    
# Crear las funsiones de la calculadora

    # sqrt en la funcion para la raiz cuadrada
def raiz_cuadrada():
    try:
        num = float(entrada.get())
        resultado = math.sqrt(num)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except ValueError:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")

    # ** es la funcion para la potenciacion
def potenciacion():
    actualizar_entrada = ('**')
    
    # log10 "Este es base 10 " es la funcion para logaritmo
def logaritmo():
    try:
        num = float(entrada.get())
        resultado = math.log10(num)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except ValueError:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")
    except ZeroDivisionError:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error: Logaritmo de 0")
        
    # sin es la funcion seno
def seno():
    try:
        num = float(entrada.get())
        resultado = math.sin(math.radians(num))
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except ValueError:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")

        
    # cos es la funcion coseno
def coseno():
    try:
        num = float(entrada.get())
        resultado = math.cos(math.radians(num))
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except ValueError:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")
        
    # tan es la funcion tangente
def tangente():
    try:
        num = float(entrada.get())
        resultado = math.tan(math.radians(num))
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except ValueError:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error")
    except ZeroDivisionError:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Error: Tangente de 90 grados")
        
# Crear los botones de la calculadora
 # Primera fila
boton_7 = ttk.Button(ventana, text= '7', command= lambda: actualizar_entrada('7'))
boton_7.grid(column= 0, row= 1, sticky= 'nsew')

boton_8 = ttk.Button(ventana, text= '8', command= lambda: actualizar_entrada('8'))
boton_8.grid(column= 1, row= 1, sticky= 'nsew')

boton_9 = ttk.Button(ventana, text= '9', command= lambda: actualizar_entrada('9'))
boton_9.grid(column= 2, row= 1, sticky= 'nsew')

boton_div = ttk.Button(ventana, text= '/', command= lambda: actualizar_entrada('/'))
boton_div.grid(column= 3, row= 1, sticky= 'nsew')

 # Segunfa fila
boton_4 = ttk.Button(ventana, text= '4', command= lambda: actualizar_entrada('4'))
boton_4.grid(column= 0, row= 2, sticky= 'nsew')

boton_5 = ttk.Button(ventana, text= '5', command= lambda: actualizar_entrada('5'))
boton_5.grid(column= 1, row= 2, sticky= 'nsew')

boton_6 = ttk.Button(ventana, text= '6', command= lambda: actualizar_entrada('6'))
boton_6.grid(column= 2, row= 2, sticky= 'nsew')

boton_por = ttk.Button(ventana, text= '*', command= lambda: actualizar_entrada('*'))
boton_por.grid(column= 3, row= 2, sticky= 'nsew')

 # Tercera fila
boton_1 = ttk.Button(ventana, text= '1', command= lambda: actualizar_entrada('1'))
boton_1.grid(column= 0, row= 3, sticky= 'nsew')

boton_2 = ttk.Button(ventana, text= '2', command= lambda: actualizar_entrada('2'))
boton_2.grid(column= 1, row= 3, sticky= 'nsew')

boton_3 = ttk.Button(ventana, text= '3', command= lambda: actualizar_entrada('3'))
boton_3.grid(column= 2, row= 3, sticky= 'nsew')

boton_menos = ttk.Button(ventana, text= '-', command= lambda: actualizar_entrada('-'))
boton_menos.grid(column= 3, row= 3, sticky= 'nsew')


 # Cuarta fila
boton_0 = ttk.Button(ventana, text= '0', command= lambda: actualizar_entrada('0'))
boton_0.grid(column= 0, row= 4, columnspan= 2, sticky= 'nsew')

boton_punto = ttk.Button(ventana, text= '.', command= lambda: actualizar_entrada('.'))
boton_punto.grid(column= 2, row= 4, sticky= 'nsew')

boton_mas = ttk.Button(ventana, text= '+', command= lambda: actualizar_entrada('+'))
boton_mas.grid(column= 3, row= 4, sticky= 'nsew')


# Quinta fila
boton_igual = ttk.Button(ventana, text= '=', command= evaluar)
boton_igual.grid(column= 0, row= 5, columnspan= 4, sticky= 'nsew')

boton_limpiar = ttk.Button(ventana, text= 'C', command= limpiar)
boton_limpiar.grid(column= 0, row= 6, columnspan= 4, sticky= 'nsew')


 # Sexta fila Botones para calculadora cientifica
boton_raiz = ttk.Button(ventana, text= '√', command= raiz_cuadrada)
boton_raiz.grid(column= 4, row= 1, sticky= 'nsew')

boton_potencia = ttk.Button(ventana, text= '^', command= potenciacion)
boton_potencia.grid(column= 4, row= 2, sticky= 'nsew')

boton_log = ttk.Button(ventana, text= 'lg', command= logaritmo)
boton_log.grid(column= 4, row= 3, sticky= 'nsew')

boton_seno = ttk.Button(ventana, text= 'sin', command= seno)
boton_seno.grid(column= 4, row= 4, sticky= 'nsew')

boton_coseno = ttk.Button(ventana, text= 'cos', command= coseno)
boton_coseno.grid(column= 4, row= 5, sticky= 'nsew')

boton_tangente = ttk.Button(ventana, text= 'tan', command= tangente)
boton_tangente.grid(column= 4, row= 6, sticky= 'nsew')


 # Ajustar las los tamaños de las filas y columnas de los botones
for i in range (4):
    ventana.columnconfigure(i, weight= 1)
ventana.columnconfigure(4, weight= 1) # Este para las columnas de las trigonometricas

for i in range (7):
    ventana.rowconfigure(i, weight= 1)
ventana.rowconfigure(i, weight= 1)

ventana.mainloop()