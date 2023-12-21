#Disciplina: TÓPICOS ESPECIAIS EM CET
#Discente: Ingryd Medeiros
#Método de euler - trapezios

import numpy as np
from euler_progressivo import *
from euler_regressivo_geral import *

def euler_trapeziogeral(f, h, x0, y0, n):

    # Listas para armazenar os valores de x e y
    listax = []
    listay_trapeziogeral = [y0]
    
    # Calcular e armazenar os valores de x atualizado
    for i in range(n+1):
        xi = x0 + (i * h)
        listax.append(xi)
    
    # Chamar os resultados das listas progressiva e regressiva generalizada 
    listax_pro, listay_pro = euler_pro(f, h, x0, y0, n)
    listax_regregeral, listay_regregeral = euler_regregeral(f, h, x0, y0, n)

    # Calcular e armazenar os valores de y atualizado
    for i in range(n):
        yi_progressivo = listay_pro[i]
        yi_regressivo = listay_regregeral[i+1] 
        yi = listay_trapeziogeral[-1] + (h/2) * (f(listax[i], yi_progressivo) + f(listax[i+1], yi_regressivo))
        listay_trapeziogeral.append(yi)

    return listax, listay_trapeziogeral

