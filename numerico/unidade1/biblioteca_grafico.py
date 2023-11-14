#DISCENTES - Ingryd Medeiros

#importação de biblioteca de gráficos do python
import matplotlib.pyplot as plt
#Importação da biblioteca de calculo do python
import numpy as np
import math

#Definir a função gráfico e seus parâmetros
def grafico(f, i, j):
#f(função basica), i(início do intervalo de busca), j(fim do intervalo de busca)

#Plotar gráfico
    x = np.linspace(i, j, 1000)
    y = f(x)
    raiz = (f, i, j)
    fig, ax = plt.subplots()
    ax.plot(x, y, label='Função')
    ax.axhline(y=0, color='black', linestyle='-')
    ax.axvline(x=raiz, color='purple', linestyle='.', label=f'Raiz: {raiz:.5f}')
    plt.title('Grafico da função f(x)')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    ax.set_ylim(y.min(), y.max())
    ax.legend()
    plt.grid()
    plt.show()