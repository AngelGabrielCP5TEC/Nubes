#Ana Paula Navarro Hernández - A01644875
#Angel Gabriel Camacho Pérez - A01743075

import cv2
import numpy as np
import matplotlib.pyplot as plt

imagen = cv2.imread('/content/nuve6.jpg')

hsv_image = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
plt.title('Imagen Original')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(hsv_image, cv2.COLOR_HSV2RGB))
plt.title('con filtro hsv')

plt.show()