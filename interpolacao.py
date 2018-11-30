import tkinter as tk
import numpy
import math
import calculatorInterpolacao as cI


class initInterpolacao():
    #creates a top level entity following configures below
    def __init__(self,k):
        #print(k)
        self.window2=tk.Toplevel(k)
        self.visor=tk.Label(self.window2,text="Digite quantos pontos ira inserir: ",bg="light cyan",
                            fg="black", font=("Arial",15))
        self.input=tk.Entry(self.window2,text="",bg="light cyan",
                            fg="black", font=("Arial",15),width=5)
        self.botoes=[]

    def start(self):
        textButtonsT01 = {
            "00":"Interpolação 1",
            "01":"Interpolação 2",
            "02":"Interpolação 3",
        }

        functionButtonsT01 = {
            "00":lambda:self.calculator(1),
            "01":lambda:self.calculator(2),
            "02":lambda:self.calculator(3),
        }

        self.window2.geometry("430x240")
        self.window2.minsize(430,240)

        for i in range (2):
            k=0
            if(i==0):
                k=1
            else:
                k=3
            tk.Grid.rowconfigure(self.window2, i, weight=k)
        for i in range (3):
            tk.Grid.columnconfigure(self.window2, i, weight=1)

        #visor
        self.visor.grid(row=0,columnspan=2,sticky=tk.N+tk.S+tk.E+tk.W)
        self.input.grid(row=0,column=2,sticky=tk.N+tk.S+tk.E+tk.W)
        #cria botoes
        for i in range (1):
            self.botoes.append([])
            for j in range (3):
                self.botoes[i].append(tk.Button(self.window2,
                                                text=textButtonsT01[str(i)+str(j)],
                                                font=("Arial",10)))
                self.botoes[i][j].grid(row=(i+1),column=(j),
                                       sticky=tk.N+tk.S+tk.E+tk.W)
        #atribui funcoes
        for i in range (1):
            for j in range (3):
                self.botoes[i][j].configure(command=functionButtonsT01[str(i)+str(j)])


    def calculator(self,metodo):
        pontos = int(self.input.get())
        t=cI.initCalcInterpolacao(self.window2)
        t.start(pontos,metodo)
