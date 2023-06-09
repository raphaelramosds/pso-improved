import sys
import numpy as np

# Caminho para essa pasta
path = "C:/Users/rapha/Documents/pso-improved"

# Adicionar módulos adicionais
sys.path.append(path)
from modules import pso

# Função do trabalho
def costf(position):
    
    # Constantes
    a = 500
    b = 0.1
    c = 0.5 * np.pi
    
    # Componentes das coordenadas
    x = position[0]
    y = position[1]
    
    # Funções auxiliares
    z = -x * np.sin(np.sqrt(np.abs(x))) - y * np.sin(np.sqrt(np.abs(y)))
    
    x = x/250
    y = y/250
    
    r = 100 * (y - x**2)**2 + (1 - x)**2
    r1 = (y - x**2)**2 + (1 - x)**2
    rd = 1 + r1
    
    x = 25*x
    y = 25*y
    
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

# Cabeçalho do CSV
with open('./data.csv','a') as file:
    file.write("particles,iterations,x,y,fitness\n")
    for n in range(25):
        # Chamada 1: particulas aumentam de 5 a 30, iterações constantes
        for i in range(5,30 + 5,5):
            p = pso.PSO(i,10,((-500,500),(-500,500)),costf)
            file.write(f"{i},{10},{p.solution[0]},{p.solution[1]},{p.minimum}\n")
        # Chamada 2: iterações aumentam de 25 a 100, particulas constantes
        for i in range(25,100 + 25,25):
            p = pso.PSO(30,i,((-500,500),(-500,500)),costf)
            file.write(f"{30},{i},{p.solution[0]},{p.solution[1]},{p.minimum}\n")