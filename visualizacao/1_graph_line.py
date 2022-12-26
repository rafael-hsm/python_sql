# Visualização de dados em Python

import matplotlib.pyplot as plt


# data
x1 = [1, 3, 5, 7, 9 ]
y1 = [2, 3, 7, 5, 3]

titulo = "Gráfico de Linha"
eixo_x = "Eixo X"
eixo_y = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixo_x)
plt.ylabel(eixo_y)

# Line graph
plt.plot(x1, y1)

plt.show()
