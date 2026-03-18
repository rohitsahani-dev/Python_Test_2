## --Adding color to all the point in the plot using color attribute
## --Adding size to each dot in plot
## --Adding transparency to each dot
import matplotlib.pyplot as plt
import numpy as np

x = np.array([4,43,45,66,78,84,65,34,24,73])
y = np.array([72,34,45,66,72,50,65,4,40,17])

#The number of values of the color should be equall to the array size of all 
color = np.array(["red","green","blue","yellow","pink",
                  "black","orange","purple","beige","brown"])

#Each dot can have its own size using s
size = np.array([20,50,100,200,500,1000,60,90,10,300])

#Each dot can be made transparent using alpha = value

plt.scatter(x,y,c=color,s=size,alpha=0.9)

plt.show()
