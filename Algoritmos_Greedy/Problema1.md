# Minimización del tiempo promedio de terminación en calendarización no-preemptiva

Veamos un nuevo problema de calendarizacion . Tenemos un conjunto de tareas S= {a1, .... an}, donde la letra $a_i$ tarda en realizarse $p_i$ de unidades de tiempo. Dependiendo de como calendaricemos su ejecucion, cada tarea tendra un tiempo de terminacion $c_i$ (que es cuando la tarea se completa). Queremos hacer una calendarizacion non-preemptive (un tarea iniciada no se puede interrumpir) que minimice todos los tiempos de terminacion

a. Proponga un algoritmo greedy que provee esta calendarizacion

b. Determine el tiempo de ejecucion de su algoritmo

c. Demuestre que su algoritmo de la solucion optima (es decir que , demuestre presenta caracteristicas que permiten obtener una solucion optima mediante un algoritmo greedy o modele el problema como una matroide ponderada)

## 1. Proponga un algoritmo

Lo que queremos minimizar es todos los tiempos de terminacion de nuestro stack osea que minicemos el tiempo total de minimizacion entre ellos. En pocas palabras :

$$min(\sum_{i=1}^n c_i)$$

Asi mismo se sabe lo siguiente

- Una vez iniciado un proceso $a_i$ no se puede pausar
- Se ordenan los procesos segun su $p_i$ o tiempo de procesamiento. 
- El tiempo de terminacion $c_i$ de un proceso $a_i$ es igual a $p_i + t$ osea es el procesamiento actual y t que es la sumatoria de todos los anteriores. $t =\sum_{i=1}^i c_i $.

Ahora vamos a proponer el algoritmo, recordemos que estamos lidiando con una heuristica SPF o shortest processing time first debido a que vamos a realizar el procesamiento de los que tienen menos tiempo de procesamiento para minimizar el total de tiempos de terminacion. 

Esto se puede observar si tenemos 2 procesos:

- A tarda 1 seg
- B tarda 10 seg

Si se ejecuta primero el tiempo de c de A sera 1, el c de B sera 1 + 10 osea 11. Y el total de terminacion de todos sera 1 + 11  = 12.

Pero si se ejecuta primero el de mas tiempo el tiempo de procesamiento de B sera 10 pero el de A sera de 11. Y el total sera de 10 + 11 osea 21


El pseudocodigo del algoritmo sera el siguiente

```plaintext
function merge_sort(tareas):
    if longitud(tareas) ≤ 1:
        return tareas

    medio ← longitud(tareas) // 2
    izquierda ← merge_sort(tareas[0:medio])
    derecha ← merge_sort(tareas[medio:])

    return merge(izquierda, derecha)

function merge(izq, der):
    resultado ← []
    mientras izq no vacío y der no vacío:
        si izq[0].p ≤ der[0].p:
            resultado.agregar(izq.eliminar_primero())
        sino:
            resultado.agregar(der.eliminar_primero())
    agregar el resto de izq y der a resultado
    return resultado

function calcular_suma_tiempos(tareas):
    tareas_ordenadas ← merge_sort(tareas)
    t ← 0
    suma_total ← 0

    para cada tarea en tareas_ordenadas:
        t ← t + tarea.p
        suma_total ← suma_total + t

    return suma_total
```

Como se puede ver lo que se hizo fue ordenar obtener la lista de tareas, ordenarlas por $p_i$ de la menor a la mayor, y luego tener una variable t que es la suma de los $c_i$.

## 2. Tiempo de Ejecucion

El tiempo de ejecucion es el siguiente

De todos los tiempos de ejecucion realmente el de sumar es O(1) el de obtener la lista es de O(1) lo unico que afecta el rendimiento es que algoritmo de ordenamiento usemos, en este caso usamos merge sort entonces el analisis seria el siguiente:

Merge Sort

Sea $T(n)$ el tiempo que toma ordenar un arreglo de tamaño n:

Se divide el arreglo en dos partes de tamaño $n/2$.

Se hacen dos llamadas recursivas para ordenar cada mitad → $2T(n/2)$.

Luego se mezclan ambas mitades ordenadas en tiempo $O(n)$.


$$TT(n)=2T(n/2)+O(n)$$

Ahora resolvemos la recurrencia con la ecuacion de recurrencia 

$$T(n)=aT(n/b)+f(n)$$

Una vez identificada la forma de la grafica sabemos que 

- $a=2$
- $b=2$
- $f(n)= O(n)$

Resolviendo nos da $n^{log_ba}= n^{log_22}$  $f(n)=O(n^{lob_ba})$ estamos en el caso 2 por ende

$$T(n)=O(n log n)$$

Por ende la complejidad o tiempo de ejecucion de nuestro algoritmo sera de :

$$O(n log n)$$

## 3. Solucion Optima


### Demostración (Intercambio por pares):

Sabemos que de la secuencia de tareas S, tenemos 2 tareas $a_i$ y $a_{i+1}$ entonces sus $p_i$ seguiran el orden de $p_i > p{i+1}$

Calculamos el impacto

Sea:

- t: el tiempo acumulado hasta antes de $a_i$
- $c_i$ = $t+p_i$
- $c_{i+1}$ = $t+p_i+p_{i+1}$

La suma parcial de tiempos

$$c_i + c_{i+1} = (t+p_i) + (t+p_i+p_{i+1}) = 2t+2p_i+p_{i+1}$$
​
Después de intercambiar osea que primero se hagan los mas largos:

- $c' = t+p_{i+1}$
- $c'_{i+1} = t+p_{i+1}$


La sumatoria sera

$$c'_i + c'_{i+1} = (t+p_{i+1}) + (t+p_{i+1}+p_i) = 2t+2p_{i+1}+p_i$$

Ahora vamos a comparar 

$$(2t+2p_i+p_{i+1})-(2t+2p_{i+1}+p_i)$$

Al operar nos da lo siguiente

$$2t-2t+2p_i-p_i+2p_{i+1}-p_{i+1}$$

Lo que da
$$p_i+p_{i+1}>0$$

Esto quieres decir que la suma antes del intercambio era mayor, por lo tanto el intercambio mejora la suma total de tiempos de finalización.

### Conclusion

Intercambiar una tarea más larga que aparece antes por una más corta que aparece después reduce la suma de tiempos de terminación.

Lo que nos lleva a que debemos de ordenar los $p_i$ de manera creciente.

