import numpy as np

# 1. Generar los puntajes de amor para 10 personas de forma aleatoria entre 0 y 100
#    np.random.rand() genera números aleatorios entre 0 y 1.
#    Los multiplicamos por 100 para tener valores entre 0 y 100.
puntajes_amor = np.random.rand(10) * 100
print("Puntajes de amor de las 10 personas:")
print(puntajes_amor)

# 2. Crear una matriz 2-D para guardar las diferencias absolutas
#    Queremos una matriz de 10x10 (10 personas vs. 10 personas).
diferencias = np.zeros((10, 10))

# 3. Calcular la diferencia absoluta entre cada par de puntajes
#    Vamos a usar dos bucles (uno dentro de otro) para comparar cada persona con todas las demás.
for i in range(10):  # Recorremos cada persona (fila de la matriz)
    for j in range(10):  # Recorremos cada persona (columna de la matriz)
        # np.abs() calcula el valor absoluto (la diferencia sin importar el signo).
        diferencia = np.abs(puntajes_amor[i] - puntajes_amor[j])
        # Guardamos la diferencia en la posición (i, j) de nuestra matriz.
        diferencias[i, j] = diferencia

print("\nMatriz de diferencias de puntajes de amor:")
print(diferencias)