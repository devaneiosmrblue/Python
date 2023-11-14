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

def simpsonrep (f, a, b, n):
    
    if n % 2 != 0:
        print("Não é possivel usar o método para o número de particões, ele precisa ser par.") 
        return 
       
    h = (b-a)/n #n são as partições
    print("h:", h) 
    area2 = 0
    area3 = 0
    
    area1 = h/3 * (f(a) + f(b)) # Soma das áreas dos dois trapézios
    print("area um", area1)
    # Area total = area1 + area2 + area3
    for i in range(1,n):
        xi = a + i*h
        print("x:", xi)
        if i % 2 != 0:
            area2 = area2 + f(xi) #números pares
        else:
            area3 = area3 + f(xi) #números impares

    area2 = 4*h/3 * area2
    print("area dois", area2)
    area3 = 2*h/3 * area3
    print("area tres", area3)
    areatotal = area1 + area2 + area3

    return areatotal

areatotal = simpsonrep(f, a, b, n)

print(f"\nA integral aproximada é: {areatotal}")

resultado = quad(f, a, b)[0]
print("Valor real da integral é:", resultado,"\n")

erroabsoluto = areatotal - resultado
print("Erro estimado:", erroabsoluto,"\n")
erropercentual = (erroabsoluto/resultado) * 100
print("Erro percentual:",erropercentual,"%")

    
    
    