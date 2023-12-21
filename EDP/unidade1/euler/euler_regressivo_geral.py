# Disciplina: TÓPICOS ESPECIAIS EM CET
# Discente: Ingryd Medeiros
# Método de Euler - Regressivo

import numpy as np

def euler_regregeral(f, h, x0, y0, n):
    
    # Listas para armazenar os valores de x e y
    listax = []
    listay_regregeral = [y0]

    # Calcular e armazenar os valores de x atualizado
    for i in range(n + 1):
        xi = x0 + (i * h)
        listax.append(xi)

    # Calcular regressivo de forma generalizada usando o método de Euler
    for i in range(n):
        xi_novo = listax[i]
        yi_novo = listay_regregeral[-1]

    # A correção do calculo para euler regressivo generalizado tenta usar o h e os valores das listas x e y para estimar o proximo ponto da derivada do ponto atual em x e na sua mudança
    # A correção foi sugerida pelo ARIA - IA do opera
    # Calcular e armazenar os valores de y atualizado
        yii = yi_novo + h * f(xi_novo + h, yi_novo + h * f(xi_novo, yi_novo)) # Correção do calculo como tentativa de generalizar
        listay_regregeral.append(yii) 
        
    return listax, listay_regregeral

