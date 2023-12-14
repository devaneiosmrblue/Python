#Disciplina: TÓPICOS ESPECIAIS EM CET
#Discente: Ingryd Medeiros
#Método de Euler - Regressivo

import numpy as np

def euler_regre(f, h, x0, y0, n):
    # Listas para armazenar os valores de x e y
    listax = []
    listay_regre = [y0]
    
    # Cálculo e armazenamento dos valores de x atualizado
    for i in range(n+1):
        xi = x0 + (i * h)
        listax.append(xi)
    
    # Cálculo e armazenamento dos valores de y atualizado
    for i in range(n):
        yi = (1/(1+h)) * (( listay_regre[-1]) + (h * (listax[i+1])))
        listay_regre.append(yi)
    
    return listax, listay_regre

