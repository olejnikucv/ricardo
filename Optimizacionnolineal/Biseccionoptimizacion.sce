clear, clc

disp('Método de Bisección para el cálculo de máximos y mínimos de funciones')
//----------- Método de Bisección para cálculo de máximos y mínimos ---------//
a=-5
b=5
tol=1e-8
M=(a+b)/2

function y=f(x)
    y=x.^2-x+3
endfunction

function y2=g(x)
    y2=2*x-1
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
