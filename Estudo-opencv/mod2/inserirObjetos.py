 # cria varios retangulos coloridos sobre a imagem
import cv2
imagem = cv2.imread('../entrada.jpg')
# imagem[0][0] = (0,255,0)
# imagem[0][1] = (0,255,0)
# imagem[0][2] = (0,255,0)
# imagem[1][0] = (0,255,0)
# imagem[2][0] = (0,255,0)
# imagem[2][2] = (0,255,0) 
imagem[30:100 , 70:100] = (0,255,0) #LINHA 31 A 100 #COLUNA 71 A 100
#Cria um quadrado vermelho
imagem[100:150, 50:100] = (0, 0, 255)
#Cria um retangulo amarelo por toda a altura da imagem
imagem[:, 200:220] = (0, 255, 255)
#Cria um retangulo verde da linha 150 a 300 nas colunas 250 a
350
imagem[150:300, 250:350] = (0, 255, 0)
#Cria um quadrado ciano da linha 150 a 300 nas colunas 250 a
350
imagem[300:400, 50:150] = (255, 255, 0)
#Cria um quadrado branco
imagem[250:350, 300:400] = (255, 255, 255)
#Cria um quadrado preto
imagem[70:100, 300: 450] = (0, 0, 0)
cv2.imwrite("alterada.jpg", imagem)
cv2.imshow("Imagem", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()

""""" # desenho de formas geometricas na imagem
import numpy as np
import cv2
imagem = cv2.imread('../entrada.jpg')
vermelho = (0, 0, 255)
verde = (0, 255, 0)
azul = (255, 0, 0)

#IMG, ALTURA?P_INICIAL?X LARGURA?P_FINAL?Y COR , ESPESSURA
cv2.line(imagem, (0, 0), (200, 300), verde)
cv2.line(imagem, (400, 300), (150, 150), vermelho, 5)
cv2.rectangle(imagem, (100, 100), (240, 240), azul, 10)
cv2.rectangle(imagem, (300, 150), (325, 225), verde, -1)

(X, Y) = (imagem.shape[1] // 2, imagem.shape[0] // 2)

for raio in range(0, 300, 50):
    cv2.circle(imagem, (X, Y), raio, vermelho)
    
cv2.imwrite("modificada.jpg", imagem)
cv2.imshow("Desenhando sobre a imagem", imagem)
cv2.waitKey(0)
"""""

""""" #escrita em imagem
import numpy as np
import cv2
imagem = cv2.imread('../entrada.jpg')
fonte = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagem,'OpenCV',(15,65), fonte,
2,(255,255,255),2,cv2.LINE_AA)
cv2.imshow("onça", imagem)
cv2.waitKey(0)
"""""
