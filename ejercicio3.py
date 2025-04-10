import numpy as np

locs = np.array([
    [0, 0, 0],
    [1, 1, 2],
    [0, 0, 0],
    [2, 1, 3],
    [5, 5, 4],
    [5, 0, 0],
    [5, 0, 0],
    [0, 0, 0],
    [2, 1, 3],
    [1, 3, 1]
])
generator = np.random.default_rng(1010)
weights = generator.normal(size=10)
print("Ubicaciones iniciales de los peces:")
print(locs)
print("\nPesos de los peces:")
print(weights)

# 1. Crear un acuario 3D vacío (lleno de ceros)
acuario = np.zeros((5, 5, 5))

# 2. Simular el movimiento de los peces y registrar sus nuevas posiciones
nuevas_ubicaciones = np.copy(locs) # Asumimos que las nuevas ubicaciones ya están dadas en 'locs'

# 3. Contar cuántos peces llegan a cada nueva ubicación
conteo_ubicaciones = {}
for i in range(len(nuevas_ubicaciones)):
    ubicacion = tuple(nuevas_ubicaciones[i]) # Convertimos la lista a una tupla para usarla como clave
    if ubicacion in conteo_ubicaciones:
        conteo_ubicaciones[ubicacion].append(i) # Guardamos el índice del pez
    else:
        conteo_ubicaciones[ubicacion] = [i]

print("\nConteo de peces en cada nueva ubicación:")
print(conteo_ubicaciones)

# 4. Determinar qué peces sobreviven en cada ubicación
peces_sobrevivientes = np.ones(len(weights), dtype=bool) # Inicialmente todos sobreviven

for ubicacion, indices_peces in conteo_ubicaciones.items():
    if len(indices_peces) > 1:
        # Si hay más de un pez en la misma ubicación, encontramos el más grande
        pesos_en_ubicacion = weights[indices_peces]
        indice_pez_mas_grande = indices_peces[np.argmax(pesos_en_ubicacion)]

        # Los demás peces en esa ubicación no sobreviven
        for indice_pez in indices_peces:
            if indice_pez != indice_pez_mas_grande:
                peces_sobrevivientes[indice_pez] = False

print("\nSobreviven (True) o no sobreviven (False):")
print(peces_sobrevivientes)

# 5. Mostrar los pesos de los peces que sobrevivieron
pesos_sobrevivientes = weights[peces_sobrevivientes]
print("\nPesos de los peces sobrevivientes:")
print(pesos_sobrevivientes)