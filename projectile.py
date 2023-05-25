import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, masa, v0, x0, y0, phi, otpor, C, A, dt = 0.001):
        self.dt = dt
        self.masa = masa
        self.phi = (phi / 180) * np.pi
        self.vx = v0 * np.cos(self.phi)
        self.vy = v0 * np.sin(self.phi)
        self.x0 = x0
        self.y0 = y0
        self.otpor = otpor
        self.C = C
        self.A = A


        self.list_ax = []
        self.list_ay = []
        self.list_vx = []
        self.list_vy = []
        self.list_x  = []
        self.list_y  = []
        self.list_t =  []

    def Euler(self):
        while self.y0 >= 0:
          ax = -np.sign(self.vx) * ((self.otpor * self.C * self.A) / 2*self.masa) * self.vx**2
          self.list_ax.append(ax)
          self.vx = self.vx + ax * self.dt
          self.list_vx.append(self.vx)
          self.x0 = self.x0 + self.vx * self.dt
          self.list_x.append(self.x0)
          ay = -9.81 - (np.sign(self.vy) * ((self.otpor * self.C * self.A) / 2 * self.masa) * self.vy**2 )
          self.list_ay.append(ay)
          self.vy = self.vy + ay * self.dt
          self.list_vy.append(self.vy)
          self.y0 =  self.y0 + self.vy * self.dt
          self.list_y.append(self.y0)

        return self.list_x, self.list_y
    
        g=9.81

    def Runge_Kutta(self):
        g = 9.81
        t0 = 0.0
        variable = (self.otpor * self.C * self.A) / (2 * self.masa)
        
        while self.y0 >= 0:
            k1vx = (- np.sign(self.vx) * variable * (self.vx)**2) * self.dt
            k1x = self.vx * self.dt
            k2vx = (- np.sign(self.vx + (k1vx / 2)) * variable * (self.vx + (k1vx / 2))**2) * self.dt
            k2x = (self.vx + (k1vx / 2)) * self.dt
            k3vx = (- np.sign(self.vx + (k2vx / 2)) * variable * (self.vx + (k2vx / 2))**2) * self.dt
            k3x = (self.vx + (k2vx / 2)) * self.dt
            k4vx = (- np.sign(self.vx + (k3vx / 2)) * variable * (self.vx + (k3vx / 2))**2) * self.dt
            k4x = (self.vx + (k3vx / 2)) * self.dt
            
            self.vx = self.vx + (1/6) * (k1vx + 2*k2vx + 2*k3vx + k4vx)
            self.x0 = self.x0 + (1/6) * (k1x + 2*k2x + 2*k3x + k4x)
            
            k1vy = (- g - np.sign(self.vy) * variable * (self.vy)**2) * self.dt
            k1y = self.vy * self.dt
            k2vy = (- g - np.sign(self.vy + (k1vy / 2)) * variable * (self.vy + (k1vy / 2))**2) * self.dt
            k2y = (self.vy + (k1vy / 2)) * self.dt
            k3vy = (- g - np.sign(self.vy + (k2vy / 2)) * variable * (self.vy + (k2vy / 2))**2) * self.dt
            k3y = (self.vy + (k2vy / 2)) * self.dt
            k4vy = (- g - np.sign(self.vy + (k3vy / 2)) * variable * (self.vy + (k3vy / 2))**2) * self.dt
            k4y = (self.vy + (k3vy / 2)) * self.dt
            
            self.vy = self.vy + (1/6) * (k1vy + 2*k2vy + 2*k3vy + k4vy)
            self.y0 = self.y0 + (1/6) * (k1y + 2*k2y + 2*k3y + k4y)
            
            t0 = t0 + self.dt
            
            self.list_t.append(t0)
            self.list_x.append(self.x0)
            self.list_y.append(self.y0)
            
            
        return self.list_x, self.list_y

           
           