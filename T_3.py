import matplotlib.pyplot as plt
import numpy as np

#--Adding 100 dot, in random location in the graph using random 
x = np.random.randint(100,size=(100))
y = np.random.randint(100,size=(100))
color = np.random.randint(100,size=(100))
size =10*np.random.randint(100,size=(100))

#--cmap is a keyword and nipy_spectral is the build in colormaps
plt.scatter(x,y,c=color,s=size,alpha=0.7,cmap='nipy_spectral')

#--You can include the colormap in the drawing by including the plt.colorbar() statement:
plt.colorbar()

plt.show()
