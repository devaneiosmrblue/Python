# Disciplina: TÓPICOS ESPECIAIS EM CET
# Discente: Ingryd Medeiros
# Método de Euler - Progressivo
 
import numpy as np

def euler_pro(f, h, x0, y0, n):

    # Listas para armazenar os valores de x e y
    listax = []
    listay_pro = [y0]
    
    # Calcular e armazenar os valores de x atualizado
    for i in range(n+1):
        xi = x0 + (i * h)
        listax.append(xi)
    
    # Calcular e armazenar os valores de y atualizado
    # [-1] - Usar no calculo o ultimo valor armazenado na lista y
    for i in range(n):
        yi = listay_pro[-1] + h * f(listax[i], listay_pro[-1])
        listay_pro.append(yi)

    return listax, listay_pro
