#CALCULO NÚMERICO - TURMA T01
#DISCENTES - Ingryd Medeiros

print("\n""MMQ - LOGARITMICA","\n")

# Importar a biblioteca de calculo do python
import numpy as np
# Importar a biblioteca de tempo do python
import time
# Importar a biblioteca de gráfico do python
import matplotlib.pyplot as plt
# Importar a biblioteca de tabela do python
from tabulate import tabulate

# Valor de entrada
x = np.array([2, 4, 8, 16, 32, 64, 128, 256])
y = np.array([1,2,3,4,5,6,7,8])
xy = np.array(x*y)
x_2 = np.array(x**2)

# Lista dos valores de entrada
lista1 = []
for i in range(len(x)):
    lista1.append([np.log(x[i]), y[i], np.log(x[i])*y[i], np.log(x[i])**2])

# Imprime a tabela dos dados de entrada
print("Tabela de MMQ - Logaritmica","\n")
print(tabulate(lista1, headers=["ln(x)","y","xy","x^2"], tablefmt="orgtbl"))


def g(x, a, b):
    return a*np.log(x)+b

# Função do MMQ - para ajuste logaritmica
def metodologaritmica(x, y):
    
    try:
        n = len(x)
        somatoriox = 0
        somatorioy = 0
        somatorioxy = 0
        somatoriox_2 = 0

        for i in range(n):
            somatoriox = somatoriox + np.log(x[i])
            somatorioy = somatorioy + y[i]
            somatorioxy = somatorioxy + np.log(x[i])*y[i]
            somatoriox_2 = somatoriox_2 + np.log(x[i])**2

        # Calculo de a e b do método logaritmica
        a = (n * somatorioxy - somatoriox * somatorioy) / (n * somatoriox_2 - somatoriox**2)
        b = (somatoriox * somatorioxy - somatorioy * somatoriox_2) / (somatoriox**2 - n * somatoriox_2)

        # Criar lista de somatórias
        lista2 = [[somatoriox, somatorioy, somatorioxy, somatoriox_2]]

        # Imprime tabela de somatórias
        print("")
        print("Tabela de MMQ - Somatórias:","\n")
        print(tabulate(lista2, headers=["Σx","Σy","Σxy","Σx^2"], tablefmt="orgtbl"))

        #  Cálculo de g(x) para cada valor de x 
        lista3 = []
        for i in range(n):
            xi = g(x[i], a, b)
            lista3.append(xi)

        # Cálculo do R2
        media_y = sum(y)/n
        SQReq = sum((lista3 - media_y)**2)
        SQTot = sum((y - media_y)**2)
        R2 = SQReq / SQTot
        
        # Cálculo dos residuos
        lista4 = []
        for i in range(n):
            y_real = a * np.log(x[i]) + b
            erro = y[i] - y_real
            lista4.append(erro)

        return a, b, R2, erro
    except:
        print("Erro de ajuste")

# Chama a função do método dos MMQ - linear
a, b, R2, erro = metodologaritmica(x, y)

print("")
# Imprime dos valores de a e b
print(f"Os valores de a e b são: a = ({round(a, 4)}) e b = ({round(b, 4)})\n")
# Imprime do equação da reta
print(f"A equação logaritmica da reta g(x) é: ({round(a, 4)}) * x + ({round(b, 4)})\n")
# Imprime do coeficiente de determinação
print(f"R^2 é aproximadamente: {round(R2, 4)}\n")
# Imprime dos residuos 
print(f"Os residuos do calculo são aproximadamente: {round(erro, 4)}\n")
# Chama da função g(x)
g(x, a, b)

# Função gráfico
def grafico(x, y, a, b):
    
    plt.plot(x, y, 'o', color='black', label='Valores de x')
    plt.plot(x, g(x, a, b), color='plum', label='Linha de ajuste logaritmica')
    plt.margins(x=0.1, y=0.1)
    plt.grid(True)
    plt.title('MMQ - Logaritmica', fontsize=14)
    plt.xlabel('Eixo X', fontsize=12)
    plt.ylabel('Eixo Y', fontsize=12)
    plt.legend()
    plt.show()

#Chama a função gráfico e seus parametros
grafico(x, y, a, b)