# Knapsack problem fraccionado - Greedy Choice Property

## Integrantes

- Christian Echeverría  221441
- Gustavo Cruz          22779
- Josué Say             22801
- Mathew Cordero        22982
- Pedro Guzmán          22111

## Definición del Problema

El **problema de la mochila fraccionada** consiste en seleccionar elementos con cierto peso y valor para maximizar el beneficio sin exceder la capacidad de una mochila.

Un ladrón tiene una mochila con capacidad limitada y dispone de **n** objetos, cada uno con:

- **Peso**: $w_i$ (kg, lb, etc.).  
- **Valor**: $v_i$ (precio de venta, utilidad, etc.).

El objetivo es maximizar el valor robado sin exceder el peso permitido. En este caso, los objetos pueden **partirse** y robarse en fracciones.

## Definición Matemática

Dado un conjunto de $n$ elementos:

- Pesos:  
$$w_1, w_2, w_3, ..., w_n$$
- Valores:  
$$v_1, v_2, v_3, ..., v_n$$

Queremos maximizar la siguiente función objetivo:
$$\sum_{i=1}^{n} x_i v_i$$

Sujeto a la restricción de capacidad:
$$\sum_{i=1}^{n} x_i w_i \leq W$$

Y la restricción de fraccionamiento:
$$0 \leq x_i \leq 1, \quad \forall i$$

Donde:

- $x_i$ es la **fracción del objeto $i$** que se toma.  
- $W$ es la **capacidad máxima** de la mochila.

## Estrategia Greedy

Para maximizar el valor total sin exceder la capacidad de la mochila, se sigue esta estrategia:

1. **Calcular el ratio valor/peso** de cada objeto:  
   $$\frac{v_1}{w_1}, \frac{v_2}{w_2}, ..., \frac{v_n}{w_n}$$

2. **Ordenar los objetos en orden descendente** según este ratio.

3. **Tomar los objetos en ese orden**, agregándolos completamente hasta que no quepan más.

4. **Si un objeto excede el espacio restante, tomar solo una fracción de él**.

## Justificación Matemática

Para asegurar que esta estrategia garantiza una solución óptima, es necesario demostrar que el problema cumple con:

1. **Subestructura Óptima**  
2. **Propiedad Greedy Choice**

### 1. Subestructura Óptima

Una solución presenta **subestructura óptima** si una solución óptima global se puede construir a partir de soluciones óptimas de subproblemas.

#### Demostración

- Sean $c_1, c_2, ..., c_n$ las **cantidades (o fracciones)** de cada objeto $w_1, w_2, ..., w_n$ que se han seleccionado para optimizar la capacidad total $W$.

- Ahora supongamos que quitamos la última fracción seleccionada, es decir, el elemento $c_n$. Esto nos deja con un peso anterior:
  
$$W_{previo} = W - c_n$$

- La **ganancia obtenida** hasta este punto es:
  
  - $G_{previo}$: ganancia obtenida con la combinación $c_1, c_2, ..., c_{n-1}$.  
  - $G_0$: la ganancia de la **mejor solución óptima posible** para el mismo peso $W_{previo}$, usando otra combinación $d_1, d_2, ..., d_{n-1}$. Por definición, $G_0 \geq G_{previo}$.

- Supongamos, por reducción al absurdo, que la combinación $c_1, c_2, ..., c_{n-1}$ **no** es óptima, es decir, que:
  
$$G_0 > G_{previo}$$

- Al agregar la última fracción $c_n$ a ambas combinaciones:

  - Ganancia de la solución actual:
    $$G_{previo} + g[c_n]$$

  - Ganancia de la supuesta mejor solución:
    $$G_0 + g[c_n]$$

- Esto implicaría que:
  
$$G_0 + g[c_n] > G_{previo} + g[c_n]$$

- Esto contradice la hipótesis de que la solución original con $c_1, c_2, ..., c_n$ era óptima.

Por lo tanto, la suposición inicial es falsa, y la combinación $c_1, c_2, ..., c_{n-1}$ **debe ser óptima**. Esto demuestra que el problema cumple con la **subestructura óptima**, ya que la solución óptima se construye a partir de soluciones óptimas de subproblemas.

### 2. Propiedad Greedy Choice

Un problema cumple con esta propiedad si tomar siempre la **mejor opción local** (en este caso, el objeto con el mayor ratio valor/peso) lleva a una **solución óptima global**.

#### Demostración

1. Sea $i$ el objeto con el **mayor ratio** $v_i/w_i$.

2. Supongamos que tomar este objeto (de forma total o fraccionada) **no** lleva a una solución óptima global, lo que genera una solución $S_{greedy}$.

3. Supongamos que existe otra solución óptima $S^*$ con un valor mayor, es decir:

$$V(S^*) > V(S_{greedy})$$

Donde:

- $V(S)$ representa la **ganancia total** de la solución $S$.
- $x_i$ es la cantidad del objeto $i$ en la solución $S_{greedy}$.  
- $y_i$ es la cantidad del mismo objeto $i$ en la solución $S^*$.

4. Dado que $S_{greedy}$ toma la máxima cantidad posible, debe cumplirse que:

$$x_i > y_i$$

5. Definimos la diferencia de cantidad tomada como:

$$z_i = x_i - y_i > 0$$

6. Ahora, consideremos un objeto $j$ en $S^*$ con menor ratio $v_j/w_j < v_i/w_i$ y que se ha tomado en cantidad $c_j$.

7. Si **reducimos** la cantidad $c_j$ en $z_i$ y **aumentamos** la cantidad $y_i$ en la misma proporción, el cambio en la ganancia total sería:

$$z_i\left(\frac{v_i}{w_i} - \frac{v_j}{w_j}\right) > 0$$

8. Esto indica que la nueva solución tendría una **ganancia mayor** que $S^*$, lo que contradice que $S^*$ era óptima.

Por lo tanto, la hipótesis inicial es falsa y la estrategia de tomar siempre el objeto con el mayor ratio $v_i/w_i$ es correcta. Esto demuestra que el problema cumple con la **propiedad Greedy Choice**.

## Conclusión

Dado que el problema de la mochila fraccionada cumple con ambas propiedades:

1. **Subestructura Óptima**  
2. **Propiedad Greedy Choice**

Se concluye que la estrategia Greedy **garantiza una solución óptima** para este problema.

> **Nota**: En la versión de la mochila **0/1** (donde los objetos no pueden fraccionarse), la estrategia Greedy **no siempre** encuentra la solución óptima.
