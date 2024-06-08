# Example of a sin function
import matplotlib.pyplot as plt
import numpy as np

# Creazione di alcuni dati
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Creazione del grafico
plt.plot(x, y)
plt.title("Grafico del seno")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.show()