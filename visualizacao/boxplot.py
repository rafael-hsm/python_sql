# Boxplot - diagrama de caixa

import matplotlib.pyplot as plt
import random


vetor = []

for i in range(10):
    number_random = random.randint(0, 1000)
    vetor.append(number_random)

plt.boxplot(vetor)
plt.title("Boxplot")
plt.show()
