import tkinter as tk
import numpy
import math
import integralMethods2nd as i2nd

class integralmethodchosen():
    #creates a top level entity following configures below
    def __init__(self,k):
        self.window2=tk.Toplevel(k)
        self.visor=tk.Label(self.window2,text="Escolha o método numérico para calcular a integral",bg="light cyan",
                       fg="black", font=("Arial 15 bold"))
        self.t=i2nd.integralSolver()
        self.botoes=[]
    def start(self):
        textButtonT01 = {
            "00":"Trapezio",
            "01":"Simpson",
        }
        functionButtonsT01 = {
            "00":lambda:self.t.insideTopLevel(int(0),self.window2),
            "01":lambda:self.t.insideTopLevel(int(1),self.window2),
        }
        #grid
        self.window2.geometry("640x360")
        self.window2.minsize(640,360)
        for i in range (2):
            if(i==0):
                k=1
            else:
                k=2
            tk.Grid.rowconfigure(self.window2, i, weight=1)
        for i in range (2):
            tk.Grid.columnconfigure(self.window2, i, weight=1)
        #visor
        self.visor.grid(row=0,columnspan=3,sticky=tk.N+tk.S+tk.E+tk.W)
        #cria botoes
        for i in range (1):
            self.botoes.append([])
            for j in range (2):
                self.botoes[i].append(tk.Button(self.window2,
                                                text=textButtonT01[str(i)+str(j)],
                                                font=("Arial 15 bold")))
                self.botoes[i][j].grid(row=(i+1),column=(j),
                                       sticky=tk.N+tk.S+tk.E+tk.W)
        #atribui funcoes
        for i in range (1):
            for j in range (2):
                self.botoes[i][j].configure(command=functionButtonsT01[str(i)+str(j)])
