# Modelación de problemas con matroides ponderadas: Árboles de expansión mínima y hospedaje

Demuestre que el *minimum-spanning-tree problem* y el problema de sitios de hospedaje descritos en clase se pueden modelar como matroides ponderadas (es decir, identifique y describa el conjunto *S*, la función de pesos y la familia de conjuntos independientes). Demuestre que cumplen con las propiedades de herencia e intercambio.

## 1. Minimum-Spanning-Tree Problem (Árbol de expansión mínima)

### Descripción del problema

Dado un grafo no dirigido y conexo $G = (V, E)$ con pesos positivos asignados a cada arista $e \in E$, el objetivo del problema de **minimum spanning tree (MST)** es encontrar un subconjunto de aristas $T \subseteq E$ que:

- Conecte todos los vértices (es decir, forme un árbol de expansión)
- Tenga peso total mínimo:
  $$
  \sum_{e \in T} w(e)
  $$

### Modelación como matroide ponderada

Queremos demostrar que este problema puede modelarse como una **matroide ponderada** $M = (S, I, w)$.

#### 1.1 Conjunto base ($S$)

El conjunto de **aristas del grafo**, es decir:
$$
S := E
$$

#### 1.2 Función de pesos ($w$)

Función que asigna un peso positivo a cada arista:
$$
w: S \to \mathbb{R}^+, \quad w(e) \text{ representa el costo de la arista } e
$$

#### 1.3 Familia de conjuntos independientes ($I$)

La familia $I$ está compuesta por todos los subconjuntos de aristas que **no forman ciclos**, es decir, **subconjuntos acíclicos** o **bosques**:
$$
I := \{ A \subseteq E \;|\; A \text{ no contiene ciclos} \}
$$

### Verificación de las propiedades de matroide

#### 1. **No-vaciedad**

$$
\emptyset \in I \quad \text{(el conjunto vacío no forma ciclos)}
$$

- **Se cumple.**

#### 2. **Herencia**

Si $A \in I$, entonces cualquier subconjunto $B \subseteq A$ también es acíclico, porque eliminar aristas no puede introducir ciclos.

- **Se cumple.**

#### 3. **Intercambio**

Si $A, B \in I$ con $|A| < |B|$, entonces existe una arista $e \in B \setminus A$ tal que $A \cup \{e\} \in I$.

Esto es **cierto para los grafos**: en dos bosques acíclicos con distinta cantidad de aristas, siempre podemos agregar alguna arista del más grande al más pequeño **sin formar un ciclo** (ver notas sobre "propiedad de intercambio").

- **Se cumple.**

## 2. Problema de Hospedaje (Unit Task Scheduling Problem)

### Descripción del problema

Dado un conjunto de tareas $T = \{t_1, t_2, ..., t_n\}$, donde cada tarea $t_i$ tiene:

- Un deadline $d_i \in \mathbb{Z}^+$: tiempo límite para completarla
- Una penalización $w_i \in \mathbb{R}^+$ si no se completa a tiempo

Todas las tareas requieren exactamente **una unidad de tiempo** para completarse y se ejecutan en una **única máquina** que procesa **una tarea a la vez**.

### Objetivo

Encontrar un subconjunto de tareas y un orden de ejecución tal que **minimice la penalización total**, es decir:

$$
\min \sum_{i = 1}^n w_i \cdot I_i
$$

donde la función indicadora $I_i$ es:

$$
I_i =
\begin{cases}
0, & C_i \leq d_i \quad \text{(a tiempo)} \\
1, & C_i > d_i \quad \text{(tarde)}
\end{cases}
$$

### Modelación como matroide ponderada

#### 2.1 Conjunto base ($S$)

Conjunto de tareas:
$$
S := \{t_1, t_2, ..., t_n\}
$$

#### 2.2 Función de pesos ($w'$)

Para aplicar estrategia greedy, transformamos los pesos con:
$$
w'(t_i) = M - w_i \quad \text{donde } M > \sum w_i
$$

De esta forma, **maximizar $w'(A)$ equivale a minimizar $\sum w_i \cdot I_i$**.

#### 2.3 Conjuntos independientes ($I$)

Un subconjunto $A \subseteq S$ es **independiente** si existe un ordenamiento (schedule) de sus tareas que las completa **todas a tiempo**.

Formalmente:
$$
A \in I \iff \exists \; \sigma : A \to \{1, ..., |A|\} \text{ tal que } C_i \leq d_i \quad \forall t_i \in A
$$

### Verificación de propiedades de matroide

#### 1. **No-vaciedad**

El conjunto vacío no tiene tareas → ninguna penalización.

- **Se cumple.**

#### 2. **Herencia**

Si $A$ puede completarse a tiempo, cualquier subconjunto $B \subseteq A$ también.

- **Se cumple.**

#### 3. **Intercambio (Propiedad de aumento)**

Si $A, B \in I$ con $|A| < |B|$, se puede demostrar que **existe una tarea $x \in B \setminus A$** tal que $A \cup \{x\}$ **también se puede completar a tiempo**.

Esto se demostró en clase por contradicción, considerando el ordenamiento de deadlines y argumentando que si **todas las combinaciones fallan**, entonces $B$ tampoco sería agendable a tiempo, lo cual contradice $B \in I$.

- **Se cumple.**
