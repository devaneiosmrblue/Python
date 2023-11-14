#DISCENTES - Ingryd Medeiros

def isolamentoraiz(f):
        
    #Importação a biblioteca de gráficos do python
    import matplotlib.pyplot as plt
    #Importação a biblioteca de calculo do python
    import numpy as np
    #importação para numeros matematicos mais complexos
    import math

    print('')
    print("O método usado é isolamento de raiz")
    print('')
    
    #Definir os limites de busca de raizes
    i=float(input("Insira o limite inical do intervalo de busca para achar uma raiz: "))
    j=float(input("Insira o limite final do intervalo de busca para achar uma raiz: "))
    h=float(input("Insira o passo desejado: "))
    print('')
    
    listax = []
    listay = []

    #Definar a função isolamento de raiz e quais parametros ela recebe
    def metodoisolamentoraiz(f, i, j, h):
        for x0 in np.arange(i, j+h, h):
            listax.append(x0)
        print(listax)
        print('')
        for k in listax:
            y = f(k)
            listay.append(y)
        print(listay)

    #O for itera sobre os índices de 1 até- 1, com passo de 1. O loop começa em 1 para que o índice indice-1 possa ser usado na comparação.
        print('')
        condicao = 0 #Começa com condição não possui raiz
        for indice in range(1, len(listax), 1):
            if listay[indice] * listay[indice-1] < 0:
                condicao = 1
                print(f"Existe uma raiz no intervalo ({listax[indice-1]}, {listax[indice]})")
        if condicao == 0:
            print ("A função não possui raiz no intervalo de busca")
    
    metodoisolamentoraiz(f, i, j, h)

    # Plotar o gráfico da função
    listax = np.linspace(i, j, 1000)
    listay = []  #inicializa listay como uma lista vazia
    for x in listax:
        listay.append(f(x))
    fig, ax = plt.subplots()
    ax.plot(listax, listay, label='f(x)')
    ax.plot(listax, np.zeros_like(listax), label='x')
    plt.title('Grafico da função f(x)')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    ax.set_ylim(-35,35)
    ax.legend()
    plt.grid()
    plt.show()
