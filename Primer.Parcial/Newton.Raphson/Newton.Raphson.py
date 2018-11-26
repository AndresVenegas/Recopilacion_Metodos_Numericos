def f(x):
    return x**4-8.6*x**3-35.51**2+464*x-998.46

def fprima(x):
    return 4*x**3-25.8*x**2-71.02*x+464

x0 = 7
itera = 0
for i in range(100):
    itera += 1
    xr = x0 - f(x0)/fprima(x0)
    if abs(f(xr)) < 0.000001:
        break
    x0 = xr
    
print("La raiz es %.5f"%x0)
print("Usando %i iteraciones"%itera)
