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

# Programación Dinámica

## 1. Modificación del Rod-Cutting Problem (1)

### Descrpción

Suponga que al *rod-cutting problem* agregamos un límite piezas que se pueden vender o cortar para cada posible tamaño. Es decir que, para 0 < i ≤ n, lᵢ ∈ N es el número máximo de piezas de tamaño i que podemos usar en la solución. Demuestre que con esta nueva restricción el problema ya no exhibe una subestructura óptima. *Hint:* ¿qué característica de los subproblemas se evaluó para determinar la ausencia de subestructura óptima en el *unweighted longest simple path problem*?

### Solución

En un problema *normal* de *Rod Cutting* definimos $C(n)$ como el costo mínimo para cortar una barra de longitud $n$:

$$
C(n) = \min_{1 \leq i \leq n} \left( C(i) + C(n - i) \right)
$$

Pero con la nueva restricción en la cantidad de piezas, debemos verificar que la elección de una pieza de tamaño $i$ respete la restricción de cantidad de piezas $l_i$.

Ahora debemos buscar un contraejemplo donde la solución óptima de un subproblema **no se pueda reutilizar** para construir la solución óptima del problema general.

### Base de la Inducción

Si $n = 0$, el costo es $0$. Si $n = 1$, el costo es simplemente el costo de la pieza de tamaño $1$ (si está disponible bajo la restricción $l_1$).

Si suponemos que para cualquier longitud menor que $n$, la restricción en la cantidad de piezas no afecta la subestructura óptima y se puede resolver óptimamente cada subproblema.

$$
C(n) = \min_{1 \leq i < n} \left( C(i) + C(n - i) \right)
$$

Pero ahora, la restricción en la cantidad de piezas **rompe la independencia de los subproblemas**. Porque si en una solución óptima para una barra de longitud menor se usó el máximo permitido de piezas de un tamaño particular, esa misma solución **no puede ser utilizada nuevamente** cuando se resuelve el problema para una longitud mayor.

### Ejemplo

Si que quiere cortar una barra de tamaño $n = 5$ y que podemos usar un máximo de:

- $l_2 = 2$ (como máximo 2 piezas de tamaño 2)
- $l_3 = 1$ (como máximo 1 pieza de tamaño 3)

Se puede construir a partir de:

$$
\text{Usar 2 piezas de tamaño 2 y 1 pieza de tamaño 1}
$$

Pero si ahora se aplica el mismo enfoque con una barra con mayor tamaño, por ejemplo $n = 8$, la solución óptima **podría haber reutilizado las piezas de tamaño 2**, pero como ya hemos alcanzado el límite en una instancia previa, esta solución deja de ser válida.

Como en el caso del problema *unweighted longest simple path*, donde la mejor solución a un subproblema puede volverse inválida al expandirse a un problema mayor, aquí sucede lo mismo con la restricción en la cantidad de piezas permitidas.

## 2. Modificación del Rod-Cutting Problem (2)

### Descripción

Volvamos al *rod-cutting problem* original. Resulta que no tenemos ni las herramientas ni las habilidades necesarias para cortar tubos, por lo que subcontratamos este servicio. Cada corte que queramos realizar costará una cantidad fija *c*. ¿Qué modificación se le tiene que hacer al algoritmo ya provisto para adaptarse a esta nueva condición?

### Solución

En el problema rod-cutting, buscamos maximizar el beneficio al vender piezas de una barra de longitud $n$. La ecuación de recurrencia estándar es:

$$
r(n) = \max_{1 \leq i \leq n} \{ p_i + r(n - i) \}
$$

donde $p_i$ representa el precio de una pieza de longitud $i$.

#### Modificación por Costo de Corte

Si cada corte tiene un costo fijo $c$, debemos considerar este gasto adicional. Cada vez que realizamos un corte, pagamos $c$, lo que modifica la ecuación de recurrencia:

$$
r(n) = \max_{1 \leq i \leq n} \{ p_i + r(n - i) - c \}
$$

donde:

