# cv -> identificar objetos -> detectar bordas = identificar os formatos dos objetos na imagem

""" Sobel é direcional,temos que juntar o filtro horizontal e o vertical para ter uma transformação completa

import cv2
import numpy as np

img = cv2.imread("../sdk.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobel = cv2.bitwise_or(sobelX,sobelY)

resultado = np.hstack([
    np.vstack([img, sobelX]),
    np.vstack([sobel, sobelY]),
])
cv2.imshow("Sobel", resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""



""" Laplacian não precisa juntar filtro x e y, basta apenas um passo para gerar o resultado

import cv2
import numpy as np

img = cv2.imread("../cat.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

lap = cv2.Laplacian(img, cv2.CV_64F)
lap = np.uint8(np.absolute(lap)) 

resultado = np.hstack([img, lap])
cv2.imshow("Lapacian", resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""


""" Canny
canny(sourceimage, limiar1, limiar2)
qualquer gradiente > limiar2 = borda
qualquer gradiente < limiar1 = não borda
"""
import cv2
import numpy as np

img = cv2.imread('../lut.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
suavizacaoGaussiana = cv2.GaussianBlur(img, (9,9), 0)

canny = cv2.Canny(suavizacaoGaussiana, 20, 120) #limiares mais baixos
canny2 = cv2.Canny(suavizacaoGaussiana, 70, 200) #limiiares mais altos

resultado = np.vstack([
    np.hstack([img, suavizacaoGaussiana]),
    np.hstack([canny, canny2]),
    
])
cv2.imshow("Canny", resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()




