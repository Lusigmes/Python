""""" # 2 HISTOGRAMS DA IMAGEM CINZA E BGR
# x = intensidade do pixiel /y = quantidade de pixels daquela intensidade
import numpy as np
import cv2
from matplotlib import pyplot as plt

# Carregar a imagem
img = cv2.imread('../images.jpg')
# Dividir a imagem nos canais de cores cinza
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converte P&B
cv2.imshow("Imagem P&B", img2)

histogramaCinza = cv2.calcHist([img2], [0], None, [256], [0, 256])
# Dividir a imagem nos canais de cores BGR
(canalAzul, canalVerde, canalVermelho) = cv2.split(img)
# Calcular o histograma de cada canal de cor
histogramaAzul = cv2.calcHist([canalAzul], [0], None, [256], [0, 256])
histogramaVerde = cv2.calcHist([canalVerde], [0], None, [256], [0, 256])
histogramaVermelho = cv2.calcHist([canalVermelho], [0], None, [256], [0, 256])

# Plotar os histogramas
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(histogramaCinza, color='black', label='Cinza')
plt.xlim([0, 256])
plt.title("Histograma Cinza")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")

plt.subplot(1, 2, 2)
plt.plot(histogramaAzul, color='blue', label='Azul')
plt.plot(histogramaVerde, color='green', label='Verde')
plt.plot(histogramaVermelho, color='red', label='Vermelho')
plt.xlim([0, 256])
plt.title("Histograma BGR")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")

plt.legend()
plt.show()

cv2.waitKey(0)
"""""

""""" # HISTOGRARMA NA ESCALA CINZA
import matplotlib.pyplot as plt
import cv2
img = cv2.imread('../entrada.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converte P&B
cv2.imshow("Imagem P&B", img)

#Função calcHist para calcular o hisograma da imagem
h = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.figure()
plt.title("Histograma P&B")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.plot(h)
plt.xlim([0, 256])
plt.hist(img.ravel(),256,[0,256]) #espaço onde nao existe pixel
plt.show()
cv2.waitKey(0)
"""""

""""" # plota o grafico nos 3 canais de cores passados
from matplotlib import pyplot as plt
import numpy as np
import cv2
img = cv2.imread('../images.jpg')
cv2.imshow("Imagem Colorida", img)
#Separa os canais
canais = cv2.split(img)
cores = ("b", "g", "r")

plt.figure()
plt.title("Histograma Colorido")
plt.xlabel("Intensidade")
plt.ylabel("Número de Pixels")

for (canal, cor) in zip(canais, cores): #cria lista de tuplas formada pela uniao das listas passadas
    #Este loop executa 3 vezes, uma para cada canal
    hist = cv2.calcHist([canal], [0], None, [256], [0, 256])
    plt.plot(hist, color = cor)
plt.xlim([0, 256])
plt.show()
"""""


# A intenção neste caso é distribuir de forma mais uniforme as intensidades dos pixels sobre a imagem
#  No histograma é possível identificar a diferença pois o acumulo de pixels próximo a alguns valores é suavizado.

# Perceba que a equalização faz com que a distribuição das intensidades dos pixels de 0
# a 255 seja uniforme. Portanto teremos a mesma quantidade de pixels com valores na faixa de
# 0 a 10 (pixels muito escuros) e na faixa de 245 a 255 (pixels muito claros).

# Dessa forma temos uma distribuição mais uniforme das intensidades dos pixels na 
# imagem. Lembre-se que detalhes podem inclusive serem perdidos com este processamento de imagem.
# é garantido é o aumento de contraste

from matplotlib import pyplot as plt
import numpy as np
import cv2
img = cv2.imread('../entrada.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h_eq = cv2.equalizeHist(img)

plt.figure()
plt.title("Histograma Equalizado")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(h_eq.ravel(), 256, [0,256])
plt.xlim([0, 256])
plt.show()

plt.figure()
plt.title("Histograma Original")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(img.ravel(), 256, [0,256])
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
