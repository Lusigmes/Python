# IDENTIFICA E RASTREIA ALGUMAS BORDAS MAS NÃO É TAO UTIL

import cv2
import numpy as np
import mahotas

peleMin = np.array([0,48,80], dtype="uint8")
peleMax = np.array([20,255,255], dtype="uint8")

def redimensionar(img, width):
    height = int(img.shape[0]/img.shape[1]*width)
    img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
    return img

def rastrear(video):
    # camera = cv2.VideoCapture(0)
    camera = cv2.VideoCapture('vid2.mp4')
    while True:
        (sucess, frame) = camera.read()
        if not sucess: break
        
        frameRed = redimensionar(frame, 400)
        imgC = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
        # imgC = redimensionar(imgC, 200)
        blurG_ = cv2.GaussianBlur(imgC, (33,33), 1)
    
        
        T = mahotas.thresholding.otsu(blurG_)
        
        bin_img = np.zeros_like(imgC)
        bin_img[imgC > T] = 255
        bin_img[bin_img < 255] = 0
        bin_img = cv2.bitwise_not(bin_img)
        
        canny_ = cv2.Canny(bin_img,50,150)
        
        frameAux = frame.copy()
        
        contornos, lx = cv2.findContours(canny_.copy(),
                                        cv2.RETR_EXTERNAL,
                                        cv2.CHAIN_APPROX_SIMPLE)
        
        for contorno in contornos:
            area = cv2.contourArea(contorno)
            if area > 30:
                x,y,w,h = cv2.boundingRect(contorno)
                cv2.rectangle(frameAux, (x,y), (x+w,y+h), (20,255,10),2)
     
                
        cv2.imshow("Rastreio", frameAux)
        cv2.imshow("bin", bin_img)
        
        if cv2.waitKey(1) & 0xFF==ord("x"): break
    camera.release()
    cv2.destroyAllWindows()
    
rastrear("vid.mp4")