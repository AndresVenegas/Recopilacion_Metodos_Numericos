# ejemplo del paracaidas
import math
import numpy as np
import matplotlib.pyplot as plt

def fun(c):
    return (c**2-10)
arrayLen = 100
cIni = 0
cEnd = 30
carray = np.linspace (cIni,cEnd,arrayLen)
fcarray = np.zeros(arrayLen)

for i in range(arrayLen):
    fcarray[i] = fun(carray[i])
plt.plot(carray,fcarray)
plt.grid()

c0 = 3
c1 = 3.2
maxIter = 100
itera = 0
for i in range(maxIter):
    itera += 1
    fc0 = fun(c0)
    fc1 = fun(c1)
    if fc0 * fc1 >0:
        print("No hay raiz en este rango")
        break
    cr = c0 -((fc1*(c1-c0))/(fc0-fc1))
    fcr = fun(cr)
    if fc0 * fcr < 0:
        c1 = cr
    else:
        c0 = cr
    if abs(fcr) < 0.005:
        break
print ("La raiz es %.5f"%c0)
print ("Con iteraciones %i"%itera )
