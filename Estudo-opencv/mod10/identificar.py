import cv2
import mahotas
import numpy as np

imagem = cv2.imread("../1.jpg")

img = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# suavizar = cv2.blur(img,(35,35))
suavizar = cv2.blur(img,(3,3))

# (T, bin) = cv2.threshold(suavizar, 240, 255, cv2.THRESH_BINARY) # binarização com limiar
# T = mahotas.thresholding.rc(suavizar)
T = mahotas.thresholding.otsu(suavizar)
bin = suavizar.copy()
bin[bin > T] = 255
bin[bin < 255] = 0
bin = cv2.bitwise_not(bin)

bordas = cv2.Canny(bin,80,200)

contorno, lx = cv2.findContours(bordas.copy(), 
                                cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
# cv.findContours(	image, mode, method[, contours[, hierarchy[, offset]]]	) -> 	image, contours, hierarchy

def esc(img, texto, cor=(0,0,255)):
    fonte = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(img, texto, (10,20), fonte, 0.5, cor, 0, cv2.LINE_AA)

esc(img, "cinza", 0)
esc(suavizar, "blur", 0)
esc(bin, "otsu", 255)
esc(bordas, "canny", 255)

resultado = np.hstack([
    np.vstack([img, suavizar]),
    np.vstack([bin, bordas]),
])
cv2.imshow("Resultado: "+ str(len(contorno)), resultado)
cv2.waitKey(0)

imagemc = imagem.copy()
cv2.imshow("Original: ", imagem)

cv2.drawContours(imagemc, contorno, -1, (0,255,0), 2)
esc(imagemc, str(len(contorno)) + " objetos encontradas")
cv2.imshow("Resultado: ", imagemc)

cv2.waitKey(0)
cv2.destroyAllWindows()