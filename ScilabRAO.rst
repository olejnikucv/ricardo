Uso de fsolve en Scilab
=======================

Hallar la raíz de la función:

.. math::
  y =e^{-x}-x 

Ejemplo
*******

.. code-block:: scilab

   // Uso de fsolve
   clear, clc

   function y=f(x)
     y = exp(-x)-x  // Función ejemplo
   endfunction

   R=fsolve(0,f)    // Se define primero el valor inicial y posteriormente la función

   disp('El valor de la raíz es:')
   disp(R)

.. Note::
      Alternativa al fsolve de Matlab para hallar raíces de funciones no lineales

Uso de ode en Scilab
=======================

Hallar la solución de la ecuación diferencial:

.. math::
   y =x \cdot y 

Con:

.. math::
   x=0, y=1

En x=1

Ejemplo
*******

.. code-block:: scilab

   // Uso de ode para solución de ecuaciones diferenciales ordinarias
   clear, clc
   
   function z=g(x,y)  
      z = x*y             // Se define la ecuación diferencial
   endfunction

   ode([0,1],0,1,g)       // Donde [0,1] es condición inicial, el valor inicial y final respectivamente y la función 



.. Note::
      Alternativa al ode45 de Matlab para solución de ecuaciones diferenciales ordinarias.