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

Ahora vamos a 


## 2. Tiempo de Ejecucion

## 3. Solucion Optima