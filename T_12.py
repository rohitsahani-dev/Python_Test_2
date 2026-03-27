import matplotlib.pyplot as plt
import numpy as np

#--create arrays that represent the value of the x and y axis:-
x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

#--numpy has method that lets us make a polynomial model:-
mymodel=np.poly1d(np.polyfit(x,y,3))

#--this line specifies the line spacing starting from 1 and end at 22 position :-
myline=np.linspace(1,22,100)

#--Draw the original scatter plot:-
plt.scatter(x,y)

#--Draw the line of polynomial regression:-
plt.plot(myline,mymodel(myline))

#--Display the output:-
plt.show()
