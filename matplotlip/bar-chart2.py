import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["Fruits" , "Grains" , "Protein" , "Dairy" , "Sweets"])
values = np.array([4,3,5,1,2])

plt.title("Daily Consumption")
colors = ["red" , "yellow" , "blue" , "green" , "#33EEFF"]
plt.pie(values ,
         labels = categories ,
           autopct="%1.1f%%" ,
             colors = colors ,
              explode= [  0,  0  , 0 , 0 , 0] ,
              shadow= True,)

plt.show()

