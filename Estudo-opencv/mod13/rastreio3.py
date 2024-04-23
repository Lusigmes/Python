# seleciona o objeto com a bound box(ROI)
# e rastreia o objeto durante o video. é util em alguns casos
import cv2
import sys
from random import randint

(major_ver, minor_ver, submionor_ver) = (cv2.__version__).split('.')

trackerTypes = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'MOSSE', "CSRT"]
trackerType = trackerTypes[6]

if int(minor_ver) < 3:
    tracker = trackerType
else:
    if trackerType == 'BOOSTING':
        0
    if trackerType == 'MIL':
        tracker = cv2.TrackerMIL.create()
    if trackerType == 'KCF':
        tracker = cv2.TrackerKCF.create()
    if trackerType == 'TLD':
        0 
    if trackerType == 'MEDIANFLOW':
        0 
    if trackerType == 'MOSSE':
        0
    if trackerType == 'CSRT':
        tracker = cv2.TrackerCSRT.create()
# print(tracker)

# video = cv2.VideoCapture(0)
video = cv2.VideoCapture('vid2.mp4')
if not video.isOpened():
    print("Nao foi possivel carregar o video")
    sys.exit()

(sucess, frame) = video.read()
if not sucess:
    print("Nao é possivel ler o arquivo do video")
    sys.exit()
    
bbox = cv2.selectROI(frame, False)# print("bbox: ",bbox)
sucess = tracker.init(frame, bbox)
cor = (randint(0, 255),randint(0, 255),randint(0, 255))
    
while True:
    sucess, frame = video.read()
    if not sucess: break
    
    timer = cv2.getTickCount()
   
    sucess, bbox = tracker.update(frame) # print("sucess: ",sucess)    # print("bbox in loop: ",bbox)
   
    fps = cv2.getTickFrequency()/ (cv2.getTickCount() - timer)
       
    if sucess:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x,y), (x+w, y+h), cor, 2, 1)# cv2.rectangle(image, start_point, end_point, color, thickness) 
    else:
        cv2.putText(frame, "Falha em rastrear ", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, .75, (0, 0, 255), 2)
     
    cv2.putText(frame, "Rastreador "+trackerType, (100, 20), cv2.FONT_HERSHEY_SIMPLEX, .75, (15, 220, 0), 2)
    cv2.putText(frame, "FPS: "+str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, .75, (255, 40, 0), 2)

    cv2.imshow("Rastreio", frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord("x"): break

video.release()
cv2.waitKey(0)
cv2.destroyAllWindows()