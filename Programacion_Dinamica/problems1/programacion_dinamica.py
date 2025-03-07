def knapsack_01(weights, values, W):
  """
  weights: lista con los pesos de los objetos
  values:  lista con los valores de los objetos
  W:       capacidad máxima de la mochila
  Retorna: valor máximo que se puede obtener sin exceder W
  """
  n = len(weights)
  # Creamos una tabla (n+1) x (W+1) para almacenar los resultados
  dp = [[0] * (W + 1) for _ in range(n + 1)]
  
  for i in range(1, n + 1):
      for j in range(1, W + 1):
          # Caso 1: no tomar el objeto i-ésimo
          dp[i][j] = dp[i-1][j]
          
          # Caso 2: tomar el objeto i-ésimo (si cabe en la mochila)
          if weights[i-1] <= j:
              dp[i][j] = max(dp[i][j], dp[i-1][j - weights[i-1]] + values[i-1])
  
  # La respuesta está en dp[n][W]
  return dp[n][W]

# Ejemplo de uso
if __name__ == "__main__":
  pesos = [2, 3, 4, 5]
  valores = [3, 4, 5, 6]
  capacidad = 5
  print("Valor máximo:", knapsack_01(pesos, valores, capacidad))