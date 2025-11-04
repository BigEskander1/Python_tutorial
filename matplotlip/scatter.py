import matplotlib.pyplot as plt
import numpy as np

hours_studiedX = np.array([0,1,2,3,4,5,6,7,8])
gradeX = np.array([55,60,65,70,79,80,89,90,105])

hours_studiedY = np.array([0,1,2,3,4,5,6,7,8])
gradeY = np.array([45,67,95,30,79,83,89,80,85])

plt.scatter(hours_studiedX,gradeX , color="blue" , label = "Class A")
plt.scatter(hours_studiedY,gradeY , color="red" , label = "Class B")

plt.title("Study")
plt.xlabel("Hours Studied")
plt.ylabel("Grade")

plt.legend()
plt.show()

