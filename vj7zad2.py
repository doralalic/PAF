import numpy as np
import matplotlib.pyplot as plt
import projectile as pr

dt = [0.01, 0.02, 0.05]
for i in dt:
    p = pr.Projectile(2, 5, 0, 0, 60, 0.2, 0.2, 0.2, i)
    a, b = p.Euler()
    plt.scatter(a, b, s = 1, label = "Euler{}".format(i))
p2 = pr.Projectile(2, 5, 0, 0, 60, 0.5, 0.5, 0.5, 0.01)
x,y = p2.Runge_Kutta()
plt.plot(x, y, c = "black", label = "Runge-Kutta{}".format(0.01))
plt.legend()
plt.show()