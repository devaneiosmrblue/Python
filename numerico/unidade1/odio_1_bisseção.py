#DISCENTES - Ingryd Medeiros

def bisseção(f):
    #Importação a biblioteca de gráficos do python
    import matplotlib.pyplot as plt
    #Importação a biblioteca de calculo do python
    import numpy as np
    #Importar o arquivo isolamento de raiz, apelidado de (iso)
    import biblioteca_isolamento_raiz as iso
    #Importação da biblioteca do grafico, apelidado de gaf
    import biblioteca_grafico as gaf
    #Importação para numeros matematicos mais complexos
    import math


    print('')
    print("O método usado é bisseção")
    print('')

    #Definir os limites de busca de raizes
    i=float(input("Insira o limite inical do intervalo de busca para achar uma raiz: "))
    j=float(input("Insira o limite final do intervalo de busca para achar uma raiz: "))
    h=float(input("Insira o passo desejado: "))
    print('')


    #Definir a função bisseção e quais parametros ela recebe 
    def metodobissecao(f, i, j, e, imax):
        repeticoes = 0
        x = (i+j)/2
    
        #Início do laço de iterações
        while repeticoes <= imax:
            if abs(f(x)) < e:
                #Imprime a raiz encontrada e o número de iterações com 10 casas decimais
                print(f"A raiz aproximada é: {x:.10f} com {repeticoes} iterações")
                break
            if f(i) * f(x) < 0:
                j = x
            else:
                i = x
            x = (i+j)/2
            #Imprime as informações desejadas da iteração (i, j, x e f(x) com 10 casas decimais)
            print(f"Iteração {repeticoes}: i = {i:.10f}, j = {j:.10f}, x = {x:.10f}, f(x) = {f(x):.10f}")
            repeticoes += 1

    #Chamar a função isolamento de raiz e seus parametros
    iso.isolamento_de_raiz(f, i, j, h)
    print('') 

    #Inserir os intervalos que possuem raizes e precisão desejada
    i1 = float(input("Digite o intervalo inicial: "))
    i2 = float(input("Digite o intervalo final: "))
    e = float(input("Digite a precisão desejada: "))
    imax = int(input("Digite a iteração máxima (∈ = Z): "))

    #Chamar a função bisseção e seus parametros
    metodobissecao(f, i1, i2, e, imax)
    #Chamar a função gráfico e seus parametros
    gaf.grafico(f, i1, i2)
