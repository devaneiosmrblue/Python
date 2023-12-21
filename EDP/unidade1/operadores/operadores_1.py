# Disciplina: TÓPICOS ESPECIAIS EM CET
# Discente: Ingryd Medeiros
# Operadores discretizados

import numpy as np

# Diferença progressiva 
def delta_progressiva (f, x, h):
    delta_pro = (f(x + h) - f(x)) / h
    return delta_pro

# Diferença regressiva
def delta_regressiva (f, x, h):
    delta_regre = (f(x) - f(x - h)) / h
    return delta_regre

# Diferença centrada
def delta_centrada (f, x, h):
    delta_central = (f(x + (h/2)) - f(x - (h/2))) / (2*h)
    return delta_central

# Diferença para derivada de segunda ordem
def delta_ordem2(f, x, h):
    delta_od2 = (f(x + h) - 2*f(x) + f(x - h)) / (h**2)
    return delta_od2

# Diferença deslocamento
def delta_deslocamento (f, x, h):
    delta_desloc = f(x + h)
    return delta_desloc

# Operador média
def operador_media (f, x, h):
    opm = (1/2) * (f(x + (h/2))) + f(x - (h/2))
    return opm


    