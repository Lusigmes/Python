import cv2
import numpy as np

# Carregar imagem em tons de cinza
img = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)

# Definir kernel para operações morfológicas
kernel = np.ones((5,5), np.uint8)

# Aplicar erosão
erosion = cv2.erode(img, kernel, iterations=1)

# Aplicar dilatação
dilation = cv2.dilate(img, kernel, iterations=1)

# Aplicar abertura (erosão seguida de dilatação)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# Aplicar fechamento (dilatação seguida de erosão)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Mostrar resultados
cv2.imshow('Original', img)
cv2.imshow('Erosion', erosion)
cv2.imshow('Dilation', dilation)
cv2.imshow('Opening', opening)
cv2.imshow('Closing', closing)
cv2.waitKey(0)
cv2.destroyAllWindows()
