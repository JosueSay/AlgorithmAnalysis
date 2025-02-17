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

## Ejercicio 2

Resuelva la recurrencia $ T(n) = 3T(\sqrt{n}) + \log_2 n $. Para hacerlo demuestre primero que se puede convertir en $ S(m) = 3S\left(\frac{m}{2}\right) + m $; y luego resuelva esta recurrencia con el método de sustitución. Con este resultado provea la respuesta para la recurrencia original.

**Hint**: note que, en $ S(m) $, $ m $ parece ocupar el lugar que $\log_2 n$ tiene en $ T(n) $.

## Ejercicio 3

Use un árbol de recursión para proveer una cota ajustada a la recurrencia $ T(n - a) + T(a) + cn $, donde $ a \ge 1 $, $ c > 0 $; ambas constantes. Puede suponer que $ n $ es múltiplo de $ a $.

### Solución

El problema nos indica que la función $ T(n) $ se divide en dos subproblemas: uno de tamaño $ T(n-a) $ y otro constante $ T(a) $. El tiempo total de ejecución en cada nivel de recursión es la suma de estos términos más un costo lineal adicional de $ cn $.

#### Iteración 1

- Cantidad de elementos: $ cn $
- Subproblema 1: $ c(n-a) $
- Subproblema 2: $ c(a) $
- **Total de tiempo de ejecución:** $ cn $, ya que:

  $$ c(n-a) + c(a) = cn - ca + ca = cn $$

#### Iteración 2

- Subproblema 1: $ c(n-a) $ se subdivide en:
  - Subproblema 1.1: $ c(n-a-a) = c(n-2a) $
  - Subproblema 1.2: $ c(a) $
- Subproblema 2: $ c(a) $
- **Total de tiempo de ejecución:** $ cn $, ya que:

  $$ c(n-2a) + c(a) + c(a) = cn - 2ca + ca + ca = cn $$

Siguiendo este patrón, podemos ver que en cada nivel la suma total del costo sigue siendo $ cn $.

![Árbol de Recursión](./images/arbol_recursion.png "Árbol de Recursión")

#### Determinación de la cantidad de niveles

El proceso continúa hasta que el subproblema grande $ c(n-ka) $ sea igual a la constante $ c(a) $. Para encontrar el número de niveles $ k $, resolvemos:

$$ c(n-ka) = c(a) $$
$$ n-ka = a $$
$$ n-a = ka $$
$$ k = \frac{n-a}{a} = \frac{n}{a} - 1 $$

Por lo tanto, el árbol de recursión tiene $ k $ niveles.

#### Cálculo del tiempo total de ejecución

El tiempo total de ejecución es el número de niveles multiplicado por el costo de cada nivel:

$$ T(n) = k \cdot cn $$

Sustituyendo $ k = \frac{n}{a} - 1 $:

$$ T(n) = \left( \frac{n}{a} - 1 \right) cn $$

Distribuyendo:

$$ T(n) = \frac{cn^2}{a} - cn $$

El término dominante es $ \frac{cn^2}{a} $, ya que crece más rápido que $ cn $ cuando $ n $ tiende a infinito. Los factores constantes $ c $ y $ a $ no afectan la notación asintótica, por lo tanto, la cota ajustada es:

$$ T(n) = O(n^2) $$

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
