# Disciplina: TÓPICOS ESPECIAIS EM CET
# Discente: Ingryd Medeiros

import matplotlib.pyplot as plt
import numpy as np
from euler_progressivo import *
from euler_exato import *
from euler_regressivo import *
from euler_trapezio import *
from euler_regressivo_geral import *
from euler_trapezio_geral import *

# Funções matematicas
def exato(x):
    return x - 1 + 2 * np.exp(-x)

def f(x, y):
    return x - y

# Condições iniciais (pvi)
#x0 = float(input("Digite o valor de x0: "))
#y0 = float(input("Digite o valor de y0: "))
#n = float(input("Digite o valor de n: "))
x0 = 0
y0 = 1
n = 10
h = (y0 - x0) / n

# Chamar as funções
listax, listay_pro = euler_pro(f, h, x0, y0, n)
listax, listay_regre = euler_regre(f, h, x0, y0, n)
listax, listay_exato = euler_exato(funcao=exato,valores_x=listax)
listax, listay_trapezio = euler_trapezio(f, h, x0, y0, n)
#listax, listay_regregeral = euler_regregeral(f, h, x0, y0, n)
#listax, listay_trapeziogeral = euler_trapeziogeral(f, h, x0, y0, n)


# Imprimir as listas com os resultados dos calculos
print("\nListas de Resultados\n")
print("Lista x:", [f"{x:.4f}" for x in listax])
print("Lista y - exato:", [f"{y:.4f}" for y in listay_exato])
print("Lista y - progressivo:", [f"{y:.4f}" for y in listay_pro])
print("Lista y - regressivo:", [f"{y:.4f}" for y in listay_regre])
print("Lista y - trapezio:", [f"{y:.4f}" for y in listay_trapezio])
#print("Lista y - regressivo geral:", [f"{y:.4f}" for y in listay_regregeral])
#print("Lista y - trapezio geral:", [f"{y:.4f}" for y in listay_trapeziogeral])

# Gráfico
plt.plot(listax, listay_pro, label="Euler - Progressivo", color="green")
plt.plot(listax, listay_exato, label="Euler - Exato", color="black")
plt.plot(listax, listay_regre, label="Euler - Regressivo", color="blue")
plt.plot(listax, listay_trapezio, label="Euler - Trapezio", linestyle="--", color="red")
#lt.plot(listax, listay_regre, label='Euler - Regressivo Geral', linestyle='--', color='yellow')
#plt.plot(listax, listay_trapezio, label='Euler - Trapezio Geral', linestyle='--', color='orange')
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(0, 1)
plt.ylim(0, 1.2)
plt.title("Soluções das funções")
plt.show()