import numpy as np
import matplotlib.pyplot as plt

class HarmonicOscillator:
    def __init__(self, masa, k , x0, v0, dt=0.01):
        self.masa = masa
        self.k = k
        self.x0 = x0
        self.v0 = v0
        self.dt = dt

        self.lista_x = []
        self.lista_v = []
        self.lista_a = []
        self.lista_t = []
        self.a=[]  

    def update(self, t):

        t0 = 0.0

        while t0<=t:
          a = (-self.k / self.masa )* self.x0
          self.lista_a.append(a)
          self.v0 = self.v0 + a * self.dt
          self.lista_v.append(self.v0)
          self.x0 = self.x0 + self.v0 * self.dt
          self.lista_x.append(self.x0)
          self.lista_t.append(t0)
          t0 = t0 + self.dt

        return self.lista_t, self.lista_x, self.lista_v, self.lista_a

        



