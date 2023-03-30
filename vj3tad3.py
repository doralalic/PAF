import math
def aritm(x):
    q=sum(x)/len(x)
    return q 

x = [ 1, 2, 3,4,5,6,7,8,9,10]
a=aritm(x)
print(a)

def devijacija(x):
    a=aritm(x)
    suma=0
    for i in x:
        suma=suma+(i-a)**2
    y=math.sqrt(suma/ (len(x)*(len(x)-1)))
    return y
b=devijacija(x)
print(b)

    