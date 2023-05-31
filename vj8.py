import matplotlib.pyplot as plt
import numpy as np
import em 

E = (0, 0, 0)
B = (0, 0, 1)
v = (0.1, 0.1, 0.1)
s = (0, 0, 0)

p1 = em.Particle(0.5, 1, E, B, v, s)
p2 = em.Particle(0.5, -1, E, B, v, s)

p = p1.path(17)
e = p2.path(17)

graph = plt.axes(projection = "3d")
graph.view_init(15, 25)
graph.plot(p[:, 0], p[:, 1], p[:, 2], label = 'p+')
graph.plot(e[:, 0], e[:, 1], e[:, 2], label = 'e-')
graph.legend()
plt.show()