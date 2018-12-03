import tkinter as tk
import numpy
import math

class edoSolver:
    def __init__(self):
        pass
    def insideTopLevel(self,key,parent):
        #inicialize new window
        window3=tk.Toplevel(parent)
        #grid
        window3.geometry("480x300")
        window3.minsize(480,300)
        for i in range (8):
            tk.Grid.rowconfigure(window3, i, weight=1)
        for i in range (4):
            if(i==0 or i ==2):
                k=1
            else:k=10
            tk.Grid.columnconfigure(window3, i, weight=k)
        #configures window3
        pvi=tk.Label(window3,text="PVI", font="Arial 15 bold", bg="cadetblue1")
        pvi.grid(row=0,column=0,columnspan=4,sticky=tk.N+tk.S+tk.E+tk.W)

        ylinha=tk.Label(window3,text="y(x,y)' = ", font="Arial 15 bold",bg="lightcyan")
        eqbase=tk.Entry(window3,justify=tk.CENTER,font="14",relief=tk.GROOVE, borderwidth=2)

        ylinha.grid(row=1,column=0,sticky=tk.N+tk.S+tk.E+tk.W)
        eqbase.grid(row=1,column=1,columnspan=3,sticky=tk.N+tk.S+tk.E+tk.W)


        ybase=tk.Label(window3,text="y       (",font="Arial 15 bold",anchor=tk.E,bg="lightcyan")
        initialx=tk.Entry(window3,width=10,justify=tk.CENTER,font="14",relief=tk.GROOVE, borderwidth=2)
        ybase2=tk.Label(window3,text=")        = ",font="Arial 15 bold",anchor=tk.W,bg="lightcyan")
        xvalue=tk.Entry(window3,width=10,justify=tk.CENTER,font="14",relief=tk.GROOVE, borderwidth=2)

        ybase.grid(row=2,column=0,sticky=tk.N+tk.S+tk.E+tk.W)
        initialx.grid(row=2,column=1,sticky=tk.N+tk.S+tk.E+tk.W)
        ybase2.grid(row=2,column=2,sticky=tk.N+tk.S+tk.E+tk.W)
        xvalue.grid(row=2,column=3,sticky=tk.N+tk.S+tk.E+tk.W)


        hsize=tk.Label(window3,text="Tamanho do intervalo",font="Arial 15 bold",bg="cadetblue1")
        hvalue=tk.Entry(window3,justify=tk.CENTER,relief=tk.GROOVE, borderwidth=2)

        hsize.grid(row=3,column=0,columnspan=4,sticky=tk.N+tk.S+tk.E+tk.W)
        hvalue.grid(row=4,column=0,columnspan=4,sticky=tk.N+tk.S+tk.E+tk.W)


        rslt=tk.Label(window3,text="Insira x para y(x)",font="Arial 15 bold",bg="cadetblue1")
        rslt.grid(row=5,column=0,columnspan=4,sticky=tk.N+tk.S+tk.E+tk.W)


        yr=tk.Label(window3,text="y      (",font="Arial 15 bold",anchor=tk.E,bg="lightcyan")
        calcx=tk.Entry(window3,width=10,justify=tk.CENTER,relief=tk.GROOVE, borderwidth=2)
        yr2=tk.Label(window3,text=")        =",font="Arial 15 bold",anchor=tk.W,bg="lightcyan")
        result=tk.Label(window3,width=10,bg="lightcyan",relief=tk.GROOVE, borderwidth=2)

        yr.grid(row=6,column=0,sticky=tk.N+tk.S+tk.E+tk.W)
        calcx.grid(row=6,column=1,sticky=tk.N+tk.S+tk.E+tk.W)
        yr2.grid(row=6,column=2,sticky=tk.N+tk.S+tk.E+tk.W)
        result.grid(row=6,column=3,sticky=tk.N+tk.S+tk.E+tk.W)


        lParameters=[]
        lParameters.append(key)
        lParameters.append(eqbase)
        lParameters.append(hvalue)
        lParameters.append(initialx)
        lParameters.append(xvalue)
        lParameters.append(calcx)
        lParameters.append(result)

        print(lParameters)

        bresult=tk.Button(window3,text="Calcular",font="Arial 15 bold",
                          bg="palegreen1",borderwidth=5,relief=tk.RIDGE,
                          activebackground="palegreen1")
        bresult.grid(row=7,column=0,columnspan=4,sticky=tk.N+tk.S+tk.E+tk.W)
        bresult.configure(command=lambda:self.methods(lParameters,pvi))

    def methods(self,p,pvi):
        try:
            eq=str(p[1].get())
            h=float(p[2].get())
            t0=float(p[3].get())
            y0=float(p[4].get())
            xget=float(p[5].get())
            r=0.
            if(p[0]==0):
                print(eq)
                pvi.configure(text="PVI (EULER)")
                r=self.eulerEDO(eq,h,y0,t0,xget)
            elif(p[0]==1):
                pvi.configure(text="PVI (Runge-Kutta - 2a ordem))")
                r=self.rungeKutta2(eq,h,y0,t0,xget)
            else:
                pvi.configure(text="PVI (Runge-Kutta - 4a ordem))")
                r=self.rungeKutta4(eq,h,y0,t0,xget)
            p[6].configure(text=str(r),bg="lightgreen")
        except ValueError as error1:
            p[6].configure(text=" INPUT ERROR",bg="indianred1")

    def eulerEDO(self,eq,h,y0,t0,xget):
        y=0.
        y=y0
        x=t0
        k=0.
        f=(lambda x,y:eval(eq))
        if(xget!=0):
            while(x<=xget):
                y = y + h*f(x,y)
                x+=h
        return (y)

    def rungeKutta2(self,eq,h,y0,t0,xget):
        yn=0.
        y=y0
        x=t0
        k=0.
        f=(lambda x,y:eval(eq))
        if(xget!=0):
            while(x<=xget):
                s1=f(x,y)
                s2=f((x+h),(y+h*s1))
                y = y+(h/2)*(s1+s2)
                x+=h
        return y

    def rungeKutta4(self,eq,h,y0,t0,xget):
        yn=0.
        y=y0
        x=t0
        k=0.
        f=(lambda x,y:eval(eq))
        if(xget!=0):
            while(x<=xget):
                s1=f(x,y)
                s2=f((x+h/2),(y+h/2*s1))
                s3=f((x+h/2),(y+h/2*s2))
                s4=f((x+h),(y+h*s3))
                y = y + (h/6)*(s1+2*s2+2*s3+s4)
                x+=h
        return y
