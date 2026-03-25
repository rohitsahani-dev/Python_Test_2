import matplotlib.pyplot as plt
import numpy

x = numpy.random.normal(5.0,1.0,1000)
y = numpy.random.normal(5.0,1.0,1000)

#plt.plot(x,y)

plt.scatter(x,y,color = "red")

plt.show()
