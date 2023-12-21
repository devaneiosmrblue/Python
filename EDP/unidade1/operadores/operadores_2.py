# Disciplina: TÓPICOS ESPECIAIS EM CET
# Discente: Ingryd Medeiros
# # Operadores discretizados para 2 variaveis

import numpy as np

# Diferença finita para a derivada parcial progressiva(u(t)) 
def progressiva_ut(g, x, t, h):
    return (g(x, t + h) - g(x, t)) / h

# Diferença finita para a derivada parcial regressiva(u(t)) 
def regressiva_ut(g, x, t, h):
    return (g(x, t) - g(x, t - h)) / h

# Diferença finita para a derivada parcial centrada(u(x)) 
def centrada_ux(g, x, t, h):
    return (g(x + h, t) - g(x - h, t)) / (2*h)

# Diferença finita para a derivada parcial centrada(u(xx)) 
def centrada_uxx(g, x, t, h):
    return (g(x + h, t) - 2 * g(x, t) + g(x - h, t)) / (h**2)

# Diferença finita para a derivada parcial centrada(u(tt)) 
def centrada_utt(g, x, t, h):
    return (g(x, t + h) - 2 * g(x, t) + g(x, t - h)) / (h**2)

# Diferença finita para a derivada parcial centrada(u(xt)) 
def centrada_uxt(g, x, t, h):
    return (g(x + h, t + h) - g(x + h, t - h) - g(x - h, t + h) + g(x - h, t - h)) / (4*h**2)

# Diferença finita para a derivada parcial centrada(u(tx)) 
def centrada_utx(g, x, t, h):
    return (g(x + h, t + h) - g(x + h, t - h) - g(x - h, t + h) + g(x - h, t - h)) / (4*h**2)