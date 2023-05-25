import numpy as np
import matplotlib.pyplot as plt
import projectile as pr

dt = [0.01, 0.02, 0.05]
for i in dt:
    p = pr.Projectile(2, 5, 0, 0, 60, 0.2, 0.2, 0.2, i)
    a, b = p.Euler()
    plt.plot(a, b,  label = "Euler{}".format(i))

plt.legend()
plt.show()