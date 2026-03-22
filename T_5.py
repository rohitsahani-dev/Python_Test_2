import matplotlib.pyplot as plt

def graph_plot(x):
    result = 2*x+3
    return result

xCord = []
yCord = []

num = int(input("Enter how many value of x you want to enter : "))

for i in range(num+1):
    x=int(input(f"Enter {i+1} value :"))
    print(f"X{i+1} : {x}")
    xCord.append(x)
    y =graph_plot(x)
    print(f"Y{i+1} : {y}")
    yCord.append(y)

plt.plot(xCord,yCord,marker = 'o')
plt.show()
