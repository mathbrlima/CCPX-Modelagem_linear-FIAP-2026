# Preparando o ambiente:
from collections import Counter
import pandas as pd

# Configurar a saída da tabela final:
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# Criar a base de dados:
dados = [14]*6 + [15]*12 + [16]*9 + [17]*3
print(dados)

# Curiosidade:
# print(type(dados))

# Frequência Absoluta:
fi = pd.Series(Counter(dados)).sort_index()
print(fi)

# Frequência Absoluta Acumulada:
fia = fi.cumsum()
print(fia)

# Frequência Relativa:
fr = fi / fi.sum() * 100
print(fr)

# Frequência Relativa Acumulada:
fra = fr.cumsum()
print(fra)

# Montar a tabela:
tabela = pd.DataFrame({
    "Frequência Absoluta": fi,
    "Frequência Absoluta Acumulada": fia,
    "Frequência Relativa": fr,
    "Frequência Relativa Acumulada": fra
})

print(tabela)

# Linha de "Total":
total_row = pd.Series({
    "Frequência Absoluta": fi.sum(),
    "Frequência Absoluta Acumulada": "-",
    "Frequência Relativa": fr.sum(),
    "Frequência Relativa Acumulada": "-"
}, name="Total")

# Tabela Final
tabela = pd.concat([tabela, total_row.to_frame().T])
print(tabela)