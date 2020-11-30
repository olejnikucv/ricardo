import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import math
import tkinter
from tkinter import messagebox

def f(x):
    return np.exp(-x)-x

# Método de Bisección usando Python

tol=1e-6
a=-3
b=1
M=(a+b)/2

if f(a)*f(b)>0:
    messagebox.showerror("Error", "No hay raíces o hay más de dos raíces en el intervalo dado")
    sys.exit ()
    
print('M','f(M)',sep="  ")
while abs(f(M))>tol:
    if f(a)*f(M)>0:
        a=M
        M=(a+b)/2
    else:
        b=M
        M=(a+b)/2
        print(round(M,3),round(f(M),0),sep="   ")
        
x=np.linspace(-2,2,100) # Uso de linspace(a,b,n), permite crear un vector que va de _a_ a _b_ utilizando 100 puntos  
y=f(x)
plt.plot(x,f(x))
plt.plot(M,f(M),'ro')
grid()
show()
 
 