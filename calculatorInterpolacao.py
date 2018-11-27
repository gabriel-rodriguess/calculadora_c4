import tkinter as tk
import numpy
import math



class initCalcInterpolacao():
    #creates a top level entity following configures below
    def __init__(self,k):
        #print(k)
        self.window2=tk.Toplevel(k)
        self.window2.focus_force()
        self.visor=tk.Label(self.window2,text="X",bg="light cyan",
                            fg="black", font=("Arial",15))
        self.visor1=tk.Label(self.window2,text="X",bg="light cyan",
                            fg="black", font=("Arial",15))
        self.visor2=tk.Label(self.window2,text="Y",bg="light cyan",
                                        fg="black", font=("Arial",15))
        self.botoes=[]

    def start(self,num):
        self.window2.geometry("300x440")
        self.window2.minsize(300,440)

        for i in range (num+2):
            tk.Grid.rowconfigure(self.window2, i, weight=1)
        for i in range (2):
            tk.Grid.columnconfigure(self.window2, i, weight=1)

        #visor
        self.visor.grid(row=0,columnspan=2,sticky=tk.N+tk.S+tk.E+tk.W)
        self.visor1.grid(row=1,column=0,sticky=tk.N+tk.S+tk.E+tk.W)
        self.visor2.grid(row=1,column=1,sticky=tk.N+tk.S+tk.E+tk.W)
        #cria botoes
        for i in range (num):
            self.botoes.append([])
            for j in range (2):
                self.botoes[i].append(tk.Entry(self.window2,font=("Arial",10)))
                self.botoes[i][j].grid(row=(i+2),column=(j),
                                       sticky=tk.N+tk.S+tk.E+tk.W)
        self.botoes.append([])
        self.botoes[num].append(tk.Button(self.window2,
                                        text="Calcular a equação",
                                        font=("Arial",10)))
        self.botoes[num][0].grid(row=(num+2),columnspan=2,
                               sticky=tk.N+tk.S+tk.E+tk.W)

        self.botoes[num][0].configure(command=metodoInterpolacao())

    def metodoInterpolacao():
        pass
