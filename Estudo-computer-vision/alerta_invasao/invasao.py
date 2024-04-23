import cv2
from ultralytics import YOLO
from alarme import alarme,alarmeControl # passo 3 alarme
import threading # passo 3 - processamento do arlarme em paralelo com o video

model = YOLO('yolov8n.pt')
# video = cv2.VideoCapture('steal.mp4')
# area_invasao = [90,415,500,490] # passo 2: criar area de invasao
video = cv2.VideoCapture('ex02.mp4')
area_invasao = [100,190, 1150,700] # passo 2: criar area de invasao

while True:
    sucess, frame = video.read()
    if not sucess: break
    
    # frame = cv2.resize(frame, (700,478))
    frame = cv2.resize(frame, (1270,720))
    
    frame_invasao = frame.copy() # passo 2
    cv2.rectangle(frame_invasao, (area_invasao[0],area_invasao[1]), (area_invasao[2],area_invasao[3]),(0,255,0),-1) # passo 2
   
    
    resultado = model(frame) # passo 1
    
    for objetos in resultado: # passo 1: detectar uma pessoa no frame
        obj = objetos.boxes
        for dados in obj:
            x,y,w,h = dados.xyxy[0]
            x,y,w,h = int(x),int(y),int(w),int(h)
            # print(x,y,w,h)
            pessoas_detectadas = int(dados.cls[0])
            cx, cy = (x+w)//2, (y+h)//2 # passo 2 - centro do objeto
            # cv2.circle(img=frame, center=(cx,cy), radius=3, color=(0,0,0),thickness=5)# passo 2
            if pessoas_detectadas == 0:
                cv2.rectangle(frame, (x,y), (w,h),(0,0,255),3)
            # fim passo 1
                #passo 2 #centro de x e y tem de estrar entre ponto inicial e final que foi definido para x e y
                if cx >= area_invasao[0] and cx <= area_invasao[2] and cy >= area_invasao[1] and cy <= area_invasao[3]:
                    cv2.rectangle(frame_invasao, (area_invasao[0],area_invasao[1]), (area_invasao[2],area_invasao[3]),(0,0,255),-1) # passo 2
                    cv2.rectangle(frame, (100,30),(450,80),(0,0,255),-1) # passo 2
                    cv2.putText(img=frame, text="INVASOR DETECTADO", org=(105,65), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,color=(255,255,255), thickness=3) # passo 2
                #fim passo 2   
                    if not alarmeControl: # passo 3 - controle de ativação do alarme
                        alarmeControl = True # passo 3
                        threading.Thread(target=alarme).start() # passo 3
                        
                    #fim passo 3   
    frame_completo = cv2.addWeighted(frame_invasao,0.5,frame,0.5, 0) # passo 2 -> garante opacidade
    cv2.imshow("camera",frame_completo)
    if cv2.waitKey(1) & 0xFF == ord('x'): break
    
cv2.destroyAllWindows()