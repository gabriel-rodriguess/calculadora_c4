import numpy
import math
import matplotlib.pyplot as plt

def plotInGraph(givenx,giveny,xAnalise): #plota via trechos para gerar curva suavizada
    givenX=givenx
    givenY=giveny
    x=[]
    y=[]
    ypoint=newtonMethod(givenx,giveny,xAnalise)
    xpoint=xAnalise
    xminimo=float(input("Insira o ponto x minimo a ser vizualizado no grafico: "))
    xmaximo=float(input("Insira o ponto x maximo a ser vizualizado no grafico: "))
    xminimo*=10
    xmaximo=(xmaximo)*10+1
    plt.axhline(y=.0,xmin=-100000,xmax=100000,linewidth=.5,color='k') #eixo x
    plt.axvline(x=.0,ymin=-100000,ymax=100000,linewidth=.5,color='k') #eixo y
    for i in range (int(xminimo),int(xmaximo),1):   #gera uma linha a cada 0.1 do eixo x
        r=0.
        x.append(i/10)
        y.append(newtonMethod(givenx,giveny,i/10))

    for i in range(len(givenX)):
        plt.plot(givenX[i],givenY[i],marker='D', markersize=5, color="c") #pontos dados
    print("\nValor de y para o x={}: {}".format(xpoint,ypoint))
    print("\nEquação do polinômio: ")
    print(newtonMethodEq(givenx,giveny,xAnalise))
    plt.plot(xpoint,ypoint,marker='o',markersize=5,color='g')
    plt.title('Gráfico do polinomio encontrado', fontsize=16)
    plt.xlabel('x', fontsize=14)
    plt.ylabel('y', fontsize=14)
    plt.plot(x,y)
    plt.show()

def deltasFind(x,y):
    deltasmin=[]
    deltatemp=[]
    for k in range (len(x)-1):
        for i in range (len(y)-1):
            deltatemp.append((y[i+1]-y[i])/(x[i+k+1]-x[i]))
        deltasmin.append(deltatemp[0])
        y=deltatemp
        deltatemp=[]
    return(deltasmin)

def newtonMethod(x,y,xAnalise):
    aux=y[0]
    d=deltasFind(x,y)
    res=aux
    for i in range (len(x)-1):
        temp=1.
        for j in range (i+1):
            temp*=(xAnalise-x[j])
        temp*=d[i]
        res+=temp
    return res

def newtonMethodEq(x,y,xAnalise):
    aux=y[0]
    d=deltasFind(x,y)
    res=aux
    eq=str(res)
    for i in range (len(x)-1):
        temp=1.
        if(d[i]*-1<=0):
            eq=eq+"+"
        eq=eq+str(d[i])
        for j in range (i+1):
            temp*=(xAnalise-x[j])
            eq=eq+"*(x"
            if(x[j]*-1<=0):
                eq=eq+"-"+str(x[j])+")"
            else:
                eq=eq+"+"+str(x[j]*(-1))+")"
        temp*=d[i]
        res+=temp
    return eq

def start(a,xAnalise):
    x=[] #pontos x
    y=[] #pontos y

    for i in range(len(a)):
    	x.append(a[i][0])
    	y.append(a[i][1])

    plotInGraph(x,y,xAnalise)
