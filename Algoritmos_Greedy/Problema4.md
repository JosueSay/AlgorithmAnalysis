# Selección óptima de equipo interdisciplinario bajo restricciones de diversidad

## Parte a: Demostración de Matroide y Algoritmo Greedy

### 1. Demostración que el problema es una matroide ponderada

Para modelar este problema como una matroide ponderada, definimos:
- **Conjunto base (E)**: Todos los estudiantes disponibles `E = {estudiante₁, estudiante₂, ..., estudianteₙ}`
- **Familia de conjuntos independientes (I)**: Todos los subconjuntos de E donde no hay dos estudiantes de la misma carrera

**Propiedades que cumplen:**

1. **Hereditaria**:
   - Si B ∈ I y A ⊆ B ⇒ A ∈ I
   - Ejemplo: Si {A, D} es válido (carreras diferentes), entonces {A} también lo es

2. **Propiedad de intercambio**:
   - Si A, B ∈ I y |A| < |B| ⇒ ∃x ∈ B\A tal que A ∪ {x} ∈ I
   - Ejemplo: Si A = {A} y B = {D,E}, podemos agregar D o E a A

### 2. Algoritmo Greedy

```python
def seleccionar_equipo(estudiantes):
    # Paso 1: Ordenar por promedio descendente
    estudiantes_ordenados = sorted(estudiantes, key=lambda x: x['promedio'], reverse=True)
    
    equipo = []
    carreras_seleccionadas = set()
    
    # Paso 2: Selección greedy
    for estudiante in estudiantes_ordenados:
        if estudiante['carrera'] not in carreras_seleccionadas:
            equipo.append(estudiante)
            carreras_seleccionadas.add(estudiante['carrera'])
    
    return equipo
```

**Complejidad temporal**: O(n log n) por el ordenamiento

## Parte b: Instancia del Problema y Aplicación del Algoritmo

### 1. Datos de entrada

```python
estudiantes = [
    {"nombre": "Ana", "carrera": "Ingeniería en Ciencias de la Computación", "promedio": 95},
    {"nombre": "Carlos", "carrera": "Matemática Aplicada", "promedio": 90},
    {"nombre": "Beatriz", "carrera": "Ingeniería en Ciencias de la Computación", "promedio": 85},
    {"nombre": "David", "carrera": "Licenciatura en Química", "promedio": 88},
    {"nombre": "Elena", "carrera": "Data Science", "promedio": 92}
]
```

### 2. Ejecución paso a paso

| Paso | Estudiante | Carrera                              | Promedio | Acción           | Equipo Actual |
|------|------------|--------------------------------------|----------|------------------|---------------|
| 1    | Ana        | Ing. Ciencias Computación            | 95       | Agregar          | [Ana]         |
| 2    | Elena      | Data Science                         | 92       | Agregar          | [Ana, Elena]  |
| 3    | Carlos     | Matemática Aplicada                  | 90       | Agregar          | [Ana, Elena, Carlos] |
| 4    | David      | Licenciatura en Química              | 88       | Agregar          | [Ana, Elena, Carlos, David] |
| 5    | Beatriz    | Ing. Ciencias Computación            | 85       | Rechazar (carrera repetida) | - |

### 3. Resultado final

**Equipo seleccionado:**
1. Ana (Ing. Ciencias Computación) - 95
2. Elena (Data Science) - 92
3. Carlos (Matemática Aplicada) - 90
4. David (Licenciatura en Química) - 88

**Suma total de promedios:** 365

### 4. Análisis de optimalidad

Para demostrar que esta solución es óptima:
- No se puede incluir a Beatriz sin eliminar a Ana (mayor promedio)
- Todos los estudiantes seleccionados tienen los mayores promedios de sus respectivas carreras
- No existe ninguna combinación válida con mayor suma de promedios

## Conclusión

El problema cumple con la estructura de matroide y el algoritmo greedy garantiza encontrar la solución óptima en tiempo O(n log n), seleccionando siempre los estudiantes con mayores promedios de carreras no repetidas.