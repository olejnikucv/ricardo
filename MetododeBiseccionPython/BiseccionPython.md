# Método de Bisección utilizando Python

```python
import math
import scipy
from pylab import *
import matplotlib.pyplot as plt
ERROR = 1E-6

# -------------------------- Valores iniciales --------------------------------
x0 = 0
x1 = 2
#------------------------------------------------------------------------------

#----------------------- Definición de la función -----------------------------
def ec(x):
    return (math.exp(-x)-x)
#------------------------------------------------------------------------------

#------------------------- Método de Bisección --------------------------------
    
M=(x0+x1)/2    # Primer valor de punto medio
fM = ec(M)     # Función evaluada en el punto medio 
if ec(x0)*ec(x1)<0:
    while abs(ec(M))>ERROR:
        if ec(x0)*ec(M)>0:
            x0=M
            M=(x0+x1)/2
        if ec(x1)*ec(M)>0:
            x1=M
            M=(x0+x1)/2
    print('El valor de la raíz es')
    print(M)
else:
    print('No hay raíces o hay mas de una raíz en el intervalo seleccionado')        
            
# ------------- Gráfico de función y gráfico del punto de corte ---------------
xvals = scipy.arange(-5,5,0.1)
f = lambda x: exp(-x)-x
f(xvals)
a=xvals
b=f(xvals)
plot(a,b)
grid()
punto=plot([M],[ec(M)],'ro')

texto1 = text(-4, 100, r'$exp(-x)-x$', fontsize=15)
title('Función')
xlabel('x')
ylabel('y')

show()
# -----------------------------------------------------------------------------
```
