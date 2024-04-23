""""" #espelhando no vertical e horizontal
import cv2
img = cv2.imread('../entrada.jpg')
cv2.imshow("Original", img)

flip_horizontal = img[::-1,:] #comando equivalente abaixo
#flip_horizontal = cv2.flip(img, 1)
cv2.imshow("Flip Horizontal", flip_horizontal)

flip_vertical = img[:,::-1] #comando equivalente abaixo
#flip_vertical = cv2.flip(img, 0)
cv2.imshow("Flip Vertical", flip_vertical)

flip_hv = img[::-1,::-1] #comando equivalente abaixo
#flip_hv = cv2.flip(img, -1)
cv2.imshow("Flip Horizontal e Vertical", flip_hv)

cv2.waitKey(0)
"""""

""""" rotacionando imagem
# affine preservam os pontos, grossura de linhas e planos
# linhas paralelas permanecem paralelas após uma transformação affine.
# não necessariamente preserva a distância entre pontos mas ela preserva a proporção das distâncias entre os pontos de uma linha reta

import cv2
img = cv2.imread('../entrada.jpg')

(alt, lar) = img.shape[:2] #captura altura e largura
centro = (lar // 2, alt // 2) #acha o centro
M = cv2.getRotationMatrix2D(centro, 90, 1.0) #30 graus

img_rotacionada = cv2.warpAffine(img, M, (lar, alt))
cv2.imshow("Imagem rotacionada em 45 graus", img_rotacionada)
cv2.waitKey(0)
"""""

# MASCARAS - imagem com pixels on/off, preto e branco
""""" #Mascara circular
import cv2
import numpy as np
# import imutils

img = cv2.imread('../entrada.jpg')
cv2.imshow("Original", img)
mascara = np.zeros(img.shape[:2], dtype = "uint8")

(cX, cY) = (img.shape[1] // 2, img.shape[0] // 2)
cv2.circle(mascara, (cX, cY), 300, 255, -1)

img_com_mascara = cv2.bitwise_and(img, img, mask=mascara)
cv2.imshow("Máscara aplicada à imagem", img_com_mascara)
cv2.waitKey(0)
"""""

import cv2
import numpy as np

img = cv2.imread('../entrada.jpg')
cv2.imshow("Original", img)
mascara = np.zeros(img.shape[:2], dtype = "uint8")
# print(np.zeros(img.shape[:2], dtype = "uint8"))
# X/LARGURA/EIXO X  - Y/ALTURA/EIXO Y
(cX, cY) = (img.shape[1] // 2, img.shape[0] // 2)
cv2.circle(mascara, (cX, cY), 200, 255, 100)
cv2.circle(mascara, (cX, cY), 100, 255, -1)

cv2.imshow("Máscara", mascara)
img_com_mascara = cv2.bitwise_and(img, img, mask = mascara)

cv2.imshow("Máscara aplicada à imagem", img_com_mascara)
cv2.waitKey(0)
cv2.destroyAllWindows()

