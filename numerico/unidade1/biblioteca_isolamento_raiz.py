#DISCENTES - Ingryd Medeiros

#Importação a biblioteca de gráficos do python
import matplotlib.pyplot as plt
#Importação a biblioteca de calculo do python
import numpy as np
#Importação de numeros complexos do python
import math as math

#Definir as listas que seram usadas
listax = []
listay = []

#Definir a função isolamento de raiz e quais parâmetros ela recebe
def isolamento_de_raiz(f, i, j, h):
    for x0 in np.arange(i, j+h, h): 
    #A função np.arange gera um range NumPy com valores no intervalo [i, j+h], com um passo h.
        listax.append(x0) 
    #listax.append(x0) é uma operação que adiciona o valor atual de x0 à lista listax
    print(listax) 
    print('')
    for k in listax: 
    #O loop for itera sobre cada valor k na listax, calcula o valor correspondente de f(k) usando a função f(x) e adiciona o resultado à lista listay
        y = f(k)
        listay.append(y) 
    #A listay contém os valores de f(x) para cada valor de x na listax
    print(listay)

    print('')
    condição = 0 
    #Começa com condição que não possui raiz
    for indice in range(1, len(listax), 1):
    #O for itera sobre os índices de 1 até- 1, com passo de 1. O loop começa em 1 para que o índice indice-1 possa ser usado na comparação
        if listay[indice] * listay[indice-1] < 0: 
    #Verifica se o produto das listas é negativo. Se verdadeiro, isso significa o produto dos índices possuem sinais opostos e, portanto, há uma raiz no intervalo entre esses pontos
            condição = 1
            print(f"Existe uma raiz no intervalo ({listax[indice-1]}, {listax[indice]})") 
    #Caso exista raiz no intervalo de busca, ele imprime elas para o usuario
    if condição == 0: 
    #Verifica se a condição é igual a zero, caso seja, então nenhuma raiz foi encontrada no intervalo definido pelo usuário e ele imprime a mensagem
        print ("A função não possui raiz no intervalo de busca")