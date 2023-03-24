import matplotlib.pyplot as plt 
import numpy as np
def jednoliko_gibanje(f, m, N):
    f = float(input("upisi silu u N: "))
    m = float(input("upisi masu u kg: "))

    a = f / m 
    print(a) 

    akceleracija = []
    brzina = []
    put = []
    vrijeme = []

    a=0
    v=0
    s=0
    dt=0.01
    t=0

    while t<N:
         akceleracija.append(a)
         brzina.append(v)
         put.append(s)
         vrijeme.append(t)
         v = v + a*dt
         s = s +  (a*t*t) / 2
         t = t + dt

    plt.plot(vrijeme, akceleracija )
    plt.show()

    plt.plot(vrijeme, brzina)
    plt.show()

    plt.plot(vrijeme , put)
    plt.show()

def kosi_hitac(v0, kut, N):
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

