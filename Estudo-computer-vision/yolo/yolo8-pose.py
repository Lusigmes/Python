from ultralytics import YOLO
import cv2

model = YOLO('yolov8n-pose.pt')

img = cv2.imread("boxe.jpg")
results = model('boxe.jpg')

keypoints = results[0].keypoints
# keypoint = keypoints[0] 

# print(keypoints[1].conf)
# print(keypoint.conf)

print("keypoints confiança", keypoints.conf)
kconfs = keypoints.conf
for kconf in kconfs:
    for k in kconf:
        print(float(k))

for point_tensor in keypoints.xy: 
    for point in point_tensor:
        
        x,y = int(point[0]), int(point[1])
        print("X:",x ," Y:",y)
        
        img = cv2.circle(img=img, center=(x, y), radius=3, color=(0, 0, 255), thickness=2)
        
    print("len total pontos", len(point_tensor))  
    
boxes = results[0].boxes
# box = boxes[0]
xyxys = boxes.xyxy

print("boxes class id", boxes.cls)
print("boxes confiança", boxes.conf)
bconfs = boxes.conf
for bconf in  bconfs:
    print(float(bconf))
    
for xyxy in xyxys:
    cv2.rectangle(img, (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3])), (0,255,0),1)

print("Executou até aqui")

cv2.imshow("img".encode("unicode_escape").decode(), img)
cv2.imshow("plot".encode("unicode_escape").decode(), results[0].plot())

cv2.waitKey(0)
cv2.destroyAllWindows()


''' boxes
boxes = results[0].boxes
box = boxes[0]

print("box.xyxy--->",box.xyxy)
print("box.xywh--->",box.xywh)
print("box.data--->",box.data)
print("box.conf--->",box.conf)
print("box.cls--->",box.cls)
'''
''' masks
masks = results[0].masks
mask = masks[0]

print("masks.xy--->",mask.xy)
print("masks.xyn--->",mask.xyn)
print("masks.data--->",mask.data)
'''
""" keypoints
keypoints = results[0].keypoints
keypoint = keypoints[1] 
# usar keypooints[]. para tratar todos / usar keypoint e escolher qual objeto tratar la em cima
# keypoint = keypoints[0], keypoints[1] ... keypoints[N encontrados], cada posição de keypoints[] trata informações de cada objeto encontrado
#usar keypoint, trata o objeto individualmente / usar keipoints trata todos os objetos encontrados
# print("keypoints.xy--->",keypoints.xy) # print("keypoints.xyn--->",keypoints.xyn)
# print("keypoints.conf--->",keypoints.conf) # print("keypoints.data--->",keypoints.data) # print("keypoints.data tam--->",len(keypoints.data))
# print(keypoint.xy) # xy = keypoint.xy # print (xy)

"""
"""probs
probs = results[0].probs
print("probs.top5--->",probs.top5)
print("probs.top1--->",probs.top1)
print("probs.top5conf--->",probs.top5conf)
print("probs.top1conf--->",probs.top1conf)
print("probs.data--->",probs.data)
"""

