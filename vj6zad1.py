import numpy as np
import matplotlib.pyplot as plt
import harmonic_oscilator as HO

h=HO.HarmonicOscillator(1 ,3, 1,1,0.01)
t , x, v, a = h.update(10)

plt.subplot(1,3,1)
plt.title("x-t graf")
plt.plot(t,x)

plt.subplot(1,3,2)
plt.title("v-t graf")
plt.plot(t,v)

plt.subplot(1,3,3)
plt.title("a-t graf")
plt.plot(t,a)

plt.show()

