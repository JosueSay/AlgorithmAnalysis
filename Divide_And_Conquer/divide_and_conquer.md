---
header-includes:
  - \usepackage{amsmath}
  - \usepackage{amssymb}
  - \usepackage{fontspec}
  - \setmainfont{FiraCode Nerd Font}
  - \usepackage{setspace}
  - \setstretch{1.5}
  - \usepackage{fvextra}
  - \DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,commandchars=\\\{\}}
geometry: top=0.67in, bottom=0.67in, left=0.85in, right=0.85in
---

# Divide and Conquer

## Integrantes

- Christian Echeverría  221441
- Gustavo Cruz          22779
- Josué Say             22801
- Mathew Cordero        22982
- Pedro Guzmán          22111

## Ejercicio 1

Use el método de sustitución para determinar la solución a la siguiente recurrencia:

$ T(n) = 4T\left(\frac{n}{2}\right) + n $. La solución de acuerdo con el *Master Method* es $\Theta(n^2)$, pero usar la hipótesis $cn^2$ falla. Realice el procedimiento bajo esa hipótesis para comprobar que falla y luego modifique la hipótesis para que funcione.

## Solución de Recurrencia por Método de Sustitución

### Planteamiento Inicial
Tenemos la recurrencia $$T(n) = 4T\left(\frac{n}{2}\right) + n$$

Según el Teorema Maestro, esta recurrencia cae en el Caso 2, ya que $f(n) = n$ es polinomialmente menor que $n^2$ (donde $a=4$ y $b=2$). Por lo tanto, la solución debería ser $\Theta(n^2)$. Sin embargo, al intentar asumir $T(n) \leq cn^2$, la sustitución no funciona.

### Primera Hipótesis
Asumamos que $T(k) \leq ck^2$ para todo $k < n$. Sustituyendo en la recurrencia:

$$T(n) = 4T\left(\frac{n}{2}\right) + n$$

Para simplificar la sustitución, podemos considerar $n$ como una potencia de 2 sin pérdida de generalidad:

$$T(n) = 4c\left(\frac{n^2}{4}\right) + n = cn^2 + n$$

Para que la hipótesis se mantenga, necesitaríamos:
$$cn^2 + n \leq cn^2$$

Esto implicaría que $n \leq 0$, lo cual es imposible ya que $n > 0$. Por lo tanto, la hipótesis inicial falla.

### Cambio de hipótesis Hipótesis
Debido a que la hipótesis inicial falla, se realizaran cambios para la hipótesis de la forma $$T(n) \leq cn^2 - dn$$ para algunas constantes $c$ y $d$.

Sustituyendo en la recurrencia:
$$\begin{align*}
T(n) &= 4T\left(\frac{n}{2}\right) + n \\
&= 4\left(c\left(\frac{n^2}{4}\right) - d\left(\frac{n}{2}\right)\right) + n \\
&= 4c\left(\frac{n^2}{4}\right) - 4d\left(\frac{n}{2}\right) + n \\
&= cn^2 - 2dn + n
\end{align*}$$

Para que se cumpla $T(n) \leq cn^2 - dn$, necesitamos:
$$cn^2 - 2dn + n \leq cn^2 - dn$$

Simplificando:
1. Se resta $cn^2$ de ambos lados:
   $$-2dn + n \leq -dn$$
2. Agrupamos términos:
   $$(-2d + 1)n + (-dn) = (-3d + 1)n \leq 0$$

Para que esta desigualdad se cumpla para todo $n > 0$, se necesita:
$$-3d + 1 \leq 0 \implies d \geq \frac{1}{3}$$

### Verificación para Casos Base
Por ultimo se verifican los pequeños valores de $n$:

Para $n = 2$:
$$T(2) = 4c - 4d + 2$$
Debe cumplir:
$$4c - 4d + 2 \leq 4c - 2d \implies -4d + 2 \leq -2d \implies -2d + 2 \leq 0 \implies d \geq 1$$

Para $n = 4$:
$$T(4) = 16c - 8d + 4$$
Debe cumplir:
$$16c - 8d + 4 \leq 16c - 4d \implies -8d + 4 \leq -4d \implies -4d + 4 \leq 0 \implies d \geq 1$$

### Conclusión
La solución correcta requiere tomar $d \geq 1$. Con $d = 1$, tenemos:
$$T(n) \leq cn^2 - n$$

Esta forma satisface tanto la recurrencia como los casos base, confirmando que $T(n) = \Theta(n^2)$. La hipótesis inicial de $cn^2$ falló porque necesitábamos el término lineal negativo $-n$ para manejar los términos de orden inferior que surgían durante la sustitución.

## Ejercicio 2

Resuelva la recurrencia $ T(n) = 3T(\sqrt{n}) + \log_2 n $. Para hacerlo demuestre primero que se puede convertir en $ S(m) = 3S\left(\frac{m}{2}\right) + m $; y luego resuelva esta recurrencia con el método de sustitución. Con este resultado provea la respuesta para la recurrencia original.

**Hint**: note que, en $ S(m) $, $ m $ parece ocupar el lugar que $\log_2 n$ tiene en $ T(n) $.

## Ejercicio 3

Use un árbol de recursión para proveer una cota ajustada a la recurrencia $ T(n - a) + T(a) + cn $, donde $ a \ge 1 $, $ c > 0 $; ambas constantes. Puede suponer que $ n $ es múltiplo de $ a $.

## Ejercicio 4

Use el *Master Method* (si es posible) para dar cotas ajustadas a las siguientes recurrencias:  

### $ T(n) = 2T\left(\frac{n}{4}\right) + \sqrt{n} $  

### $ T(n) = 4T\left(\frac{n}{2}\right) + n^2 \log_2 n $

## Ejercicio 5

Dé una recurrencia que cumpla con las condiciones del tercer caso del *Master Method* excepto la condición de regularidad.

## Ejercicio 6

Sea $ G = (V, E) $ un grafo dirigido. Deseamos determinar si existe un camino que conecte a dos nodos, $ u, v \in V $; esto se conoce como el *problema de conectividad-st* o *STCON*. El algoritmo de Savitch, presentado a continuación, determina si existe un camino con tamaño máximo $ 2^i $ entre dos nodos $ u, v $ del grafo $ G $:

![Algorithm Savitch](./images/savitch.png "Algorithm Savitch")

<!-- **Algorithm 3.4 Savitch**  
1: if $i = 0$ then  
2: &emsp; if $u = v$ then  
3: &emsp;&emsp; return T  
4: &emsp; else if $(u, v)$ is an edge then  
5: &emsp;&emsp; return T  
6: &emsp; end if  
7: else  
8: &emsp; for every vertex $w$ do  
9: &emsp;&emsp; if $R(G, u, w, i - 1)$ and $R(G, w, v, i - 1)$ then  
10: &emsp;&emsp;&emsp; return T  
11: &emsp;&emsp; end if  
12: &emsp; end for  
13: end if  
14: return F   -->

Identifique las partes *Divide*, *Conquer* y *Combine* de este algoritmo, y determine (con notación asintótica) una cota superior para su tiempo de ejecución si se ejecuta para $i = \log_2 n$, donde $n$ es el número de vértices en el grafo. El tiempo de ejecución que encuentre, ¿será indicador de eficiencia (es decir, será que el algoritmo es “rápido”) o de ineficiencia (“lento”)?
