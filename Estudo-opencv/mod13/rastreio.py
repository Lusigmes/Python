# NÃO IDWENTIFICA NADA UTIL

import cv2
import numpy as np

azulEscuro = np.array([100, 67, 0], dtype=  "uint8")
azulClaro = np.array([255,128 , 50], dtype="uint8")

# camera = cv2.VideoCapture(0)
camera = cv2.VideoCapture('vid2.mp4')

while True:
    (sucess, frame) = camera.read()
    if not sucess:
        break
    obj = cv2.inRange(frame, azulEscuro, azulClaro)
    obj = cv2.GaussianBlur(obj,(3,3), 0)
    
    contorno, lx = cv2.findContours(obj.copy(),
                                        cv2.RETR_EXTERNAL, 
                                        cv2.CHAIN_APPROX_SIMPLE)
    
    if len(contorno) > 0:
        cnt = sorted(contorno, key=cv2.contourArea, reverse=True)[0]
        
        rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
        cv2.drawContours(frame, [rect], -1, (0, 255, 255), 2)
    
    cv2.imshow("rastreio", frame)
    # cv2.imshow("obj binario", obj)
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break

camera.release()
cv2.destroyAllWindows()