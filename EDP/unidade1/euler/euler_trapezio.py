#Disciplina: TÓPICOS ESPECIAIS EM CET
#Discente: Ingryd Medeiros
#Método de euler - trapezios

import numpy as np
from euler_progressivo import *
from euler_regressivo import *

def euler_trapezio(f, h, x0, y0, n):

    # Listas para armazenar os valores de x e y
    listax = []
    listay_trapezio = [y0]
    
    # Calcular e armazenar os valores de x atualizado
    for i in range(n+1):
        xi = x0 + (i * h)
        listax.append(xi)
    
    # Chamar os resultados das listas progressiva e regressiva
    listax_pro, listay_pro = euler_pro(f, h, x0, y0, n)
    listax_regre, listay_regre = euler_regre(f, h, x0, y0, n)

    # Calcular e armazenar os valores de y atualizado
    # [-1] - Usar no calculo o ultimo valor armazenado na lista y
    for i in range(n):
        yi_progressivo = listay_pro[i]
        yi_regressivo = listay_regre[i+1] 
        yi = listay_trapezio[-1] + (h/2) * (f(listax[i], yi_progressivo) + f(listax[i+1], yi_regressivo))
        listay_trapezio.append(yi)

    return listax, listay_trapezio
