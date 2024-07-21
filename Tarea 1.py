import numpy as np
from matplotlib import pyplot as plt
#import matplotlib.pyplot as plt

def seno(a):
    return np.sin(a)

x = np.linspace(0, 2*np.pi, 100)

f=seno(x)

plt.figure()
plt.plot(x,f) #grafica la funcion
#plt.plot(x,f, "o") #grafica los puntos de la funcion
plt.grid(True) #cuadricula de la grafica
plt.show()