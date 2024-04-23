""""" #altura, largura e canais de cores da imagem. exibe e clona a imagem aberta, sai com qualquer botao
# Importação das bibliotecas
import cv2
# Leitura da imagem com a função imread()
imagem = cv2.imread('../entrada.jpg')
print('Largura em pixels: ', end='')
print(imagem.shape[1]) #largura da imagem
print('Altura em pixels: ', end='')
print(imagem.shape[0]) #altura da imagem
print('Qtde de canais: ', end='')
print(imagem.shape[2])
# Mostra a imagem com a função imshow
cv2.imshow("Nome da janela", imagem)
cv2.waitKey(0) #espera pressionar qualquer tecla
# Salvar a imagem no disco com função imwrite()
cv2.imwrite("saida.jpg", imagem)
"""""

""""" #canal de cores bgr de cada posição do pixel
import cv2
imagem = cv2.imread('saida.jpg')
(b, g, r) = imagem[0, 0] 
print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)
"""""

""""" #muyda todos pixels para azul
import cv2
imagem = cv2.imread('saida.jpg')

for y in range(0, imagem.shape[0]):
    for x in range(0, imagem.shape[1]):
        imagem[y, x] = (255,0,0)
        cv2.imwrite("Imagem_modificada.jpg", imagem)
        # cv2.imshow("Imagem modificada", imagem)
"""""
        
""""" # resta da divisão por 256” para manter o resultado entre 0 e 255.
import cv2
imagem = cv2.imread('saida.jpg')
for y in range(0, imagem.shape[0]): #percorre linhas
    for x in range(0, imagem.shape[1]): #percorre colunas
        imagem[y, x] = (x%256,y%256,x%256)
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)
"""""

""""" # valores de linha multiplicado pela coluna (x*y) no componente “G” da tupla que
# forma a cor de cada pixel e deixamos o componente azul e vermelho zerados.
import cv2
imagem = cv2.imread('saida.jpg')
for y in range(0, imagem.shape[0], 1): #percorre as linhas
    for x in range(0, imagem.shape[1], 1): #percorre as colunas
        imagem[y, x] = (0,(x*y)%256,0)
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)
"""""

# salta a cada 10 pixels ao percorrer as linhas e mais 10 pixels ao
# percorrer as colunas. A cada salto é criado um quadrado roxo de 5x5 pixels. 
import cv2
imagem = cv2.imread('saida.jpg')
for y in range(0, imagem.shape[0], 10): #percorre linhas
    for x in range(0, imagem.shape[1], 10): #percorre colunas
        imagem[y:y+5, x: x+5] = (255,0,255)
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()