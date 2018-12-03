import math
import numpy
import matplotlib.pyplot as plt

def plotByPointInterP(given,xAnalise): #plota via trechos para gerar curva suavizada
    givenX=[]
    givenY=[]
    for i in range (len(given)):
        givenX.append(given[i][0])
        givenY.append(given[i][1])
    x=[]
    y=[]
    ypoint=0.
    xpoint=0.
    xminimo=givenX[0]-1
    xmaximo=givenX[len(givenX)-1]+1
    if(xminimo>xAnalise):
        xminimo=xAnalise
    elif(xmaximo<xAnalise):
        xminimo=xAnalise
    xminimo*=10
    xmaximo=(xmaximo)*10+1
    plt.axhline(y=.0,xmin=-100000,xmax=100000,linewidth=.5,color='k') #eixo x
    plt.axvline(x=.0,ymin=-100000,ymax=100000,linewidth=.5,color='k') #eixo y
    for i in range (int(xminimo),int(xmaximo),1):   #gera uma linha a cada 0.1 do eixo x
        r=0.
        x.append(i/10)
        y.append(poliLagrange(given,len(givenX),i/10))
    #for i in range (int(round(min(x))-1),int(round(max(x))+2),1): #grades verticais
    #    plt.axvline(x=i,ymin=-1000,ymax=1000,linewidth=.1,color='k',linestyle='--')
    #for i in range (int(round(min(y))-1),int(round(max(y))+2),1): #grades horizontais
    #    plt.axhline(y=i,xmin=-1000,xmax=1000,linewidth=.1,color='k',linestyle='--')

    '''aux=0
    temp=int(input("Insira a quantidades de pontos que deseja analisar: "))
    print("Insira os pontos de análise em x (pressione enter a cada valor)")
    for i in range(temp):
        aux=float(input())'''
    xpoint=xAnalise
    ypoint=(poliLagrange(given,len(givenX),xAnalise))
    print("f({})={}\n".format(xpoint,ypoint))

    #grades verticais nos pontos analisados
    plt.axvline(x=xpoint,ymin=-100000,ymax=100000,linewidth=.1,color='k',linestyle='--')
    #grades horizontais nos pontos analisados
    plt.axhline(y=ypoint,xmin=-100000,xmax=100000,linewidth=.1,color='k',linestyle='--')

    #text=''
    #for i in range(len(xpoint)):
        #text=plt.annotate('['+str(round(xpoint[i],5))+','+str(round(ypoint[i],5))+']',xy=(xpoint[i], ypoint[i]), xycoords='data',xytext=(xpoint[i], ypoint[i]), textcoords='offset points')  #plota o texto do ponto
        #text.set_fontsize( (abs(max(y))+abs(min(y))) * 0.1) #porcentgem ocupada pelo texto
    plt.plot(xpoint, ypoint, marker='o', markersize=5, color="g") #plota o ponto
    for i in range(len(givenX)):
        plt.plot(givenX[i],givenY[i],marker='D', markersize=5, color="c") #pontos dados
    plt.title('Gráfico de f(x)', fontsize=16)
    plt.xlabel('x', fontsize=14)
    plt.ylabel('y', fontsize=14)
    plt.plot(x,y)
    r=[]
    r.append(ypoint)
    r.append(plt)
    return r


def calculateLx(A,k,qtd,x):
    l=1.
    for i in range(qtd):
        if(i!=k):
            l*=(x-A[i][0])/(A[k][0]-A[i][0])
    return l

def poliLagrange(A,qtd,x):
    p=0.

    for i in range(qtd):
        p+=A[i][1]*calculateLx(A,i,qtd,x)

    return p

def start(a,x):
    r=[]
    r=plotByPointInterP(a,x)
    return r
