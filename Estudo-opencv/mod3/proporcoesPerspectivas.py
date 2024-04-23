""""" #recortando img
import cv2
imagem = cv2.imread('../entrada.jpg')
recorte = imagem[436:512, 605:739] #linha 436+1 até 512 e coluna 605+1 até 739
cv2.imwrite("recorte.jpg", recorte) #salva no disco
cv2.imshow("Recorte da imagem", recorte)
cv2.waitKey(0)
"""""

""""" #função ‘rezise’ utiliza uma propriedade aqui definida como
        # cv2.INTER_AREA que é uma especificação do cálculo matemático para redimensionar a imagem.
import numpy as np
import cv2
imagem = cv2.imread('../entrada.jpg')
cv2.imshow("Original", imagem)

largura = imagem.shape[1]
altura = imagem.shape[0]
proporcao = float(altura/largura)
print(largura)
print(altura)
print(proporcao)

largura_nova = 320 #em pixels
altura_nova = int(largura_nova*proporcao)
tamanho_novo = (largura_nova, altura_nova)
print(largura_nova)
print(altura_nova)
print(tamanho_novo)

img_redimensionada = cv2.resize(imagem,
tamanho_novo, interpolation = cv2.INTER_AREA)
cv2.imshow('Resultado', img_redimensionada)
cv2.waitKey(0)
"""""

#redimensionando imagem com tecnica de slicing, redimensionando até 1/4 da imagem original
import numpy as np
import cv2
# import imutils
img = cv2.imread('../entrada.jpg')
cv2.imshow("Original", img)

img_redimensionada = img[::2,::2]
cv2.imshow("Imagem redimensionada", img_redimensionada)
cv2.waitKey(0)
cv2.destroyAllWindows()