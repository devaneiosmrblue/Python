#GRUPO 3 - CALCULO NÚMERICO - TURMA T01
#DISCENTES - Ana Clara // Lucas Perdigão // Lorrane Myllena //Ingryd Medeiros

#Importação a biblioteca de gráficos do python
import matplotlib.pyplot as plt
#Importação a biblioteca de calculo do python
import numpy as np
#Importação para numeros matematicos mais complexos
import math

#Do arquivo odio 0 será importado a função bissesão 
from odio_0_isolamento_raiz import isolamentoraiz

#Do arquivo odio 1 será importado a função bissesão 
from odio_1_bisseção import bisseção 

#Do arquivo odio 2 será importado a função falsa posição 
from odio_2_falsa_posição import falsaposição 

#Do arquivo odio 3 será importado a função ponto fixo
from odio_3_ponto_fixo import pontofixo 

#Do arquivo odio 3 será importado a função ponto fixo
from odio_4_newton import newtonraphson 

#Do arquivo odio 3 será importado a função ponto fixo
from odio_5_secante import secante

#Do arquivo odio 3 será importado a função ponto fixo
from odio_6_muller import muller


#Funções f(x)
def f1(x):
    return x**3-9*x+5

def f2(x):
    return 2*x**4+4*x**3+3*x**2-10*x-15

def f3(x): 
    return x**5-2*x**4-9*x**3+22*x**2+4*x-24

def f4(x):
    return 5*x**3 + x**2 - np.exp(1-2*x) + np.cos(x) + 20
f4_scalar = np.vectorize(f4)

def f5(x):
    return x*np.sin(x) + 4

#Funções phi(x) das testes
def phi1(x):
    return (x**3 + 5)/9

def phi2(x):
    return 0.5**((2*x**4+4*x**3+3*x**2-15)/10)

def phi3(x):
    return 0.5**((x**5-2*x**4+22*x**2+4*x-24)/9)

def phi4(x):
    return np.exp(1-2*x) - 5*x**3 - x**2 - np.cos(x) - 20

def phi5(x):
    return 4/np.sin(x) - x

listaf = [f1, f2, f3, f4, f5]
listaphi = [phi1, phi2, phi3, phi4, phi5]

# Loop do menu de seleção
while True:
    # Exibe as opções do menu
    print("")
    print("Os métodos de zero de funções são:")
    print("0. Isolamento de raiz")
    print("1. Bisseção")
    print("2. Falsa Posição")
    print("3. Ponto fixo")
    print("4. NewtonRaphson")
    print("5. Secante")
    print("6. Muller")
    print("7. Sair")
    print("")
    
    # Recebe a escolha do usuário
    escolha = int(input("Digite o número do método desejado: "))
    
    print("")
    print("As equações testes são:")
    print ("0. x^3 - 9*x + 5")
    print ("1. 2*x^4 + 4*x^3 + 3*x^2 - 10*x - 15")
    print ("2. x^5 - 2*x^4 - 9*x^3 + 22*x^2 + 4*x - 24")
    print ("3. 5*x^3 + x^2 - e^(1-2*x) + cos(x) + 20")
    print ("4. x*sen(x) + 4")
    print("")
    
    indicef = int(input("Escolha a equação desejada: "))

    # Verifica a escolha do usuário e chama a função correspondente
    if escolha == 0:
        isolamentoraiz(listaf[indicef-1])
    elif escolha == 1:
        bisseção(listaf[indicef-1])
    elif escolha == 2:
        falsaposição(listaf[indicef-1])
    elif escolha == 3:
        pontofixo(listaf[indicef-1], listaphi[indicef-1])
    elif escolha == 4:
        newtonraphson(listaf[indicef-1])
    elif escolha == 5:
        secante(listaf[indicef-1])
    elif escolha == 6:
        muller(listaf[indicef-1])
    elif escolha == 7:
        print("Você escolheu sair do menu")
        break
    else:
        print("Opção inválida. Digite um número de 0 a 7 para selecionar uma opção válida ou 7 para sair.") 
