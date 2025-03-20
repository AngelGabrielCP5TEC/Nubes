# Ana Paula Navarro Hernández - A01644875
# Angel Gabriel Camacho Pérez - A01743075

# Librerías
import cv2 # Procesamiento de imágenes
import numpy as np # Manejar arreglos y matrices multidimensionales
import matplotlib.pyplot as plt # Visualización de datos y gráficos

# Se carga la imágen
imagen = cv2.imread('/img/nube1.jpg')

# Pasa la imágen de BGR a HSV
imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# Crea una máscara para eliminar el azul del cielo 
mascara_azul = cv2.inRange(imagen_hsv, np.array([100, 50, 50]), 
                           np.array([130, 255, 255]))

# Invierte la máscara para quedarnos con las zonas sin 
# azul (posibles nubes)
mascara_no_azul = cv2.bitwise_not(mascara_azul)

# Filtra la imagen para eliminar el azul (el cielo), 
# y dejar solo las nubes
imagen_nubes = cv2.bitwise_and(imagen, imagen, mask=mascara_no_azul)

# Convierte la imagen de las nubes a escala de grises 
# para facilitar su detección
imagen_gris = cv2.cvtColor(imagen_nubes, cv2.COLOR_BGR2GRAY)

# Calcula el área de nubes detectadas y su porcentaje 
# en la imagen
area_total = imagen.shape[0] * imagen.shape[1] 
area_nubes = cv2.countNonZero(mascara_no_azul) 
area_nubes_porcentaje = (area_nubes / area_total) * 100 

# Calcula la intencidad del color de las nubes 
# (entre mas alto mas blanco es el color)
tono_promedio_nubes = np.mean(imagen_gris[mascara_no_azul == 255]) 

# Clasifica el clima según el tono promedio de las nubes 
# en diferentes categorías
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

# Se imprimen los resultados 
print(f"Area de nubes: {area_nubes_porcentaje}")
print(f"Tono de nubes: {tono_promedio_nubes}")
print(f"Clima estimado: {clima}")

# Se muestran los resultados 
plt.figure(figsize=(12, 6))

# Imágen original (en RGB)
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
plt.title('Imagen Original')

# Imágen que solo muestra nubes
plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(imagen_nubes, cv2.COLOR_BGR2RGB))
plt.title('Mostrando solo nubes')

# Imágen en escala de grises 
plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(imagen_gris, cv2.COLOR_BGR2RGB))
plt.title('Imagen gris')

# Se muestran todas las figuras 
plt.show()