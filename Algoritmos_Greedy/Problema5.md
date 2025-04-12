# Comparación de algoritmos para caminos más cortos: Dijkstra vs Bellman-Ford
## Demostración de la Complejidad del Algoritmo de Dijkstra

## Descripción del Algoritmo

El algoritmo de Dijkstra resuelve el problema del camino más corto entre dos vértices sobre un grafo ponderado positivamente y dirigido. Utiliza un enfoque codicioso (greedy) para seleccionar en cada paso el vértice no visitado con la menor distancia tentativa.

## Pseudocódigo

```
función Dijkstra(Grafo, nodoInicial):
    // Inicialización
    para cada vértice v en Grafo:
        distancia[v] = infinito
        visitado[v] = falso
    distancia[nodoInicial] = 0
    
    // Proceso principal
    mientras existan nodos no visitados:
        u = vértice no visitado con menor distancia
        visitado[u] = verdadero
        
        para cada vecino v de u:
            distanciaTentativa = distancia[u] + peso(u, v)
            si distanciaTentativa < distancia[v]:
                distancia[v] = distanciaTentativa
    
    retornar distancia[]
```

## Análisis de Complejidad

### Implementación con Array Simple

#### Operaciones Críticas:
1. **Inicialización**: O(V) - Asignamos valores iniciales a cada vértice
2. **Bucle principal**: Se ejecuta V veces (una por cada vértice)
   - **Encontrar el vértice con distancia mínima**: O(V) - Recorrido lineal
   - **Actualizar distancias de vecinos**: En el peor caso O(V)

#### Demostración Formal:

Sea G = (V, E) un grafo con |V| vértices y |E| aristas:

- El algoritmo realiza exactamente |V| extracciones del mínimo.
*Prueba*: Cada vértice se marca como visitado exactamente una vez, y para cada marcado se realiza una extracción.

- Cada arista se examina a lo sumo una vez.
*Prueba*: Una arista (u,v) se examina solo cuando u se extrae de la cola, lo que ocurre exactamente una vez.

**Teorema**: Con un array simple, la complejidad de Dijkstra es O(V²).
*Prueba*:
- Extracciones del mínimo: |V| × O(V) = O(V²)
- Examen de aristas: O(E), pero acotado por O(V²) ya que E ≤ V²
- Por tanto, la complejidad total es O(V²)

### Implementación con Cola de Prioridad (Min-Heap)

#### Operaciones Críticas:
1. **Extracción del mínimo**: O(log V)
2. **Actualización de distancia (decrease-key)**: O(log V)
3. **Número de operaciones**:
   - **Extracciones**: V en total
   - **Actualizaciones potenciales**: Una por cada arista, O(E) en total

#### Demostración Formal:

**Teorema**: Con una cola de prioridad binaria, la complejidad de Dijkstra es O((V+E)·log V).
*Prueba*:
- Extracciones del mínimo: |V| × O(log V) = O(V·log V)
- Operaciones decrease-key: O(E) × O(log V) = O(E·log V)
- Por tanto, la complejidad total es O((V+E)·log V)

Cuando E > V, podemos simplificar a O(E·log V).

### Implementación con Cola de Fibonacci

La implementación con cola de Fibonacci mejora la complejidad teórica:
- Extraer mínimo: O(log V) amortizado
- Operación decrease-key: O(1) amortizado
- Complejidad total: O(V·log V + E)


## Comparación con Bellman-Ford

- **Dijkstra**: O(V²) con array simple, O(E·log V) con heap binario
- **Bellman-Ford**: O(n log n)


## Conclusión

La complejidad del algoritmo de Dijkstra con enfoque greedy varía según la implementación:
- O(V²) con implementación básica
- O(E·log V) con cola de prioridad binaria
- O(V·log V + E) con cola de Fibonacci

Esta demostración confirma que la implementación con estructuras de datos adecuadas hace que Dijkstra tenga un rendimiento similar al algoritmo Bellman-Ford, ambos son igual de útiles en la misma instancia del problema ya que tienen una complejiad similar, en otra instancia del problema también tienen un rendimiento similar 
