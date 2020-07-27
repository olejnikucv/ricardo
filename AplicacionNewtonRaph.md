# Raíces de funciones no lineales

### **Problema:**

La siguiente ecuación muestra el tiempo necesario para alcanzar una concentración deseada de un compuesto A en mol/L

### <img align="center" src="https://i.upmath.me/svg/%20t%3D%20%5Cfrac%7B1%7D%7B38.176%7D%5Cleft%20%5B%20%5Cfrac%7B1%7D%7B_%7BC_%7BA%7D%7D%7D%20-%20279.4%2Bln%5Cleft%20(%20%5Cfrac%7B0.898C_%7BA%7D%7D%7B0.0014%2B0.5C_%7BA%7D%7D%20%5Cright%20)%5Cright%20%5D%20" alt=" t= \frac{1}{38.176}\left [ \frac{1}{_{C_{A}}} - 279.4+ln\left ( \frac{0.898C_{A}}{0.0014+0.5C_{A}} \right )\right ] " />

Calcule la concentración de A despues de 10 segundos.

### **Newton Raphson Method**

```
    function y=f(x)
        y=10-((1/38.176)*((1./x)-279.4+log(0.898.*x/(0.0014+0.5.*x))))
    endfunction
    tol=1e-6
    x0=0.001
    der=(f(x0+tol)-f(x0))/tol
    i=0
    // ----------- Método de Newton Raphson ----------------------------------------
    while abs(f(x0))>tol
        if i==30   //Número máximo de 
        messagebox('Hay un punto de inflexión cerca del valor inicial seleccionado o no hay raíces reales','Error','info') 
        abort  
        end
    i=i+1
    x0=x0-(f(x0)/der)
    der=(f(x0+tol)-f(x0))/tol
    end
```

**El valor de la raíz es:**

   **R=1.51D-03**

**Comparando con la solución obtenida de solver**

´´´ R=fsolver(0.001,f) ´´´

**R=1.51D-03**

