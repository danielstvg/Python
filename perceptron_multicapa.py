from random import uniform
import random
import math
import numpy as np
from tkinter import *
from tkinter import messagebox

class Propagacion:

    def __init__(self):
        self.matriz = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]] 
        print(self.matriz)
        self.filas = 8
        self.columnas =3
        self.salida_deseada = []
        

    #print("Digite raw_input calores de la matriz 8x3");   
    '''for f in range(filas):
        for c in range(columnas):
        #matriz[f][c] = int(input("Elemento %d, %d : " % (f,c)))
        print("")'''
    def matriz(self):
        return self.matriz
    
    def llenar(self, salida_deseada):
        self.message = "Se lleno el arreglo"
        self.salida_deseada = salida_deseada
        print(self.salida_deseada)
        return self.salida_deseada
        
    def entrenar(self):
        self.txt = ' '
        if (len(self.salida_deseada) != 8):
            self.txt = 'nn'
            return self.txt
        #print("Ingrese la salida deseada")
        #salida_deseada = [];
        #cantidad = 8
        #for x in range(cantidad):
        #    dato = int(input("Elemento %d: " % (x)))
        #salida_deseada.append(dato)
        #salida_deseada = [1,1,1,1,1,1,0,1];
        salida_modelo=0
        pat = 0
        w0 = random.uniform(0.1, 2.0)
        w1 = random.uniform(0.1, 2.0)
        w2 = random.uniform(0.1, 2.0)
        w3 = random.uniform(0.1, 2.0)
        patron = [0]*8 #double
        suma_datos = 0
        for i in range(self.filas):
            pat=0
            for j in range(self.columnas):
                if j == 0:
                    patron[i] = w1 * self.matriz[i][j]
                    pat=pat+patron[i]
                else:
                    patron[i] = w2* self.matriz[i][j]
                    pat=pat+patron[i]
                    
                    patron[i] = w3* self.matriz[i][j]
                    pat=pat+patron[i]
            
                pat=pat+w0*1
                self.txt += "\nProcesamos el patron= " + str(i) + '\n'
                self.txt += "F(w0*x0 + w1*x1 + w2+x2 + w3*x3): " + str(pat) +'\n'
                #dato = input()
            
                if pat >= 0:
                    salida_modelo=1
                else:
                    salida_modelo=0
                self.txt += "Salida deseada = " + str(self.salida_deseada[i]) +'\n'
                self.txt += "Salida modelo = " + str(salida_modelo) +'\n'
            

                if ((self.salida_deseada[i] - salida_modelo )== 0):
                    suma_datos=suma_datos+1
                else:
                    self.txt +="Como son diferentes se actualizan los pesos" +'\n'
                    w0 = w0 +(self.salida_deseada[i] - salida_modelo)*1
                    self.txt +="Wo()= " + str(w0)+'\n'
            
                    for g in range(3):
                        if g==0:
                            w1=w1+(self.salida_deseada[i] - salida_modelo)* self.matriz[i][g]
                            self.txt += "W1(t+1)= " + str(w1)+'\n'
                        else:
                            w2=w2+(self.salida_deseada[i] - salida_modelo)* self.matriz[i][g];  
                            self.txt += "W2(t+1)= " + str(w2)+'\n'
                            
                            w3=w3+(self.salida_deseada[i] - salida_modelo)* self.matriz[i][g];  
                            self.txt += "W3(t+1)= " + str(w3)+'\n'
                      
        while(suma_datos <= 3):
            self.txt += "Wo()= " + str(w0)+'\n'
            self.txt += "W1()= " + str(w1)+'\n'
            self.txt += "W2()= " + str(w2)+'\n'
            self.txt += "W3()= " + str(w2)+'\n'

        return self.txt

        


