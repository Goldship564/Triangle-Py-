import matplotlib.pyplot as plt 
import numpy as np 
import os 


input("Welcome, press Enter to continue")

a = int(input("Please input a"))
b = int(input("Please input b"))
c = int(input("Please input c"))
 

def sum(a,b):
    return (a+b)

print(sum(a,b))

if sum(a,b)>=c:

    print("It is a triangle")
 
    X = np.array([[0,a], [0,b], [3,c]])
    Y = ['magenta', 'magenta', 'magenta']

    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], s = 0, color = Y[:])

    t1 = plt.Polygon(X[:3,:], color=Y[0])
    plt.gca().add_patch(t1)

    plt.title('Your Triangle') 
    plt.show()

else:

    print("It is not a triangle") 
