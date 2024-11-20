import matplotlib.pyplot as plt
import numpy as np

# Número de dimensões
N = 3

# Cores para os eixos
cores = ['r', 'g', 'b', 'c', 'm', 'y']

# Criando a figura e o subplot tridimensional
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Criando eixos para cada componente do momento
for i in range(N):
    # Gera um vetor unitário na direção do componente i
    direction = np.zeros(N)
    direction[i] = 1
    
    # Pontos para o eixo
    x = [0, direction[0]]
    y = [0, direction[1]]
    z = [0, direction[2]]
    
    # Plotando o eixo com uma cor distinta
    ax.plot(x, y, z, color=cores[i], label=f'p{i+1}')

# Configurações de plotagem
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Mostrando o gráfico
plt.title(f'Eixos de Momento em um Espaço de {N*3} Dimensões')
plt.show()
