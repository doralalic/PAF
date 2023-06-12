import modul_seminar as modul
import numpy as np
import matplotlib as plt


def funkcija_1(x, v, t):
    
    f = 150
    return f

def funkcija_2(x, v, t):
    
    k = 50
    f = -k*x
    return f 

p1 = modul.particle(15, 5, 10, funkcija_1)
p1.plot_trajectory(0.01,10)

p2 = modul.particle(15, 5, 10, funkcija_2)
p2.plot_trajectory(0.01,10)

