## --Adding color to all the point in the plot using color attribute

import matplotlib.pyplot as plt
import numpy as np

x = np.array([4,43,45,66,78,84,65,34,24,73])
y = np.array([2,3,45,6,7,8,65,4,4,7])

#The number of values of the color should be equall to the array size of all 
color = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown"])

plt.scatter(x,y,c=color)
plt.show()
