# Visualização de dados em Python

import matplotlib.pyplot as plt


# data
x1 = [1, 3, 5, 7, 9 ]
y1 = [2, 3, 7, 1, 0]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]

titulo = "Gráfico de barras"
eixo_x = "Eixo X"
eixo_y = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixo_x)
plt.ylabel(eixo_y)

#plt.plot(x, y)  # Line graph
plt.bar(x1, y1, label = "Grupo 1")
plt.bar(x2, y2, label= "Grupo 2")
plt.legend()

plt.show()