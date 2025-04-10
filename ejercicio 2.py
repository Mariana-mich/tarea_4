import numpy as np

# Arreglo con los puntajes de los estudiantes
puntajes = np.array([75, 55, 90, 45, 65, 30, 80, 50, 70, 20])
print("Puntajes originales:")
print(puntajes)

# 1. Encontrar los índices de los puntajes menores a 60
#    Usamos una condición dentro de los corchetes para filtrar el arreglo.
indices_reprobados = np.where(puntajes < 60)[0]
print("\nÍndices de los estudiantes con puntaje menor a 60:")
print(indices_reprobados)

# 2. Tomar los tres primeros índices de los reprobados (en el orden que entregaron)
#    Los índices ya están en el orden del arreglo original (orden de entrega).
#    Usamos "slicing" para tomar los primeros tres elementos.
indices_a_cero = indices_reprobados[:3]
print("\nÍndices de los estudiantes que recibirán cero:")
print(indices_a_cero)

# 3. Reemplazar los puntajes de esos estudiantes con cero
#    Usamos los índices que encontramos para modificar el arreglo original.
puntajes[indices_a_cero] = 0
print("\nPuntajes después de la venganza del profesor:")
print(puntajes)