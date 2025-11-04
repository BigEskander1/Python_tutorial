import matplotlib.pyplot as plt
import numpy as np

# x = [2023, 2024, 2025, 2026]
# y = [15, 25 ,30, 20]
# plt.plot(x,y)


x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25 ,30, 20]) 
y2 = np.array([18, 22 ,39, 5]) 
y3 = np.array([1, 12 ,3, 50]) 

line_style = dict( marker = ".",
                markersize = 7,
                markerfacecolor = "#0DE1FF",
                markeredgecolor = "#0DE1FF",
                linestyle = "solid",
                linewidth = 3,
                color = "#0A636B")

font_style = dict(fontsize = 20,
                   family = "Arial",
                    fontweight = "bold")
                  
plt.title("Curve" , **font_style)
plt.xlabel("years" , **font_style)
plt.ylabel("student" , **font_style)

plt.plot(x, y1, **line_style)

plt.plot(x, y2, **line_style)
plt.plot(x, y3, **line_style)

plt.xticks(x)

plt.show()
