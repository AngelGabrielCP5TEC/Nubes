#Ana Paula Navarro Hernández - A01644875
#Angel Gabriel Camacho Pérez - A01743075

import cv2
import numpy as np
import matplotlib.pyplot as plt

imagen = cv2.imread('/img/nube1.jpg')

imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# Crear la máscara para eliminar el azul del cielo
mascara_azul = cv2.inRange(imagen_hsv, np.array([100, 50, 50]), 
                           np.array([130, 255, 255]))
# Invertir la máscara para quedarnos con las zonas sin 
# azul (posibles nubes)
mascara_no_azul = cv2.bitwise_not(mascara_azul)

# Filtrar la imagen para eliminar el azul (el cielo)
imagen_nubes = cv2.bitwise_and(imagen, imagen, 
                               mask=mascara_no_azul)

# Convierte la imagen de las nubes a escala de grises 
# para facilitar su detección
imagen_gris = cv2.cvtColor(imagen_nubes, cv2.COLOR_BGR2GRAY)

# Calcular el área de nubes detectadas y su porcentaje
#  en la imagen
area_total = imagen.shape[0] * imagen.shape[1]
area_nubes = cv2.countNonZero(mascara_no_azul)
area_nubes_porcentaje = (area_nubes / area_total) * 100

# Calcula la intencidad del color de las nubes 
# (entre mas alto mas blanco es el color)
tono_promedio_nubes = np.mean(imagen_gris[mascara_no_azul == 255]) 

# Clasificar el clima según el tono promedio de las nubes
if area_nubes_porcentaje <= 5:
    clima = "Despejado"
elif area_nubes_porcentaje <= 20:
    clima = "Despejado con nubes"
elif area_nubes_porcentaje <= 60:
    clima = "Parcialmente nublado"
else:
    clima = "Nublado"
    if(tono_promedio_nubes < 150):
        clima = "Tormentoso o Lluvioso"

print(f"Area de nubes: {area_nubes_porcentaje}")
print(f"Tono de nubes: {tono_promedio_nubes}")
print(f"Clima estimado: {clima}")

plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
plt.title('Imagen Original')

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(imagen_nubes, cv2.COLOR_BGR2RGB))
plt.title('Mostrando solo nubes')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(imagen_gris, cv2.COLOR_BGR2RGB))
plt.title('Imagen gris')

plt.show()