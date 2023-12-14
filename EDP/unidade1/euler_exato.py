#Disciplina: TÓPICOS ESPECIAIS EM CET
#Discente: Ingryd Medeiros
#Euler - Exato

import numpy as np

def euler_exato(funcao, valores_x):
    
    # Listas paa armazenar os valores de x(importados da progressiva) e y
    listax = []
    listay = []
    
    for x in valores_x:
        resultado = funcao(x)
        listax.append(x)
        listay.append(resultado)

    return listax, listay