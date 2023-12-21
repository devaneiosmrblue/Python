# Disciplina: TÓPICOS ESPECIAIS EM CET
# Discente: Ingryd Medeiros

import numpy as np
from operadores_1 import *
from operadores_2 import *

# Funções teste 
def f(x):
    return np.exp(-x)

def g(x,t):
    return (x**t) - (t**x)

def menu():

    while True:
        print("\nFunções Testes\n")
        print("1. Função teste derivada")
        print("2. Função teste derivada parcial")

        escolha_funcao = input("\nEscolha a função que será utilizada no cálculo da derivada: ")

        try:
            escolha_funcao = int(escolha_funcao)
            
            if escolha_funcao >= 1 or escolha_funcao <= 2:
                h = float(input("\nDigite o valor de h: "))
                x = float(input("Digite o valor de x: "))
                t = float(input("Digite o valor de t: "))

                if escolha_funcao == 1:
                    print("\nOperadores para teste derivada: \n")
                    operadores1 = ["Diferença progressiva", "Diferença regressiva", "Diferença centrada", "Diferença de ordem 2", "Diferença deslocamento", "Operador média"]

                    for i, operador in enumerate(operadores1):
                        print(f"{i}) {operador}")

                    escolha_operador = int(input("\nEscolha um operador para realizar o cálculo: "))
                    resultado = operadores_1(f, x, h, escolha_operador)
                    print(f"\nResultado da derivada: {resultado:.5f}")
                    
                elif escolha_funcao == 2:
                    print("\nOperadores para teste derivada parcial: \n")
                    operadores2 = ["Diferença progressiva u(t)", "Diferença regressiva u(t)", "Diferença centrada u(x)", "Diferença centrada u(xx)", "Diferença centrada u(tt)", "Diferença centrada u(xt)", "Diferença centrada u(tx)"]

                    for i, operador in enumerate(operadores2):
                        print(f"{i}) {operador}")

                    escolha_operador = int(input("\nEscolha um operador para realizar o cálculo: "))
                    resultado = operadores_2(g, x, t, h, escolha_operador)
                    print(f"\nResultado da derivada: {resultado:.5f}")
            else:
                print("Opção inválida")
        except ValueError:
            print("Erro")

def operadores_1(f, x, h, operador):
    if operador == 0:
        return delta_progressiva(f, x, h)
    elif operador == 1:
        return delta_regressiva(f, x, h)
    elif operador == 2:
        return delta_centrada(f, x, h)
    elif operador == 3:
        return delta_ordem2(f, x, h)
    elif operador == 4:
        return delta_deslocamento(f, x, h)
    elif operador == 5:
        return operador_media(f, x, h)

def operadores_2(g, x, t, h, operador):
    if operador == 0:
        return progressiva_ut(g, x, t, h)
    elif operador == 1:
        return regressiva_ut(g, x, t, h)
    elif operador == 2:
        return centrada_ux(g, x, t, h)
    elif operador == 3:
        return centrada_uxx(g, x, t, h)
    elif operador == 4:
        return centrada_utt(g, x, t, h)
    elif operador == 5:
        return centrada_uxt(g, x, t, h)
    elif operador == 6:
        return centrada_utx(g, x, t, h)

menu()
