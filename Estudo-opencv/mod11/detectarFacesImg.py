# TENTA CONTAR QUANTAS FACES, OLHOS E SORRRISOS NA FOTO. 
# PRECISO MELHORAR PARA OBTER O RESULTADO DESEJADO
import cv2
import numpy as np
import os 

diretorio = '../img_pessoas'
arquivos = os.listdir(diretorio)
for arq in arquivos:
    if arq.lower().endswith('.jpg') or arq.lower().endswith('.png') or arq.lower().endswith('.jpeg'):
        img = cv2.imread(diretorio+'/'+arq)
        imgC = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        detector_face = cv2.CascadeClassifier('hc/haarcascade_frontalface_default.xml')
        detector_eye = cv2.CascadeClassifier('hc/haarcascade_eye.xml')
        detector_smile = cv2.CascadeClassifier('hc/haarcascade_smile.xml')
        
        faces = detector_face.detectMultiScale(imgC, scaleFactor= 1.1, minNeighbors=7,
                                                minSize=(30,30), flags=cv2.CASCADE_SCALE_IMAGE) 
        count_smiles = 0
        count_eyes = 0
        for (x, y, w, h) in faces:
            # cv2.rectangle(image, start_point, end_point, color, thickness) 
            cv2.rectangle(imgC, (x,y), (x+w, y+h), (0, 255, 255), 7 )
            
            roi_gray = imgC[y:y+h, x:x+w]
            roi_bgr = img[y:y+h, x:x+w]
            
            eyes = detector_eye.detectMultiScale(roi_gray)
            for(ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_bgr, (ex,ey), (ex+ew, ey+eh), (100, 100, 0), 2 )
                count_eyes=+1
                
            smiles = detector_smile.detectMultiScale(roi_gray, 1.6, 20)
            for(sx, sy, sw, sh) in smiles:
                cv2.rectangle(imgC, (sx,sy), (sx+sw, sy+sh), (0, 100, 100), 2 )
                count_smiles+=1
                
        alt = int(imgC.shape[0]/imgC.shape[1]+640)
        img_resized = cv2.resize(imgC, (640, alt), interpolation=cv2.INTER_CUBIC)
        
        cv2.imshow(f"{len(faces)} face(s) encontrada(s). {count_eyes} eyes and {count_smiles} smiles detected", img_resized)       
        cv2.waitKey(0)
        cv2.destroyAllWindows()  
        