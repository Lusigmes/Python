
"""   
thresholding = limiarização
convertemos imagenss em tons de cinza para preto e branco com onde
todos pixels possuem 0 ou 255 como valores de intensidade

"""

""" # suavização da imagem, binarização com threshold de 160 e
    # a inversão da imagem binarizada.
import cv2
import numpy as np

img = cv2.imread('../cat.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
suavizacaoGaussiana = cv2.GaussianBlur(img, (7, 7), 0) # aplica blur
(T, bin) = cv2.threshold(suavizacaoGaussiana, 160, 255, cv2.THRESH_BINARY)

(T, binI) = cv2.threshold(suavizacaoGaussiana, 160, 255,
cv2.THRESH_BINARY_INV)

resultado = np.vstack([
    np.hstack([suavizacaoGaussiana, bin]),

    np.hstack([binI, cv2.bitwise_and(img, img, mask = binI)])
])

cv2.imshow("Binarização da imagem", resultado)
cv2.waitKey(0)
"""



""" # Thresholding adaptativo
import cv2
import numpy as np
# import matplotlib.pyplot as plt
img = cv2.imread("../cat.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
suavizacaoGaussiana = cv2.GaussianBlur(img, (7, 7), 0)

bin1 = cv2.adaptiveThreshold(suavizacaoGaussiana, 255, 
                            cv2.ADAPTIVE_THRESH_MEAN_C,
                            cv2.THRESH_BINARY_INV, 21, 5 )
bin2 = cv2.adaptiveThreshold(suavizacaoGaussiana, 255, 
                            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY_INV, 21, 5 )
resultado = np.hstack([
    np.vstack([img, suavizacaoGaussiana]),
    np.vstack([bin1,bin2]),
])

cv2.imshow("binarização adaptativa", resultado)

# plt.subplot(221), plt.imshow(img)
# plt.subplot(222), plt.imshow(suavizacaoGaussiana)
# plt.subplot(223), plt.imshow(bin1)
# plt.subplot(224), plt.imshow(bin2)


cv2.waitKey(0)
cv2.destroyAllWindows()
"""


""" # Thresholding otsu e riddler-calvard
"""
import mahotas  #conda install mahotas
import cv2
import numpy as np

img = cv2.imread("../cat.jpg")

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
suavizacaoGaussiana = cv2.GaussianBlur(img, (9,9), 0)

T = mahotas.thresholding.otsu(suavizacaoGaussiana)
temp = img.copy()
temp[temp > T] = 255
temp[temp < 255] = 0
temp = cv2.bitwise_not(temp)

T = mahotas.thresholding.rc(suavizacaoGaussiana)
temp2 = img.copy()
temp2[temp2 > T] = 255
temp2[temp2 < 255] = 0
temp2 = cv2.bitwise_not(temp2)

resultado = np.hstack([
    np.vstack([img, suavizacaoGaussiana]),
    np.vstack([temp, temp2]),
    
])

cv2.imshow("Binarização com Otsu e Riddler-Calvard", resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()