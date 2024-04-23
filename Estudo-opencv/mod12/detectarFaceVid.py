# Detecta face e olhos, pela webcam 
# porem o delimitador dos olhos oscilam e detectam falsos positivos
import numpy as np
import cv2

# def redimensionar(img, width):
#     height = int(img.shape[0]/img.shape[1]*width)
#     img = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
#     return img

# video = cv2.VideoCapture('')
video = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while(True):
	(sucess, frame) = video.read()
	if not sucess: break

	# frame = redimensionar(frame,200)
	frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
	faces = face_cascade.detectMultiScale(frame_gray,scaleFactor=1.3,
                                       minNeighbors=5, 
                                       minSize=(20,20),
                                       flags=cv2.CASCADE_SCALE_IMAGE )
 
	frame_aux = frame.copy()
 
	for (x,y,w,h) in faces:
		cv2.rectangle(frame_aux,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray = frame_gray[y:y+h, x:x+w]# cv2.imshow("roi",roi_gray)
		roi_color = frame_aux[y:y+h, x:x+w]# cv2.imshow("roi_c",roi_color)
		eyes = eye_cascade.detectMultiScale(roi_gray)
  
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)



	# cv2.imshow("Buscando faces:", redimensionar(frame_aux, 640))
	cv2.imshow("Buscando faces:", frame_aux)


	if(cv2.waitKey(1) & 0xFF == ord('x')):     	break

video.release()
cv2.destroyAllWindows()
