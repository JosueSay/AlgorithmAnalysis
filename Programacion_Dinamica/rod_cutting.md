## 1. Identificación de Decisiones y Subproblemas

### **Decisión:**  
En cada paso del proceso, se debe decidir cómo cortar la barra para obtener 
las piezas deseadas. Para una barra de longitud $n$, se 
puede elegir cortarla en una posición $k$ donde $1 \leq k < n$, 
obteniendo dos piezas, una de longitud  $k$ y otra de longitud $n - k$.  
Luego, cada pieza debe ser considerada como un subproblema en sí mismo.

### **Subproblemas:**  
Los subproblemas consisten en encontrar la mejor manera de cortar una barra 
de longitud $j$, donde $j < n$, para obtener las piezas necesarias 
con el costo mínimo. Cada subproblema es independiente y puede resolverse de 
manera óptima.

## 2. Demostración de Subestructura Óptima

Para demostrar que el problema de *rod-cutting* exhibe subestructura óptima, se deben de considerar los siguientes aspectos:

### **Base de la Inducción:**  
Si $n = 0$, es decir que la barra está vacía, el costo es 0. Si $n = 1$, el costo es el 
costo de la barra unitaria.

### **Hipótesis de Inducción:**  
Sí suponemos que para todas las longitudes menores que $n$, ya se conoce 
cómo particionarlas óptimamente.

### **Paso de la Inducción:**  
Si se considera una barra de longitud $n$. Y luego la decidimos cortarla en dos partes: 
una de longitud $i$ y otra de longitud $n - i$, donde $1 \leq i < n$.  
El costo total será el costo de la barra de longitud $i$ más el costo 
de la barra de longitud $n - i$.

Matemáticamente, podemos expresar esto como:

$$
\text{Costo}(n) = \min_{1 \leq i < n} \left( \text{Costo}(i) + \text{Costo}(n - i) \right)
$$

La optimalidad de esta elección se basa en que, al elegir el punto de corte 
$i$ que minimiza el costo total, aseguramos que cada parte restante también sea optimizada.
Esto es posible debido a que cada subproblema ${Costo}(i)$ y ${Costo}(n - i)$ está resuelto con optimalidad por la hipótesis inductiva.

### **Conclusión:**  
Por lo tanto, la elección de cortar en un punto $i$ que minimice 
el costo total asegura que cada subproblema también esté resuelto 
con optimalidad. Esto demuestra que el problema de *rod-cutting* exhibe 
subestructura óptima.

