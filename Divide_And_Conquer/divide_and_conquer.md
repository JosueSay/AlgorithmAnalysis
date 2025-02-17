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

## Ejercicio 4

Use el *Master Method* (si es posible) para dar cotas ajustadas a las siguientes recurrencias:  

### T(n) = 2T\left(\frac{n}{4}\right) + \sqrt{n} $  

### $ T(n) = 4T\left(\frac{n}{2}\right) + n^2 \log_2 n $

## Ejercicio 5

Dé una recurrencia que cumpla con las condiciones del tercer caso del *Master Method* excepto la condición de regularidad.

## Ejercicio 6

Sea $ G = (V, E) $ un grafo dirigido. Deseamos determinar si existe un camino que conecte a dos nodos, $ u, v \in V $; esto se conoce como el *problema de conectividad-st* o *STCON*. El algoritmo de Savitch, presentado a continuación, determina si existe un camino con tamaño máximo $ 2^i $ entre dos nodos $ u, v $ del grafo $ G $:

![Algorithm Savitch](./images/savitch.png "Algorithm Savitch")

<!-- **Algorithm 3.4 Savitch**  
1: if \(i = 0\) then  
2: &emsp; if \(u = v\) then  
3: &emsp;&emsp; return T  
4: &emsp; else if \((u, v)\) is an edge then  
5: &emsp;&emsp; return T  
6: &emsp; end if  
7: else  
8: &emsp; for every vertex \(w\) do  
9: &emsp;&emsp; if \(R(G, u, w, i - 1)\) and \(R(G, w, v, i - 1)\) then  
10: &emsp;&emsp;&emsp; return T  
11: &emsp;&emsp; end if  
12: &emsp; end for  
13: end if  
14: return F   -->

Identifique las partes *Divide*, *Conquer* y *Combine* de este algoritmo, y determine (con notación asintótica) una cota superior para su tiempo de ejecución si se ejecuta para \(i = \log_2 n\), donde \(n\) es el número de vértices en el grafo. El tiempo de ejecución que encuentre, ¿será indicador de eficiencia (es decir, será que el algoritmo es “rápido”) o de ineficiencia (“lento”)?
