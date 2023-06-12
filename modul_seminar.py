import matplotlib.pyplot as plt
import numpy as np

class particle:
    
    def __init__(self, m, x0, v0, funkcija):
        
        self.m = m
        self.x0 = x0
        self.v0 = v0
        self.f = funkcija
        self.t0 = 0
        self.a0 = self.f(self.x0,self.v0,self.t0)/self.m

        self.x = []
        self.v = []
        self.a = []
        self.t = []
       
    
    def move(self,dt,t):
            
            n = int(t/dt)
            for i in range(n):
                
                self.a0 = self.f(self.x0, self.v0, self.t0)/self.m
                self.v0 = self.v0 + self.a0*dt
                self.x0 = self.x0 + self.v0*dt
                self.t0 += dt
                
                self.x.append(self.x0)
                self.v.append(self.v0)
                self.a.append(self.a0)
                self.t.append(self.t0)
            
            return self.x, self.v, self.a, self.t
    
    
    def plot_trajectory(self,dt,t):
        x,v,a,t = self.move(dt,t)

        plt.subplot(2,4,2)
        plt.title("x-t graf")
        plt.plot(t,x)
        
        plt.subplot(2,4,3)
        plt.title("v-t graf")
        plt.plot(t,v)
        
        plt.subplot(2,4,4)
        plt.title("a-t graf")
        plt.plot(t,a)
        
        plt.show()       
    


