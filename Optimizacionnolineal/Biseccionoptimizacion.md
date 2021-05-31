# Optimización no lineal
## Método de Bisección utilizando Scilab utilizando la aproximación de la primera derivada con definición por límite
Calcular el máximo o mínimo de la siguiente función e el intervalo (-5,5)
<p align="center"><img align="center" src="https://i.upmath.me/svg/%20y%3Dx%5E2-x%2B3%20" alt=" y=x^2-x+3 " /></p>

![](https://github.com/olejnikucv/ricardo/blob/master/Optimizacionnolineal/Grafico.png)

```scilab
clear, clc

disp('Método de Bisección para el cálculo de máximos y mínimos de funciones')
//----------- Método de Bisección para cálculo de máximos y mínimos ---------//
a=-5
b=5
tol=1e-8
M=(a+b)/2

function y=f(x)
    y=-x.^2-x+3
endfunction

X=linspace(a,b)
Y=f(X)
Y2 = (f(X+tol)-f(X))/tol  // Utilizando derivada por definición
plot(X,Y,'-r')
plot(X,Y2)
xgrid
xlabel('Eje X')
ylabel('Eje Y')
legend('Función','Derivada')

der_a = (f(a+tol)-f(a))/tol
der_b = (f(b+tol)-f(b))/tol

if der_a*der_b > 0
    messagebox('No hay mínimos o máximos en el intervalo seleccionado','Error','info')
    abort
end

der_M = (f(M+tol)-f(M))/tol

while abs((f(M+tol)-f(M))/tol) > tol
    der_a = (f(a+tol)-f(a))/tol
    der_b = (f(b+tol)-f(b))/tol
    der_M = (f(M+tol)-f(M))/tol
    if der_a*der_M>0
        a=M
        M=(a+b)/2
    else
        b=M
        M=(a+b)/2
    end
end
disp(M)

der2=(f(M)+f(M+tol))/tol
if der2 > 0 then
    disp('Se encontró un punto mínimo')
else
    disp('Se encontró un punto máximo')
end
```

### Resultado
 Método de Bisección para el cálculo de máximos y mínimos de funciones

  -0.5

 Se encontró un punto máximo
