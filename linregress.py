import numpy as np
import matplotlib.pyplot as plt 
def min(x,y):
    a=((sum(x)*sum(y)) / (len(x)*len(y))) / (sum(x)/ len(x))**2
    return a   

y = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336]
x = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472] 

m=min(x,y) 
print(m)

pravac_y=[]

for i in x:
     p=m*i
     pravac_y.append(p)
    

x,y  = np.array(x), np.array(y)
plt.scatter(x,y)
plt.plot(x,pravac_y)
plt.show()


    








