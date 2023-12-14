#Disciplina: TÓPICOS ESPECIAIS EM CET
#Discente: Ingryd Medeiros

import matplotlib.pyplot as plt
import numpy as np
from euler_exato import *
from euler_progressivo import *
from euler_regressivo import *


# Funções matematicas
def exato(x):
    return x - 1 + 2 * np.exp(-x)

def f(x, y):
    return x - y

# Condições iniciais
x0 = 0
y0 = 1
h = 0.1  
n = 10

# Chamar as funções
listax, listay_pro = euler_pro(f, h, x0, y0, n)
listax, listay_regre = euler_regre(f, h, x0, y0, n)
listax, listay_exato = euler_exato(funcao=exato,valores_x=listax)

print('\nListas de Resultados\n')
print('Lista x:', [f'{x:.4f}' for x in listax])
print('Lista y - progressivo:', [f'{y:.4f}' for y in listay_pro])
print('Lista y - exato:', [f'{y:.4f}' for y in listay_exato])
print('Lista y - regressivo:', [f'{y:.4f}' for y in listay_regre])

# Imprime o resultado do progressivo
# print('\nResultados do Método Euler - Progressivo\n')
# for i in range(1, n+1):
    # resultado = listay_pro[i]
    # equacao = f"y{i} = 0.80 * {listay_pro[i-1]:.4f} + 0.20 * {listax[i]:.2f} = {resultado:.4f}"   
    # print(equacao)

# Imprime o resultado do regressivo
# print('\nResultados do Método Euler - Regressivo\n')
# for i in range(1, n+1):
    # resultado = listay_regre[i]
    # equacao = f"y{i} = 0.80 * {listay_regre[i-1]:.4f} + 0.20 * {listax[i]:.2f} = {resultado:.4f}"   
    # print(equacao)

# Gráfico
plt.plot(listax, listay_pro, label='Euler - Progressivo', color='green')
plt.plot(listax, listay_exato, label = 'Euler - Exato', color='black')
plt.plot(listax, listay_regre, label='Euler - Regressivo', color='blue')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(0,1)
plt.ylim(0,1.2)
plt.title('Soluções da função')
plt.show()
