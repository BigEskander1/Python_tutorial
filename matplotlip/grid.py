import matplotlib.pyplot as plt
import numpy as np



x = [2023, 2024, 2025, 2026]
y = [15, 25 ,30, 20]
plt.plot(x,y)
plt.grid(axis="y",
         linewidth = 2,
          color = "#000000",
           linestyle = "dotted")
plt.show()