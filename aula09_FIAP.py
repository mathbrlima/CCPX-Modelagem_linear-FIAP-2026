# Preparando o ambiente:
from scipy.stats import norm

# Exercício 1
# a)
print(norm.cdf(164, 175, 10))

# b)
print(norm.sf(164, 175, 10))

# ou
a = norm.cdf(164, 175, 10)
b = norm.sf(174, 175, 10)
print(b - a)