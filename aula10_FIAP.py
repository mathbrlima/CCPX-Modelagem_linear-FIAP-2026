# Gerar Números Inteiros Pseudoaleatórios:
import random

print(random.sample(range(1, 11), 5)) # Sem repetição

print(random.randint(1, 10)  for _ in range(5)) # Com repetição

# Gerar Números Decimais Pseudoaleatórios:
import random

print( [random.uniform(1, 10) for _ in range(5)] )

print( [round(random.uniform(1, 10), 2) for _ in range(5)] )

# Gerar Números Aleatórios com Viés:
import random

random.seed(1)
print( [random.randint(1, 10) for _ in range(5)] )

# Sorteio 'Aleatório' de palavras

nomes = []

# Sorteio de Nomes Viciados:
import numpy as np

nomes = ["Gabi", "Luã", "Rod", "Luh", "Tih", "Nay"]
vies = [0.10, 0.20, 0.05, 0.15, 0.10, 0.40]

print( np.random.choice(nomes, 3, replace=True, p=vies))