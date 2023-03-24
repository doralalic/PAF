import matplotlib.pyplot as plt 
import numpy as np

v0 = float(input("upisi iznos brzine: "))
kut = float(input("upisi iznos kuta otklona u stupnjevima: "))


kut_radijani =  (kut / 180)*np.pi

vx0 = v0*np.cos(kut_radijani)
vy0 = v0*np.sin(kut_radijani)

print(vx0)
print(vy0)

t=0
dt=0.01
x=0 
y=0 
g=9.81

put = []
visina = []
vrijeme = []

while t<=10:
    put.append(x)
    visina.append(y)
    vrijeme.append(t)
    x = vx0*t
    vy = vy0 - g*t
    y = y + vy*t
    t = t + dt 
    
plt.plot(put, visina)
plt.show()

plt.plot(vrijeme , put)
plt.show()

plt.plot(vrijeme , visina)
plt.show()
