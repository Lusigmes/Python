# MOSTRA A CONTAGEM DE FACES ENCONTRARDAS, E A POSIÇÃO DE CADA
import cv2
img = cv2.imread('../img_pessoas/p.jpg')
imgC = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

detector = cv2.CascadeClassifier('hc/haarcascade_frontalface_default.xml')
faces = detector.detectMultiScale(imgC,scaleFactor= 1.1,
                                  minNeighbors=7,
                                  minSize=(30,30),
                                  flags=cv2.CASCADE_SCALE_IMAGE)
print(len(faces))
print(faces)
# [xFace , yFace, largura, altura]

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (200, 0, 130), 3)
    
cv2.imshow("faces detectadas", img)
cv2.waitKey(0)
cv2.destroyAllWindows()