#CALCULO NÚMERICO - TURMA T01
#DISCENTES - Ingryd Medeiros

# Importar a biblioteca de calculo do python
import numpy as np
# Importar a biblioteca de tempo do python
import time
# Importar a biblioteca de gráfico do python
import matplotlib.pyplot as plt
# Importar a biblioteca de matemática do python
from scipy.integrate import quad

# Função teste
def f(x):
    return 1/x

# Limites de integração
a=float(input("\n""Insira o limite inferior de integração (a): "))
b=float(input("\n""Insira o limite superior de integração (b): "))
n=int(input("\n""Insira o numero de passos desejado (n): "))

def trapeziosimples (f, a, b, n):
    
    h = (b-a)/n #n são as partições 
    area2 = 0
    
    area1 = h/2 * (f(a) + f(b)) # Soma das áreas dos dois trapézios
         
    for i in range(1,n):
        xi = a + i*h
        area2 = area2 + f(xi)

    area3 = 2*h/2 * area2
    areatotal = area1 + area3

    return areatotal

areatotal = trapeziosimples(f, a, b, n)

print(f"\nAproximação da integral: {areatotal}")

resultado = quad(f, a, b)[0]
print("Valor real da integral:", resultado,"\n")

erroabsoluto = areatotal - resultado
print("Erro estimado:", erroabsoluto,"\n")
erropercentual = (erroabsoluto/resultado) * 100
print("Erro percentual:",erropercentual,"%")

    
    
    