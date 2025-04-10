import numpy as np

# 1. Crear un arreglo 3D de 10x10x10 lleno de ceros
cubo = np.zeros((10, 10, 10))

# 2. Definir una función para verificar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 3. Recorrer cada celda del cubo 3D usando tres bucles anidados
for i in range(10):      # Índice para la primera dimensión (filas)
    for j in range(10):  # Índice para la segunda dimensión (columnas)
        for k in range(10):  # Índice para la tercera dimensión (profundidad)
            # 4. Verificar las condiciones: i es impar, j es par y k es primo
            if i % 2 != 0 and j % 2 == 0 and es_primo(k):
                # 5. Si las condiciones se cumplen, establecer el valor de la celda a 1
                cubo[i, j, k] = 1

print("Cubo 3D con las condiciones aplicadas:")
print(cubo)

# (Opcional) Podemos contar cuántos elementos son 1 para verificar
cantidad_unos = np.sum(cubo)
print("\nCantidad de elementos con valor 1:", cantidad_unos)