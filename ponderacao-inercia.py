import numpy as np
import random
import math

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

# Função test: Bukin
def bukin(xx):
    x1 = xx[0]
    x2 = xx[1]
    
    term1 = 100 * math.sqrt(abs(x2 - 0.01 * x1**2))
    term2 = 0.01 * abs(x1 + 10)
    
    y = term1 + term2
    return y

# Redução Linear da Ponderação de Inércia
wmax = 0.9
wmin = 0.4
c1 = 2
c2 = 2
w = 0.5

# Definição de Partícula
class Particle:
    
    def __init__(self,x0,v0,tmax):
        
        self.pbest = np.zeros(2,float)
        self.positions = np.zeros((tmax,2),float)
        self.velocities = np.zeros((tmax,2),float)
        
        self.positions[0] = x0
        self.velocities[0] = v0
        self.pbest = x0
        
    def update_position(self,it,gbest,w,bounds):
        
        # Verifica se ultrapassou limite de busca
        if (self.positions[it][0] > bounds[0][0] and self.positions[it][0] < bounds[0][1]) and (self.positions[it][1] > bounds[1][0] and self.positions[it][1] < bounds[1][1]):
            
            # Gera números aleatórios entre 0 e 1 para r1 e r2
            r1 = random.random()
            r2 = random.random()

            # Calcular velocidade
            inertia = w*self.velocities[it]
            cognitive = c1*r1*(self.pbest - self.positions[it])
            social = c2*r2*(gbest - self.positions[it])
            v = inertia + cognitive + social
            
            # Inseri-los no histórico de iterações
            self.positions[it + 1] = v + self.positions[it]
            self.velocities[it + 1] = v
            
        # Caso ultrapasse, limite pela menor posição do espaço de busca e atualize a velocidade para zero
        else:
            if not(self.positions[it][0] > bounds[0][0] and self.positions[it][0] < bounds[0][1]):
                self.positions[it][0] = bounds[0][0]
            if not(self.positions[it][1] > bounds[1][0] and self.positions[it][1] < bounds[1][1]):
                self.positions[it][1] = bounds[1][0]
            self.velocities[it] = np.zeros(2,float)

# Algoritmo PSO
class PSO:    
    def __init__(self,n,tmax,bounds,f):
        
        # Iniciar enxame
        swarm = []
        for i in range(n):
            # Randomiza posição inicial
            x0 = np.array([
                random.uniform(bounds[0][0], bounds[0][1]),
                random.uniform(bounds[1][0], bounds[1][1])
            ],float)
            
            # Velocidade inicial nula
            v0 = np.array([0,0],float)
            
            # Adiciona particular no enxame
            swarm.append(Particle(x0, v0,tmax))
        
        # Iniciar gbest conforme o enxame inicial
        pbest_fitness = [f(particle.pbest) for particle in swarm]
        gbest = swarm[np.argmin(pbest_fitness)].pbest
        
        # Aplicação do algoritmo
        for it in range(0,tmax - 1):
        
            # Atualizar fator de inércia
            w = wmax - it*(wmax - wmin)/tmax
            
            # Análise das posições: atualização do pbest e gbest
            for particle in swarm:

                position = particle.positions[it]
                
                # Verificar se sua posição atual é um pbest
                if f(position) < f(particle.pbest):
                    particle.pbest = position
                
                # Verificar se sua posição atual é um gbest
                if f(position) < f(gbest):
                    gbest = position
            
                # Atualizar posição da particula
                particle.update_position(it,gbest,w,bounds)
                
        # Resultados
        print(f"Solução: {gbest}")
        print(f"Mínimo global: {f(gbest)}")

# Chamada do algoritmo
PSO(30,100,((-15,-5),(-3,3)),bukin)