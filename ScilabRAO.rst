Uso de fsolve en Scilab
=======================

Hallar la ra�z de la funci�n:

.. math::
  y =e^{-x}-x 

Ejemplo
*******

.. code-block:: scilab

   // Uso de fsolve
   clear, clc

   function y=f(x)
     y = exp(-x)-x  // Funci�n ejemplo
   endfunction

   R=fsolve(0,f)    // Se define primero el valor inicial y posteriormente la funci�n

   disp('El valor de la ra�z es:')
   disp(R)

.. Note::
      Alternativa al fsolve de Matlab para hallar ra�ces de funciones no lineales

Uso de ode en Scilab
=======================

Hallar la soluci�n de la ecuaci�n diferencial:

.. math::
   y =x \cdot y 

Con:

.. math::
   x=0, y=1

En x=1

Ejemplo
*******

.. code-block:: scilab

   // Uso de ode para soluci�n de ecuaciones diferenciales ordinarias
   clear, clc
   
   function z=g(x,y)  
      z = x*y             // Se define la ecuaci�n diferencial
   endfunction

   ode([0,1],0,1,g)       // Donde [0,1] es condici�n inicial, el valor inicial y final respectivamente y la funci�n 



.. Note::
      Alternativa al ode45 de Matlab para soluci�n de ecuaciones diferenciales ordinarias.