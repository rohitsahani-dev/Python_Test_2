import matplotlib.pyplot as plt
import numpy as np

#--Adding color to each bar in the bar-graph
x = np.array(["A","B","C","D","E"])
y = np.array([7,6,9,5,3])
c = np.array(["red","green","blue","black","cyan"])

#--In bargraph color is the key word
#--The width is added

#there is a barh which is a horizontal bar

while True:
    b = input("Enter 'h' for horizontal bar graph or 'b' for normal bar graph (h/b): ").lower()
    if b == 'h':
        plt.barh(x, y, color=c, height=0.5)
        plt.title("Horizontal Bar Graph")
        plt.show()
        break
    elif b == 'b':
        plt.bar(x, y, color=c, width=0.5)
        plt.title("Vertical Bar Graph")
        plt.show()
        break
    else:
        print("Invalid input. Please enter 'h' or 'b'.")

