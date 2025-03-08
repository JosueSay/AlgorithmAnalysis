

**3.** Tenemos dos **strings** $X$ e $Y$ cuyos tamaños son $m$ y $n$ respectivamente. Para transformar $X$ en $Y$ le aplicamos una secuencia de operaciones cuyos resultados se van almacenando en un **string** $Z$. La transformación se lleva con índices $i$ y $j$ sobre $X$ y $Z$ respectivamente, iniciando con $i = j = 1$. Cuando la transformación concluye se debe tener que $i = m + 1$, $j = n$ y $Z = Y$. Las operaciones permitidas para la transformación son las siguientes:

- **Copy:** copia un carácter de $X$ a $Z$ haciendo $Z[j] = X[i]$, y luego incrementa tanto $i$ como $j$.
- **Replace:** reemplaza un carácter de $X$ con algún otro carácter $c$ dado, haciendo $Z[j] = c$; y luego incrementa tanto $i$ como $j$.
- **Delete:** ignora un carácter de $X$ al incrementar $i$ sin incrementar $j$.
- **Insert:** inserta en $Z$ un carácter $c$ dado, haciendo $Z[j] = c$, y luego incrementa $j$ sin incrementar $i$.
- **Twiddle:** intercambia los siguientes dos caracteres de $X$ copiándolos en orden inverso. Para lograrlo hace $Z[j] = X[i + 1]$ y $Z[j + 1] = X[i]$, y luego incrementa tanto $i$ como $j$ dos unidades (i.e., $i = i + 2$, $j = j + 2$).
- **Kill:** ignora el resto de $X$ haciendo $i = m + 1$. Esta operación, si se usa, debe ser la última.

Cada operación tiene un costo constante propio, pero los costos de **Copy** y **Replace** son, cada uno, menores al costo de hacer **Delete** seguido de un **Insert**. Considere el siguiente ejemplo ilustrativo que convierte la palabra "algorithm" en "altruistic":


![alt text](image.png)



Para este ejercicio deberá desarrollar un algoritmo apoyado en el acercamiento *bottom-up* de programación dinámica que permita encontrar la secuencia de operaciones que convierte un *string* en otro incurriendo en el menor costo posible (este costo mínimo es llamado la *edit distance*). Para realizar el ejercicio siga los siguientes pasos:  

a. Identifique la subestructura óptima siguiendo el procedimiento enseñado en clase. *Hint:* para identificar los subproblemas, considere una secuencia de operaciones $(o_1, ..., o_k)\) dada como óptima. Habiéndose aplicado alguna de las operaciones, ¿qué podemos decir que tiene que haber sucedido antes de aplicarse dicha operación? ¿Cuál de los pasos del ejemplo hace la conversión más sencilla (caso base)?  

b. Esboce una tabla $T$ con $m$ filas y $n$ columnas. Esta tabla debe llenarse durante la ejecución de su solución *bottom-up*. ¿Cuál es el significado del contenido de la celda $T[i, j]$?  

c. Apoyándose en el inciso anterior, escriba la ecuación recurrente que computa el valor de la celda $T[i, j]$ tomando en cuenta las condiciones que restringen el uso de cada operación. Puede describir el costo de una operación como $\text{costo}(\text{nombre de operación})$.  

