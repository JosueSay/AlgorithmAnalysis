## Ejemplo con 4 vertices
Consideremos el siguiente grafo:

- **Vértices:** $V = \{A, B, C, D\}$
- **Aristas y pesos:**
  - $A \to B$ con peso 1
  - $A \to C$ con peso 4
  - $B \to C$ con peso 2
  - $B \to D$ con peso 6
  - $C \to D$ con peso 1
- **Vértice origen:** $s = A$

El objetivo es hallar la **distancia mínima** desde $A$ hasta cada vértice utilizando el algoritmo de Bellman-Ford.

---

### 1. Inicialización

Definimos la tabla $d[k,v]$ donde $k$ indica el número de iteraciones (o el máximo número de aristas permitidas).

Para $k = 0$:
- $d[0,A] = 0$ (origen)
- $d[0,B] = +\infty$
- $d[0,C] = +\infty$
- $d[0,D] = +\infty$

| **k** |  d(A)  |   d(B)   |   d(C)   |   d(D)   |
|:-----:|:------:|:--------:|:--------:|:--------:|
|   0   |   0    |   ∞      |   ∞      |   ∞      |

---

### 2. Primera Iteración ($k = 1$)

Se relajan todas las aristas usando los valores de $d[0,\cdot]$:

1. **Arista $A \to B$:**  
   $d[1,B] = \min(d[0,B],\, d[0,A] + 1) = \min(+\infty,\, 0+1) = 1.$

2. **Arista $A \to C$:**  
   $d[1,C] = \min(d[0,C],\, d[0,A] + 4) = \min(+\infty,\, 0+4) = 4.$

3. **Arista $B \to C$:**  
   Como $d[0,B] = +\infty$, no mejora $d[1,C]$.

4. **Arista $B \to D$:**  
   No se actualiza, pues $d[0,B] = +\infty$.

5. **Arista $C \to D$:**  
   No se actualiza, pues $d[0,C] = +\infty$.

La tabla tras la primera iteración es:

| **k** |  d(A) |   d(B)  |  d(C) |   d(D)   |
|:-----:|:-----:|:-------:|:-----:|:--------:|
|   0   |   0   |   ∞     |   ∞   |    ∞     |
|   1   |   0   |   1     |   4   |    ∞     |

---

### 3. Segunda Iteración ($k = 2$)

Usamos los valores de $d[1,\cdot]$ para relajar nuevamente:

1. **Arista $A \to B$:**  
   $d[2,B] = \min(d[1,B],\, d[1,A] + 1) = \min(1,\, 0+1) = 1.$

2. **Arista $A \to C$:**  
   $d[2,C] = \min(d[1,C],\, d[1,A] + 4) = \min(4,\, 0+4) = 4.$

3. **Arista $B \to C$:**  
   $d[2,C] = \min(4,\, d[1,B] + 2) = \min(4,\, 1+2) = 3.$
   (Se mejora $d(C)$ de 4 a 3.)

4. **Arista $B \to D$:**  
   $d[2,D] = \min(+\infty,\, d[1,B] + 6) = \min(+\infty,\, 1+6) = 7.$

5. **Arista $C \to D$:**  
   $d[2,D] = \min(7,\, d[1,C] + 1) = \min(7,\, 4+1) = 5.$
   (Se mejora $d(D)$ de 7 a 5.)

La tabla tras la segunda iteración es:

| **k** |  d(A) |  d(B) |  d(C) |  d(D) |
|:-----:|:-----:|:-----:|:-----:|:-----:|
|   1   |   0   |   1   |   4   |   ∞   |
|   2   |   0   |   1   |   3   |   5   |

---

### 4. Tercera Iteración ($k = 3$)

Finalmente, se relajan nuevamente las aristas usando $d[2,\cdot]$:

1. **Arista $A \to B$:**  
   $d[3,B] = \min(d[2,B],\, d[2,A] + 1) = \min(1,\, 0+1) = 1.$

2. **Arista $A \to C$:**  
   $d[3,C] = \min(d[2,C],\, d[2,A] + 4) = \min(3,\, 0+4) = 3.$

3. **Arista $B \to C$:**  
   $d[3,C] = \min(3,\, d[2,B] + 2) = \min(3,\, 1+2) = 3.$

4. **Arista $B \to D$:**  
   $d[3,D] = \min(d[2,D],\, d[2,B] + 6) = \min(5,\, 1+6) = 5.$

5. **Arista $C \to D$:**  
   $d[3,D] = \min(5,\, d[2,C] + 1) = \min(5,\, 3+1) = 4.$
   (Se mejora $d(D)$ de 5 a 4.)

La tabla final queda:

| **k** |  d(A) |  d(B) |  d(C) |  d(D) |
|:-----:|:-----:|:-----:|:-----:|:-----:|
|   2   |   0   |   1   |   3   |   5   |
|   3   |   0   |   1   |   3   |   4   |

---

### Conclusión

Después de $|V|-1 = 3$ iteraciones, las **distancias mínimas** desde el vértice $A$ son:

- $d(A) = 0$
- $d(B) = 1$
- $d(C) = 3$
- $d(D) = 4$

## Subestructura optima y subproblemas traslapdos

En este algoritmo el problema principal es encontrar un camino mas corto entre los vertices $S$ y $v$. 

Los subproblemas en los que se puede dividir son: 
* Encontrar el camino más corto entre v y cada i (1 ≤ i ≤ |V|-1), usando i aristas. 
* Por ejemplo, en el camino A→B→C→D, el camino más corto a $D$ depende del camino más corto a $C$, que a su vez depende del camino más corto a $B$.

#### Subproblemas traslapados
Los subproblemas se superponen porque el cálculo de $d[v]$ puede depender de $d[u]$ para múltiples vértices $u$.

**Ejemplo:** $d[D]$ se actualiza primero usando $B$ y luego usando $C$.

## Recurrencia 

**Relación de Recurrencia**

La relación de recurrencia que define el valor óptimo d[v] es:

$$d[v] = \min_{(u,v) \in E} (d[u] + w(u,v))$$

* Esto significa que la distancia más corta a $v$ es el mínimo de las distancias a sus predecesores $u$ más el peso de la arista $(u,v)$.
