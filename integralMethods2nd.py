import tkinter as tk
from numpy import *
from math import *
import sympy as sp

class integralSolver:
    def __init__(self):
        pass
    def insideTopLevel(self,key,parent):
        #inicialize new window
        window3=tk.Toplevel(parent)
        #grid
        window3.geometry("480x300")
        window3.minsize(480,300)
        for i in range (7):
            tk.Grid.rowconfigure(window3, i, weight=1)
        for i in range (4):
            if(i==0 or i ==2):
                k=1
            else:k=10
            tk.Grid.columnconfigure(window3, i, weight=k)
        #configures window3
        pvi=tk.Label(window3,text="Integral (math/numpy)", font="Arial 15 bold", bg="cadetblue1")
        pvi.grid(row=0,column=0,columnspan=4,sticky=tk.N+tk.S+tk.E+tk.W)

        eqbase1=tk.Label(window3,text="y(x) = ", font="Arial 15 bold",bg="lightcyan")
        eqbase=tk.Entry(window3,justify=tk.CENTER,font="14",relief=tk.GROOVE, borderwidth=2)

        eqbase1.grid(row=1,column=0,sticky=tk.N+tk.S+tk.E+tk.W)
        eqbase.grid(row=1,column=1,columnspan=3,sticky=tk.N+tk.S+tk.E+tk.W)


        linf=tk.Label(window3,text="Limite inferior de integração:",font="Arial 15 bold",bg="lightcyan")
        linftext=tk.Entry(window3,width=10,justify=tk.CENTER,font="14",relief=tk.GROOVE, borderwidth=2)

        linf.grid(row=2,column=0,columnspan=3,sticky=tk.N+tk.S+tk.E+tk.W)
        linftext.grid(row=2,column=3,sticky=tk.N+tk.S+tk.E+tk.W)

        lsup=tk.Label(window3,text="Limite superior de integração:",font="Arial 15 bold",bg="lightcyan")
        lsuptext=tk.Entry(window3,width=10,justify=tk.CENTER,font="14",relief=tk.GROOVE, borderwidth=2)

        lsup.grid(row=3,column=0,columnspan=3,sticky=tk.N+tk.S+tk.E+tk.W)
        lsuptext.grid(row=3,column=3,sticky=tk.N+tk.S+tk.E+tk.W)


        precision=tk.Label(window3,text="Precisão:",font="Arial 15 bold",bg="cadetblue1")
        precisionvalue=tk.Entry(window3,justify=tk.CENTER,relief=tk.GROOVE, borderwidth=2)

        precision.grid(row=4,column=0,columnspan=3,sticky=tk.N+tk.S+tk.E+tk.W)
        precisionvalue.grid(row=4,column=3,sticky=tk.N+tk.S+tk.E+tk.W)


        result=tk.Label(window3,text="",font="Arial 15 bold",bg="lightcyan")
        result.grid(row=5,column=0,columnspan=4,sticky=tk.N+tk.S+tk.E+tk.W)

        lParameters=[]
        lParameters.append(key)
        lParameters.append(eqbase)
        lParameters.append(linftext)
        lParameters.append(lsuptext)
        lParameters.append(precisionvalue)
        lParameters.append(result)

        print(lParameters)

        bresult=tk.Button(window3,text="Calcular",font="Arial 15 bold",
                          bg="palegreen1",borderwidth=5,relief=tk.RIDGE,
                          activebackground="palegreen1")
        bresult.grid(row=6,column=0,columnspan=4,sticky=tk.N+tk.S+tk.E+tk.W)
        bresult.configure(command=lambda:self.methods(lParameters,pvi))

    def methods(self,p,pvi):
        #try:
            eq=str(p[1].get())
            linf=float(p[2].get())
            lsup=float(p[3].get())
            precision=float(p[4].get())
            r=0.0
            if(p[0]==0):
                pvi.configure(text="Integral (math/numpy) (Trapezio)")
                print("HIZAO")
                print(eq)
                r=self.integralTrapezio(eq,linf,lsup,precision)
            elif(p[0]==1):
                print("HIZAO2")
                pvi.configure(text="Integral (math/numpy) (Simpson)")
                r=self.simpsonMethod(eq,linf,lsup,precision)
            p[5].configure(text=str(r),bg="lightgreen")
        #except ValueError as error1:
        #    p[5].configure(text=" INPUT ERROR",bg="indianred1")

    def integralTrapezio(self,eq,min,max,p):
        f=lambda x:eval(eq)

        #segunda derivada
        x=sp.Symbol('x')
        s=eq
        s=sp.diff(s,x,2)
        s=str(s.evalf())
        print(s)
        x=0
        f2=lambda x:eval(s)
        print(f)

        n=0.
        gap=(max-min)
        ngap=0.
        res=1.
        maxvalue=0.
        for i in range (int(min)*1000,int(max+1)*1000,1):
            if(i!=0):
                k=i/1000
                if(f2(k)>maxvalue or maxvalue==0):
                    maxvalue=i/1000
        while(res>=p):
            n+=1.0
            ngap=gap/n
            res=(max-min)*(ngap**2)*(f2(maxvalue))/12 #segunda derivada de eqGiven

        delta=(max-min)/n #delta dos tapezios
        aux=.0
        y=.0
        y=f(min)
        aux=min
        for i in range (1,int(n)):
            aux+=delta
            y+=2*f(aux)
        res = (delta/2)*(y+f(max))
        return res

    def simpsonMethod(self,eq,min,max,p):
        f=lambda x:eval(eq)

        #segunda derivada
        x=sp.Symbol('x')
        s=eq
        s=sp.diff(s,x,4)
        s=str(s.evalf())
        print(s)
        x=0
        f4=lambda x:eval(s)
        print(f)

        n=0.
        gap=(max-min)
        ngap=0.
        res=1.
        maxvalue=0.
        for i in range (int(min)*1000,int(max+1)*1000,1):
            if(i!=0):
                k=i/1000
                if(f4(k)>maxvalue or maxvalue==0):
                    maxvalue=i/1000
        while(res>=p):
            n+=1.0
            ngap=gap/n
            res=gap*(ngap**4)*f4(maxvalue)/(180) #quarta derivada de eqGiven
        if(n%2==1):
            n+=1

        h=(max-min)/n
        r=.0
        aux=min
        for i in range(int(n+1)):
            if (i==0 or i==(n)):
                r+=f(aux)
            elif(i%2==0):
                r+=2*f(aux)
            elif(i%2==1):
                r+=4*f(aux)
            aux+=h
        r=(h/3)*r
        return r
