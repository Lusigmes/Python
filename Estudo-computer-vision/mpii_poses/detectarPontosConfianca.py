import matplotlib.pyplot as plt
import cv2
import numpy as np

# CARREGAR IMAGEM
imagem = cv2.imread('jab1.jpg')
cv2.imshow("img",imagem)

print(imagem.shape) #(altura/y, largura/x, canais de cores) shape[0]=y shape[1]=x shape[2]=cc
# print(type(imagem))

imagem_blob = cv2.dnn.blobFromImage(image=imagem,
                                    scalefactor=1.0/255,
                                    size=(imagem.shape[1], imagem.shape[0]))

print("blob: ", imagem_blob.shape) #(nªimagens, canais de cores,altura/y, largura/x) shape[0]=img shape[1]=cc shape[2]=y shape[3]=x


# CARREGAR REDES NEURAIS PRE TREINADAS  
net = cv2.dnn.readNetFromCaffe(
    prototxt='pose_deploy_linevec_faster_4_stages.prototxt',
    caffeModel='pose_iter_160000.caffemodel')

# print(net.getLayerNames())
# print(len(net.getLayerNames()))

# PREVER PONTOS CORPORAIS
net.setInput(imagem_blob) # associar a imagem com a rerde neural
output = net.forward() # resultado da rede neural
print(output.shape) #(nª img, pontos detectados, altura, largura) h, w = redimentsionados formato blob
# print(output)

pos_x = output.shape[3]
pos_y = output.shape[2]
print(pos_x, pos_y)

# PERCORRERR RERSULTADOS
total_pontos = 15 
pontos = []
threshold = 0.1

for i in range(total_pontos): #print(i)
    mapa_confianca = output[0, i, :, :] 
    # print(mapa_confianca) # indicador de confiaça dos pontos detectados, com valores baiixo ou altos
    # print(len(mapa_confianca)) # qnt de pontos candidatos(em probabilidade) para cada ponto
    _, confianca, _, ponto = cv2.minMaxLoc(mapa_confianca) #param 1,3 = lixo, param 2,4 pontos de confiança mais altos e pontos x,y
    # print(confianca) # valores de confiança mais alto para cada ponto
    # print(ponto) 
    # localização (x,y) de onde o ponto foi localizado na imagem, imagem reduzida/pequena
    # output.shape[3] output.shape[2]
    
    x = int((imagem.shape[1] * ponto[0])/pos_x)
    y = int((imagem.shape[0] * ponto[1])/pos_y)
    # print(x,y) # gerar os valores x,y no tamanho original da iimagem
    
    if confianca > threshold: #verirficação de segurança para nao retornar pontos invalidos
        cv2.circle(imagem, (x,y), 2, (0,255,0), thickness= -1)
        cv2.putText(imagem, '{}'.format(i), (x,y), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.7,(0,0,255))
        pontos.append((x,y))
    else:
        pontos.append(None)
    # print(pontos)
    cv2.imshow("pontos detectados", imagem)
    
ponto_conexoes = [[0,1], [1,2], [2,3], [3,4], [1,5], [5,6], [6,7], [1, 14],
                  [14,8], [8,9], [9,10], [14,11], [11,12],[12,13]]
# print(ponto_conexoes)

for conexao in ponto_conexoes:
    # print(conexao)
    parte1 = conexao[0]
    parte2 = conexao[1]
    if pontos[parte1] and pontos[parte2]:
        cv2.line(imagem, pontos[parte1], pontos[parte2], (255,0,0))
    cv2.imshow("pontos conexaos", imagem)
        
cv2.waitKey(0)
cv2.destroyAllWindows()