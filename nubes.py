#Ana Paula Navarro Hernández - A01644875
#Angel Gabriel Camacho Pérez - A01743075

import cv2
import numpy as np
import matplotlib.pyplot as plt

imagen = cv2.imread('/img/nube1.jpg')

imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)


# Mascara para identificar el cielo mediante el color azul
mascara_azul = cv2.inRange(imagen_rgb, np.array([100, 50, 50]), np.array([130, 255, 255]))
# Mascara para identificar lo que no forme parte del cielo azul
mascara_no_azul = cv2.bitwise_not(mascara_azul)

# Filtrar la imagen para eliminar el cielo azil
imagen_nubes = cv2.bitwise_and(imagen, imagen, mask=mascara_no_azul)


# Calcular el área de nubes detectadas y su porcentaje en la imagen
area_total = imagen.shape[0] * imagen.shape[1]
area_nubes = cv2.countNonZero(mascara_no_azul)
area_nubes_porcentaje = (area_nubes / area_total) * 100


print(f"Area de nubes: {area_nubes_porcentaje}")

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
plt.title('Imagen Original')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(imagen_nubes, cv2.COLOR_BGR2RGB))
plt.title('Mostrando solo nubes')

plt.show()
