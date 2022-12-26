# Visualização de dados em Python

import matplotlib.pyplot as plt


# data
x1 = [1, 3, 5, 7, 9 ]
y1 = [2, 3, 7, 1, 0]
z1 = [200, 500, 400, 330, 1000]

titulo = "Scatterplot: gráfico de dispersão"
eixo_x = "Eixo X"
eixo_y = "Eixo Y"

# Legendas
plt.title(titulo)
plt.xlabel(eixo_x)
plt.ylabel(eixo_y)

plt.scatter(x1, y1, label="Meus pontos", color="m", marker='o', s=z1)
plt.plot(x1, y1, color="k", linestyle="-.")  # Combined scatter with line graph
plt.legend()

plt.savefig("figura1.png", dpi=300)  # we can use figura1.pdf to save like vetor and obtain a good resolution too.
plt.show()

'''
Documentação oficial do Matplotlib
Fonte: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
Cores (color)
'b' blue
'g' green
'r' red
'c' cyan
'm' magenta
'y' yellow
'k' black
'w' white

Markers
character description
'.' point marker
',' pixel marker
'o' circle marker
'v' triangle_down marker
'^' triangle_up marker
'<' triangle_left marker
'>' triangle_right marker
'1' tri_down marker
'2' tri_up marker
'3' tri_left marker
'4' tri_right marker
'8' octagon marker
's' square marker
'p' pentagon marker
'P' plus (filled) marker
'*' star marker
'h' hexagon1 marker
'H' hexagon2 marker
'+' plus marker
'x' x marker
'X' x (filled) marker
'D' diamond marker
'd' thin_diamond marker
'|' vline marker
'_' hline marker


Line Styles
character description
'-' solid line style
'--' dashed line style
'-.' dash-dot line style
':' dotted line style
'''
