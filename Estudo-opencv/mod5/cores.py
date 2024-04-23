""""" #APLICAÇÕES DE MATRIZ DE CORES GRAY, LAB E HSV
import cv2
img = cv2.imread('../entrada.jpg')

cv2.imshow("Original", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("L*a*b*", lab)

cv2.waitKey(0)
"""""

""""" # separa os canais de cores bgr e exibe em tons cinza
import cv2
img = cv2.imread('../images.jpg')
(canalAzul, canalVerde, canalVermelho) = cv2.split(img)

cv2.imshow("Original", img)

cv2.imshow("Vermelho", canalVermelho)
cv2.imshow("Verde", canalVerde)
cv2.imshow("Azul", canalAzul)

resultado = cv2.merge([canalAzul, canalVerde, canalVermelho])
cv2.imshow("Resultado", resultado)
cv2.waitKey(0)
"""""

# separa os canais de cores e aplica os tons separados na imagem(cv2.merge), não exibe os tons cinza
import numpy as np
import cv2
img = cv2.imread('../entrada.jpg')
(canalAzul, canalVerde, canalVermelho) = cv2.split(img)
zeros = np.zeros(img.shape[:2], dtype = "uint8")
# print(zeros)
cv2.imshow("Vermelho", cv2.merge([zeros, zeros, canalVermelho]))
cv2.imshow("Verde", cv2.merge([zeros, canalVerde, zeros]))
cv2.imshow("Azul", cv2.merge([canalAzul, zeros, zeros]))
cv2.imshow("Original", img)

cv2.waitKey(0)
cv2.destroyAllWindows()










"""""
"""""