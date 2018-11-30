import math
import numpy
#import scipy.interpolate
import matplotlib.pyplot as plt

#tentativa de plotar gráfico via formula
#nao consegue corrigir a curva de forma suave gerando curvaturas nao existentes
#def plotFormula(formula,sizeX):
#    x = numpy.array(sizeX)
#    y = eval(formula)
#    x_new = numpy.linspace(x.min(),x.max(),10)
#    y_new = scipy.interpolate.spline(x,y,x_new)
#    plt.plot(x, y)
#    plt.show()

def plotByPointInterPoli(indexes,given): #plota via trechos para gerar curva suavizada
    givenX=[]
    givenY=[]
    for i in range (len(given)):
        givenX.append(given[i][0])
        givenY.append(given[i][1])
    x=[]
    y=[]
    ypoint=[]
    xpoint=[]
    xminimo=float(input("Insira o ponto x minimo a ser vizualizado no grafico: "))
    xmaximo=float(input("Insira o ponto x maximo a ser vizualizado no grafico: "))
    xminimo*=10
    xmaximo=(xmaximo)*10+1
    plt.axhline(y=.0,xmin=-100000,xmax=100000,linewidth=.5,color='k') #eixo x
    plt.axvline(x=.0,ymin=-100000,ymax=100000,linewidth=.5,color='k') #eixo y
    for i in range (int(xminimo),int(xmaximo),1):   #gera uma linha a cada 0.1 do eixo x
        r=0.
        x.append(i/10)
        for j in range (len(indexes)):
            r+=indexes[j]*((i/10)**j)
        y.append(r)
    #for i in range (int(round(min(x))-1),int(round(max(x))+2),1): #grades verticais
    #    plt.axvline(x=i,ymin=-1000,ymax=1000,linewidth=.1,color='k',linestyle='--')
    #for i in range (int(round(min(y))-1),int(round(max(y))+2),1): #grades horizontais
    #    plt.axhline(y=i,xmin=-1000,xmax=1000,linewidth=.1,color='k',linestyle='--')

    aux=0
    temp=int(input("Insira a quantidades de pontos que deseja analisar: "))
    print("Insira os pontos de análise em x (pressione enter a cada valor)")
    for i in range(temp):
        aux=float(input())
        xpoint.append(aux)
    for i in range (len(xpoint)):   #gera um ponto para cada item analisado
        r=0.
        for j in range (len(indexes)):
            r+=indexes[j]*(xpoint[i]**j)
        ypoint.append(r)
        print("Viscosidade para w={}: V={}\n".format(xpoint[i],ypoint[i]))
    for i in range(len(ypoint)): #grades verticais nos pontos analisados
        plt.axvline(x=xpoint[i],ymin=-100000,ymax=100000,linewidth=.1,color='k',linestyle='--')
    for i in range (len(xpoint)): #grades horizontais nos pontos analisados
        plt.axhline(y=ypoint[i],xmin=-100000,xmax=100000,linewidth=.1,color='k',linestyle='--')

    text=''
    for i in range(len(xpoint)):
        #text=plt.annotate('['+str(round(xpoint[i],5))+','+str(round(ypoint[i],5))+']',xy=(xpoint[i], ypoint[i]), xycoords='data',xytext=(xpoint[i], ypoint[i]), textcoords='offset points')  #plota o texto do ponto
        #text.set_fontsize( (abs(max(y))+abs(min(y))) * 0.1) #porcentgem ocupada pelo texto
        plt.plot(xpoint[i], ypoint[i], marker='o', markersize=5, color="g") #plota o ponto
    for i in range(len(givenX)):
        plt.plot(givenX[i],givenY[i],marker='D', markersize=5, color="c") #pontos dados
    plt.title('Viscosidade do etanol em função da % '+'de álcool anidro', fontsize=16)
    plt.xlabel('% álcool anidro', fontsize=14)
    plt.ylabel('Viscosidade do etanol', fontsize=14)
    plt.plot(x,y)
    plt.show()


def refactFormula(indexes,qtd):
    s = ''
    for i in range(qtd):
        if((round(indexes[i],5)*(-1))<0):
            s+='+'
        s+=str(round(indexes[i],10))+'*x**'+str(i)
    return s

def interPoli(a,qtd):
    a = a[a[:,1].argsort()[::-1]] #ondena os pontos

    A = numpy.zeros((qtd,qtd))
    for i in range(qtd):
        for j in range(qtd):
            A[i][j] = a[i][0]**j

    B = numpy.zeros(qtd)
    for i in range(qtd):
        B[i] = a[i][1]

    poliIndexes = numpy.zeros(temp)
    poliIndexes = numpy.linalg.solve(A,B)

    min=int(a[:,0].min())
    max=int(a[:,0].max())

    return refactFormula(poliIndexes,qtd)

    #plotByPointInterPoli(poliIndexes,a)
    #plotFormula(refactFormula(poliIndexes,qtd), range(min,max))


def start(a,nPontos):
    return interPoli(a,nPontos)
