
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
import random

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
        
    def update_position(self,it,gbest,w):
           
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
                particle.update_position(it,gbest,w)
                
        # Resultados
        self.solution = gbest
        self.minimum = f(gbest)
    
        print(f"Solução: {gbest}")
        print(f"Mínimo global: {f(gbest)}")
        