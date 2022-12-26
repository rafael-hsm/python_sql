import os

import matplotlib.pyplot as plt

# Crescimento da População Brasileira 1980-2016
# DataSus

path_ = os.getcwd() + os.sep + "visualizacao" + os.sep + "populacao_brasileira.csv"
print(path_)
dados = open(file=path_).readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        line = dados[i].split(";")
        x.append(int(line[0]))
        y.append(int(line[1]))

d = dict(zip(x, y))        
for i, v in d.items():
    if v > 150000000:
        print(i)
        break

plt.plot(x, y, color="k", linestyle="--")
plt.bar(x, y, color="#e4e5e4")

# Legendas
plt.title("Crescimento da População Brasileira 1980-2016")
plt.xlabel("Ano")
plt.ylabel("População")

# Save figure
plt.savefig("Crescimento da população brasileira.png", dpi=600)

# Show graph
plt.show()