class View():
        
    def __init__(self):
        p = Propagacion()
        raiz = Tk()
        raiz.title('Perceptrón multicapa')
        raiz.resizable(0,0)

        ventana = Frame(raiz,width='700',height='300')
        ventana.pack()

        consola = Text(ventana, width='70',height='30')
        consola.grid(row=2, column=1, padx=10, pady=10)

        consola.insert(INSERT, 'Matriz de entrada: \n')
        consola.insert(INSERT, p.matriz)

        scroll = Scrollbar(ventana, command=consola.yview)
        scroll.grid(row=2, column=2, sticky='nsew')

        opcion = Frame(ventana,width='600', height='80')
        opcion.grid(row=3, column=1, padx=10, pady=10)
        opcion.config(bg='grey')
        opcion.config(bd=2)
        opcion.config(relief='groove')
        opcion.config(cursor='hand2')

        def data():
            def result():
                x1 = dato1.get()
                x2 = dato2.get()
                x3 = dato3.get()
                x4 = dato4.get()
                x5 = dato5.get()
                x6 = dato6.get()
                x7 = dato7.get()
                x8 = dato8.get()
                datos.destroy()
                message = p.llenar([int(x1),int(x2),int(x3),int(x4),int(x5),int(x6),int(x7),int(x8)])
                messagebox.showinfo(message='Se agregaron los datos', title="Información")
                consola.insert(INSERT, '\n')
                consola.insert(INSERT, '\nArreglo insertado: \n')
                consola.insert(INSERT, message)
                consola.insert(INSERT, '\n')                             
                

            datos = Tk()
            datos.title('Datos salida')
            datos.resizable(0,0)
            
            lbl1 = Label(datos, text='Inserte dato 1:')
            dato1 = Entry(datos, width=30)
            lbl2 = Label(datos, text='Inserte dato 2:')
            dato2 = Entry(datos, width=30)

            lbl3 = Label(datos, text='Inserte dato 3:')
            dato3 = Entry(datos, width=30)
            lbl4= Label(datos, text='Inserte dato 4:')
            dato4 = Entry(datos, width=30)

            lbl5 = Label(datos, text='Inserte dato 5:')
            dato5 = Entry(datos, width=30)
            lbl6 = Label(datos, text='Inserte dato 6:')
            dato6 = Entry(datos, width=30)

            lbl7 = Label(datos, text='Inserte dato 7:')
            dato7 = Entry(datos, width=30)
            lbl8 = Label(datos, text='Inserte dato 8:')
            dato8 = Entry(datos, width=30)

            btn = Button(datos, text='Aceptar', command=result)

            
            
            lbl1.grid(row=1, column=0)
            dato1.grid(row=1, column=1)
            lbl2.grid(row=2, column=0)
            dato2.grid(row=2, column=1)
            lbl3.grid(row=3, column=0)
            dato3.grid(row=3, column=1)
            lbl4.grid(row=4, column=0)
            dato4.grid(row=4, column=1)
            lbl5.grid(row=5, column=0)
            dato5.grid(row=5, column=1)
            lbl6.grid(row=6, column=0)
            dato6.grid(row=6, column=1)
            lbl7.grid(row=7, column=0)
            dato7.grid(row=7, column=1)
            lbl8.grid(row=8, column=0)
            dato8.grid(row=8, column=1)
            btn.grid(row=9,column=0, columnspan=2)

            datos.mainloop()
    	    
        btndatos = Button(opcion, text='Salidas', command=data)
        btndatos.place(x=80,y=30)
            
        def run():
            txt = p.entrenar()
            if(txt == 'nn'):
                 messagebox.showinfo(message="Inserte la salida deseada", title="ERROR")
            else:
                consola.insert(INSERT, txt)
                messagebox.showinfo(message="Ya se entreno el perceptron", title="Información")
                        
        btndatos = Button(opcion, text='Entrenar', command=run)
        btndatos.place(x=238,y=30)

        def info():
            messagebox.showinfo(message='Nombre: \nDaniel Steven Vargas.'+'\n'+'Valentina Velandia.'+'\n'+'Camilo Novoa.', title="Big Data")

        btninformacion = Button(opcion, text='Info', command=info)
        btninformacion.place(x= 385, y=30)

        raiz.mainloop()
    

            

def main():
    vi = View()

if __name__ == '__main__':
    main()
