import matplotlib.pyplot as plt
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

while t<=10:
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
