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

def f(x):
    return 1/x

a = float(input("\nInsira o limite inferior de integração (a): "))
b = float(input("\nInsira o limite superior de integração (b): "))
n = int(input("\nInsira o número de passos desejado (n): "))

def simpsonrep(f, a, b, n):
    
    if n % 3 != 0:
        print("O número de passos precisa ser um múltiplo de 3 e maior ou igual a 3")
        return
    
    h = (b-a)/(n)
    area2 = 0
    area3 = 0
        
    for i in range(1,n):
        xi = a + i*h
        if i % 3 == 0:
            area2 = area2 + f(xi)
        else:
            area3 = area3 + f(xi)

    areatotal = (3*h/8) *(f(a) + 2*area2 + 3*area3 + f(b))

    return areatotal

areatotal = simpsonrep(f, a, b, n)

print(f"\nA integral aproximada é: {areatotal}")

resultado = quad(f, a, b)[0]
print("Valor real da integral é:", resultado,"\n")

erroabsoluto = (areatotal - resultado)
print("Erro estimado:", erroabsoluto,"\n")
erropercentual = (erroabsoluto/resultado) * 100
print("Erro percentual:",erropercentual,"%")

    
    