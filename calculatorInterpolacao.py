import tkinter as tk
import numpy
import math
import CN_TC_5_pt1ex1 as Polinomial
import CN_TC_5_pt1ex3 as Lagrange
import CN_TC_5_pt1ex5 as Newton
import matplotlib.pyplot as plt


class initCalcInterpolacao():
    #creates a top level entity following configures below
    def __init__(self,k):
        #print(k)
        self.window2=tk.Toplevel(k)
        self.window2.focus_force()
        self.equacao=tk.Entry(self.window2,text="",bg="light cyan",
                            fg="black", font=("Arial",12),justify=tk.CENTER)
        self.visor=tk.Label(self.window2,text="Escreva os pontos para achar\na equação correspondente: ",bg="light cyan",
                            fg="black", font=("Arial",12))
        self.visor1=tk.Label(self.window2,text="X",bg="light cyan",
                            fg="black", font=("Arial",15))
        self.visor2=tk.Label(self.window2,text="Y",bg="light cyan",
                                        fg="black", font=("Arial",15))
        self.entradas=[]

    def start(self,num,metodo):
        self.window2.geometry("480x600")
        self.window2.minsize(480,600)

        for i in range (num+5):
            tk.Grid.rowconfigure(self.window2, i, weight=1)
        for i in range (2):
            tk.Grid.columnconfigure(self.window2, i, weight=1)

        #visor
        self.equacao.grid(row=0,columnspan=2,sticky=tk.N+tk.S+tk.E+tk.W)
        self.visor.grid(row=1,columnspan=2,sticky=tk.N+tk.S+tk.E+tk.W)
        self.visor1.grid(row=2,column=0,sticky=tk.N+tk.S+tk.E+tk.W)
        self.visor2.grid(row=2,column=1,sticky=tk.N+tk.S+tk.E+tk.W)
        #cria botoes
        for i in range (num):
            self.entradas.append([])
            for j in range (2):
                self.entradas[i].append(tk.Entry(self.window2,font=("Arial",10)))
                self.entradas[i][j].grid(row=(i+3),column=(j),
                                       sticky=tk.N+tk.S+tk.E+tk.W)

        if(metodo !=1 and metodo ==2):
            self.visorX=tk.Label(self.window2,text="Digite o ponto X\n a ser analisado: ",bg="light cyan",
                            fg="black", font=("Arial",10))
            self.visorX.grid(row=(num+3),columnspan=2,sticky=tk.N+tk.S+tk.E+tk.W)
            tk.Grid.rowconfigure(self.window2, (num+3), weight=1)
            self.entradaX = tk.Entry(self.window2,font=("Arial",10))
            self.entradaX.grid(row=(num+4),columnspan=2,sticky=tk.N+tk.S+tk.E+tk.W)
            tk.Grid.rowconfigure(self.window2, (num+4), weight=1)

            self.botaoX = tk.Button(self.window2,text="Calcular resultado",font=("Arial",10))
            self.botaoX.grid(row=(num+5),columnspan=2,sticky=tk.N+tk.S+tk.E+tk.W)
            tk.Grid.rowconfigure(self.window2, (num+5),weight=1)
            self.botaoX.configure(command=lambda:self.metodoInterpolacao(metodo,num,int(self.entradaX.get())))
        elif(metodo !=1 and metodo ==3):
            self.visorX=tk.Label(self.window2,text="Digite o ponto X\n a ser analisado: ",bg="light cyan",
                            fg="black", font=("Arial",10))
            self.visorX.grid(row=(num+3),columnspan=2,sticky=tk.N+tk.S+tk.E+tk.W)
            tk.Grid.rowconfigure(self.window2, (num+3), weight=1)
            self.entradaX = tk.Entry(self.window2,font=("Arial",10))
            self.entradaX.grid(row=(num+4),columnspan=2,sticky=tk.N+tk.S+tk.E+tk.W)
            tk.Grid.rowconfigure(self.window2, (num+4), weight=1)

            self.botaoX = tk.Button(self.window2,text="Gerar equação",font=("Arial",10))
            self.botaoX.grid(row=(num+5),columnspan=2,sticky=tk.N+tk.S+tk.E+tk.W)
            tk.Grid.rowconfigure(self.window2, (num+5),weight=1)
            self.botaoX.configure(command=lambda:self.metodoInterpolacao(metodo,num,int(self.entradaX.get())))
        else:
            self.botao = tk.Button(self.window2,text="Gerar equação",font=("Arial",10))
            self.botao.grid(row=(num+3),columnspan=2,sticky=tk.N+tk.S+tk.E+tk.W)
            self.botao.configure(command=lambda:self.metodoInterpolacao(metodo,num,0))




    def metodoInterpolacao(self,metodo,nPontos,x):
        print("hi")
        a = numpy.zeros((nPontos,2))
        for i in range(nPontos):
            string = self.entradas[i][0].get() + " " +self.entradas[i][1].get()
            a[i] = [float(j) for j in string.strip().split(" ")]
        if(metodo == 1):
            s = Polinomial.start(a,nPontos)
            self.equacao.delete(0,tk.END)
            self.equacao.insert(0,s)
            self.equacao.configure(bg="lightgreen")
        if(metodo==2):
            s=Lagrange.start(a,x)
            self.equacao.configure(bg="lightgreen",font="Arial 12")
            k=tk.Button(self.window2,text="Gerar gráfico",bg="lightgray",
                                            fg="black", font=("Arial",15))
            k.grid(row=(nPontos+6),columnspan=2,sticky=tk.N+tk.S+tk.E+tk.W)
            tk.Grid.rowconfigure(self.window2, (nPontos+6),weight=1)
            self.equacao.delete(0,tk.END)
            self.equacao.insert(0,"Valor de y("+str(x)+") : "+str(s[0]))
            k.configure(command=lambda:s[1].show())
        if(metodo==3):
            s=Newton.start(a,x)
            print(s[0])
            self.equacao.configure(bg="lightgreen")
            self.equacao.delete(0,tk.END)
            self.equacao.insert(0,str(s[0]))
            y=tk.Label(self.window2,text="Valor de f("+str(x)+"): "+str(s[1]),bg="lightgreen",
                                            fg="black", font=("Arial",10))
            y.grid(row=(nPontos+6),columnspan=2,sticky=tk.N+tk.S+tk.E+tk.W)
            tk.Grid.rowconfigure(self.window2, (nPontos+6),weight=1)

            k=tk.Button(self.window2,text="Gerar gráfico",bg="lightgray",
                                            fg="black", font=("Arial 10 bold"))
            k.grid(row=(nPontos+7),columnspan=2,sticky=tk.N+tk.S+tk.E+tk.W)
            tk.Grid.rowconfigure(self.window2, (nPontos+7),weight=1)
            k.configure(command=lambda:s[2].show())