- El término $-c$ se aplica únicamente si efectivamente realizamos un corte, es decir, cuando $i < n$.
- Si no se hacen cortes (es decir, si se vende la barra completa), no se paga el costo $c$.

## 3. Cálculo de la Distancia de Edición mediante Programación Dinámica

### Descripción

Tenemos dos strings $X$ e $Y$ cuyos tamaños son $m$ y $n$ respectivamente. Para transformar $X$ en $Y$ le aplicamos una secuencia de operaciones cuyos resultados se van almacenando en un string $Z$. La transformación se lleva con índices $i$ y $j$ sobre $X$ y $Z$ respectivamente, iniciando con $i = j = 1$. Cuando la transformación concluye se debe tener que $i = m + 1, j = n$ y $Z = Y$. Las operaciones permitidas para la transformación son las siguientes:

- **Copy**: copia un carácter de $X$ a $Z$ haciendo $Z[j] = X[i]$, y luego incrementa tanto $i$ como $j$.
- **Replace**: reemplaza un carácter de $X$ con algún otro carácter $c$ dado, haciendo $Z[j] = c$; y luego incrementa tanto $i$ como $j$.
- **Delete**: ignora un carácter de $X$ al incrementar $i$ sin incrementar $j$.
- **Insert**: inserta en $Z$ un carácter $c$ dado, haciendo $Z[j] = c$, y luego incrementa $j$ sin incrementar $i$.
- **Twiddle**: intercambia los siguientes dos caracteres de $X$ copiándolos en orden inverso. Para lograrlo hace $Z[j] = X[i + 1]$ y $Z[j + 1] = X[i]$, y luego incrementa tanto $i$ como $j$ dos unidades (i.e., $i = i + 2, j = j + 2$).
- **Kill**: ignora el resto de $X$ haciendo $i = m + 1$. Esta operación, si se usa, debe ser la última.

Cada operación tiene un costo constante propio, pero los costos de **Copy** y **Replace** son, cada uno, menores al costo de hacer **Delete** seguido de un **Insert**. Considere el siguiente ejemplo ilustrativo que convierte la palabra *algorithm* en *altruistic*:

| Operation  | x          | z           |
|------------|-----------|------------|
| *initial strings* | algorithm  | _          |
| copy      | algorithm  | a_         |
| copy      | algorithm  | al_        |
| replace by t | algorithm  | alt_      |
| delete    | algorithm  | alt_       |
| copy      | algorithm  | altr_      |
| insert u  | algorithm  | altru_     |
| insert i  | algorithm  | altrui_    |
| insert s  | algorithm  | altruís_   |
| twiddle   | algorithm  | altruisti_ |
| insert c  | algorithm  | altruistic_ |
| kill      | algorithm_ | altruistic_ |

Para este ejercicio deberá desarrollar un algoritmo apoyado en el acercamiento **bottom-up** de programación dinámica que permita encontrar la secuencia de operaciones que convierte un *string* en otro incurriendo en el menor costo posible (este costo mínimo es llamado la **edit distance**). Para realizar el ejercicio siga los siguientes pasos:

a. Identifique la subestructura óptima siguiendo el procedimiento enseñado en clase.  
   *Hint*: para identificar los subproblemas, considere una secuencia de operaciones \((o_1, ..., o_k)\) dada como óptima. Habiéndose aplicado alguna de las operaciones, ¿qué podemos decir que tiene que haber sucedido antes de aplicarse dicha operación? ¿Cuál de los pasos del ejemplo hace la conversión más sencilla (caso base)?  

b. Esboce una tabla $T$ con $m$ filas y $n$ columnas. Esta tabla debe llenarse durante la ejecución de su solución *bottom-up*. ¿Cuál es el significado del contenido de la celda $T[i, j]$?  

c. Apoyándose en el inciso anterior, escriba la ecuación recurrente que computa el valor de la celda $T[i, j]$ tomando en cuenta las condiciones que restringen el uso de cada operación. Puede describir el costo de una operación como **costo(nombre de operación)**.  

### Solución
