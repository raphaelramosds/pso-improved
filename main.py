import sys

# Caminho para essa pasta
path = "/caminho/para/pasta/pso-improved"

# Adicionar módulos adicionais
sys.path.append(path)

import math
import numpy as np
from modules import pso

# Constantes
a = 500
b = 0.1
c = 0.5 * np.pi

# Função para ser minimizada
def costf(position):
    
    # Componentes das coordenadas
    x = position[0]
    y = position[1]
    
    # Funções auxiliares
    z = -x * np.sin(np.sqrt(np.abs(x))) - y * np.sin(np.sqrt(np.abs(y)))
    r = 100 * (y - x**2)**2 + (1 - x)**2
    r1 = (y - x**2)**2 + (1 - x)**2
    rd = 1 + r1
    F10 = -a * np.exp(-b * np.sqrt((x**2 + y**2) / 2)) - np.exp((np.cos(c * x) + np.cos(c * y)) / 2) + np.exp(1)
    zsh = 0.5 - ((np.sin(np.sqrt(x**2 + y**2)))**2 - 0.5) / (1 + 0.1 * (x**2 + y**2))**2
    Fobj = F10 * zsh
    
    # Funções compostas
    w4 = np.sqrt(r**2 + z**2) + Fobj
    w23 = z / rd
    w27 = w4 + w23
    w35 = w23 + w27
    
    # Retorno do fitness
    return w35

# Função teste I - Bukin
def bukin(xx):
    x1 = xx[0]
    x2 = xx[1]
    
    term1 = 100 * math.sqrt(abs(x2 - 0.01 * x1**2))
    term2 = 0.01 * abs(x1 + 10)
    
    y = term1 + term2
    return y

# Chamada do algoritmo
pso.PSO(30,100,((-10,10),(-10,10)),bukin)