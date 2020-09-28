# Optimización no lineal
## Método de Bisección utilizando Scilab
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

function y1=g(x)
    y1=-2*x-1
endfunction

X=linspace(a,b)
Y=f(X)
Y2=g(X)
plot(X,Y,'-r')
plot(X,Y2)
xgrid
xlabel('Eje X')
ylabel('Eje Y')
legend('Función','Derivada')

if g(a)*g(b)>0
    messagebox('No hay mínimos o máximos en el intervalo seleccionado','Error','info')
    abort
end

while abs(g(M))>tol
    if g(a)*g(M)>0
        a=M
        M=(a+b)/2
    else
        b=M
        M=(a+b)/2
    end
end
disp(M)

der2=(g(M)+g(M+tol))/tol
if der2>0 then
    disp('Se encontró un punto mínimo')
else
    disp('Se encontró un punto máximo')
end
```

### Resultado
 Método de Bisección para el cálculo de máximos y mínimos de funciones

  -0.5

 Se encontró un punto máximo
