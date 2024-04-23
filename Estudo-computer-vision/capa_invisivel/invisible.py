import cv2
import time
import numpy as np

camera = cv2.VideoCapture(0)
time.sleep(3)
backg = 0

for i in range(60):
    sucess, backg = camera.read()
    
backg = np.flip(backg, axis=1)
    
while camera.isOpened():
    sucess, video = camera.read()
    
    if not sucess: break

    video = np.flip(video, axis=1)
    videoHSV = cv2.cvtColor(video, cv2.COLOR_BGR2HSV)

    # valores do manto
    orangeLower = np.array([0, 100 , 100])
    orangeUpper = np.array([20, 255, 255])
    
    mask1 = cv2.inRange(videoHSV, orangeLower, orangeUpper)
    
    orangeLower = np.array([5, 100, 100])
    orangeUpper = np.array([255, 10, 255])
    
    mask2 = cv2.inRange(videoHSV, orangeLower, orangeUpper)
    
    mask1 = mask1 + mask2

    # remover ruídos
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations= 2)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3), np.uint8), iterations= 1)
    
    mask2 = cv2.bitwise_not(mask1)
    
    response_bg_mask = cv2.bitwise_and(backg, backg, mask=mask1)
    response_vd_mask = cv2.bitwise_and(video,video,mask=mask2)
    
    output = cv2.addWeighted(response_bg_mask, 1, response_vd_mask, 1, 0)
    

    cv2.imshow("img", output)
    
    if (cv2.waitKey(1) & 0xFF)== ord('x'): break
    
camera.release()
cv2.destroyAllWindows()
# RGB: (255, 165, 0). Em BGR: (0, 165, 255).