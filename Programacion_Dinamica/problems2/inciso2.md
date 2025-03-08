# Modificación del Rod-Cutting Problem

En el problema rod-cutting, buscamos maximizar el beneficio al vender piezas de una barra de longitud $n$. La ecuación de recurrencia estándar es:

$$
r(n) = \max_{1 \leq i \leq n} \{ p_i + r(n - i) \}
$$

donde $p_i$ representa el precio de una pieza de longitud $i$.

## Modificación por Costo de Corte
Si cada corte tiene un costo fijo $c$, debemos considerar este gasto adicional. Cada vez que realizamos un corte, pagamos $c$, lo que modifica la ecuación de recurrencia:

$$
r(n) = \max_{1 \leq i \leq n} \{ p_i + r(n - i) - c \}
$$

donde:
- El término $-c$ se aplica únicamente si efectivamente realizamos un corte, es decir, cuando $i < n$.
- Si no se hacen cortes (es decir, si se vende la barra completa), no se paga el costo $c$.

