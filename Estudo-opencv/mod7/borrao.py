"""
Basta alterar a cor de cada pixel misturando a cor com os pixels ao seu redor.
Util quando há identificação de objetos em imagens pois os processos de detecção de bordas, 
por exemplo, funcionam melhor depois de aplicar uma suavização na imagem.
"""

""" # cálculo da média
    # soma o valor dos pixels ao redor do pixel selecionado, soma e atualiza a media
import cv2
import numpy as np
img = cv2.imread("../cat.jpg")
img = img[::2, ::2]

# blur(imagem, (janela de, suavização))
suavizarMedia = np.hstack([
    np.vstack([img,                  cv2.blur(img, (3,3))]),
    
    np.vstack([cv2.blur(img, (5,5)), cv2.blur(img, (7,7))]),
    
    np.vstack([cv2.blur(img, (9,9)), cv2.blur(img, (11,11))]),
])

cv2.imshow("Imagens suavizadas por média", suavizarMedia)
cv2.waitKey(0)
"""

""" # cálculo da mediana
# despreza valores muito altos e muito baixos que podem distorcer o resultado
# valor que fica no meio do intervalo
import cv2
import numpy as np
img = cv2.imread("../cat.jpg")
img = img[::2, ::2]

# medianBlur(imagem, tamanho da caixa/janela)
suavizarMediana = np.hstack([
    np.vstack([img,                    cv2.medianBlur(img, 3)]),
    
    np.vstack([cv2.medianBlur(img, 5), cv2.medianBlur(img, 7)]),
    
    np.vstack([cv2.medianBlur(img, 9), cv2.medianBlur(img, 11)]),
])

cv2.imshow("Imagens suavizadas por mediana", suavizarMediana)
cv2.waitKey(0)
"""

""" # filtro gaussiana
# gera menos borrão, produz um efeito mais natural e reduz o ruído na imagem
import cv2
import numpy as np
img = cv2.imread("../cat.jpg")
img = img[::2, ::2]

# GaussianBlur(imagem, (altura, largura) , desvios padrão no eixo X eY)
suavizarGaussiana = np.hstack([
    np.vstack([img, 
               cv2.GaussianBlur(img, (3,3), 0)]),
    
    np.vstack([cv2.GaussianBlur(img, (5,5), 0),
               cv2.GaussianBlur(img, (7,7), 0)]),
    
    np.vstack([cv2.GaussianBlur(img, (9,9), 0),
               cv2.GaussianBlur(img, (11,11), 0)]),
])
cv2.imshow("Imagens suavizadas pelo filtro Gaussiano", suavizarGaussiana)
cv2.waitKey(0)
"""


""" # filtro bilateral(mais lento que os anteriores)
# preserva as bordas e garante a remoção do ruído
"""
import cv2
import numpy as np
img = cv2.imread("../cat.jpg")
img = img[::2, ::2]
# bilateralFilter(imagem, tamanho janela,espaço de cor, espaço coordenado, borda)
suavizarBilateral = np.hstack([
    np.vstack([img,
               cv2.bilateralFilter(img, 3, 21, 21)]),
    
    np.vstack([cv2.bilateralFilter(img, 5, 35, 35),
               cv2.bilateralFilter(img, 7, 49, 49)]),
    
    np.vstack([cv2.bilateralFilter(img, 9, 63, 63),
               cv2.bilateralFilter(img, 11, 77, 77)]),
])
cv2.imshow("Imagens suavizadas pelo filtro bidirecional", suavizarBilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
