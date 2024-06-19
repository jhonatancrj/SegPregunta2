import numpy as np
from scipy.sparse import csr_matrix

# Representación del Gráfico 1 como matriz de adyacencia
# Nodos: 1, 2, 3, 4
adj_matrix1 = np.array([
    [0, 1, 0, 1],  # Nodo 1
    [1, 0, 1, 0],  # Nodo 2
    [0, 1, 0, 1],  # Nodo 3
    [1, 0, 1, 0]   # Nodo 4
])

# Representación del Gráfico 2 como matriz de adyacencia
# Nodos: A, B, C, D
adj_matrix2 = np.array([
    [0, 1, 1, 0],  # Nodo A
    [1, 0, 1, 1],  # Nodo B
    [1, 1, 0, 1],  # Nodo C
    [0, 1, 1, 0]   # Nodo D
])

print("Matriz de adyacencia del Gráfico 1:")
print(adj_matrix1)

print("\nMatriz de adyacencia del Gráfico 2:")
print(adj_matrix2)

# Convertir las matrices de adyacencia a matrices dispersas (CSR)
sparse_matrix1 = csr_matrix(adj_matrix1)
sparse_matrix2 = csr_matrix(adj_matrix2)

print("\nMatriz dispersa del Gráfico 1 (CSR):")
print(sparse_matrix1)

print("\nMatriz dispersa del Gráfico 2 (CSR):")
print(sparse_matrix2)