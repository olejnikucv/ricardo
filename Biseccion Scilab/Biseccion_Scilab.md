## Método de Bisección

### Problema:

Hallar las raíces de la siguiente función en el intervalo [4,20]

#### $$ y=x-tan(x) $$

![imagen.png](https://raw.githubusercontent.com/olejnikucv/ricardo/master/Biseccion%20Scilab/GraficoBiseccion.png)

<div class="alert alert-success">
  <strong> Código Método de Bisección utilizando Scilab</strong>
</div>


```python
clear, clc
// ---------------- Método de Bisección utilizando Scilab ---------------------
// ----------  Creación de la función -----------------------------------------
function y=f(x)
    y=x-tan(x)
endfunction
// ------ Gráfico de la función en un intervalo -------------------------------
X=linspace(0,20,1000)
Y=f(X)
plot(X,Y)
xgrid
title('Gráfico de la función')
xlabel('Eje X')
ylabel('Eje Y')
// ----------- Método de Bisección --------------------------------------------
function biseccion(f,a,b,tol)
M=(a+b)/2
if f(a)*f(b)>0
    messagebox('Hay una o más raíces en el intervalo seleccionado','Error','info') //Mensaje de error en scilab
    abort  // Return en Matlab
end

while abs(f(M))>tol
    if f(a)*f(M)>0
        a=M
        M=(a+b)/2
    else
        b=M
        M=(a+b)/2
    end
end
disp(M)
plot(M,f(M),'Or')
endfunction
//-----------------------------------------------------------------------------
tol=1e-6
biseccion(f,4.4,4.6,tol) 
biseccion(f,7.5,7.8,tol)
biseccion(f,10.8,10.99,tol)
biseccion(f,14,14.1,tol)
biseccion(f,17.1,17.25,tol)
//plot(M,f(M),'Or')
```

<div class="alert alert-info">
  <strong> Raíces de la función en el intervalo seleccionado</strong>
</div>

4.4934094

7.7252518

10.904122

14.066194

17.220755


---

*Creado por: Ricardo Olejnik*
