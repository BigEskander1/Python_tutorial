import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["Fruits" , "Grains" , "Protein" , "Dairy" , "Sweets"])
values = np.array([4,3,5,1,2])

plt.bar(categories , values)
plt.title("Daily Consumption")
plt.show()
