# Estilos para Markdown (archivos .md)

```markdown
# Titulo 1
## Titulo 2
### Titulo 3
- Guion al comienzo marcará viñeta
** ** Negrillas
* * italico
Las ecuaciones en formato Latex (Se puede utilizar upmath https://upmath.me/ y hacer la conversión a formato MD)
- - - Línea de separación
<br> puede hacer un salto de linea
```
- - -
<br>
Ejemplo de formato látex:
<br>
<br>
<img src="https://i.upmath.me/svg/%20y%3D2x%2B1%20" alt=" y=2x+1 " />


### Código o comando
Mostrar o resaltar un código o comando se puede realizar utilizando el comando entre \```Comando``` o bien 
\<code> Comando \</code>

<code> 
  Probando una linea de código
  import numpy as np
  A=np.array([1,2,3,4])
</code>

- - - 
### Código en Python u otro lenguaje soportado 
Se puede utilizar el comando \```python u \```otrolenguaje

```python
import numpy as np
A=np.array([1,2,3,4])
print(A)
```
- - -
### Citas textuales

The overriding design goal for Markdown's
<code> > formatting syntax is to make it as readable </code>
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions.

- - - 
```markdown
# Tabla de contenidos
1. [Example](#example)
2. [Example2](#example2)
3. [Third Example](#third-example)
4. [Fourth Example](#fourth-examplehttpwwwfourthexamplecom)


## Example
## Example2
## Third Example
## [Fourth Example](http://www.fourthexample.com) 
```
