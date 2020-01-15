from mtcnn.mtcnn import MTCNN
import matplotlib.pyplot as plt
import cv2

image = cv2.imread('zamalek.jpg')

detector = MTCNN()

faces = detector.detect_faces(image)

for face in faces:

    x,y,w,h = face['box']
    
    print(face)
    cv2.rectangle(image,(x,y),(x+w,h+y),[255,0,0],3)

    cv2.circle(image,face['keypoints']['left_eye'],1,[0,255,0],-1)
    cv2.circle(image,face['keypoints']['right_eye'],1,[0,255,0],-1)

    cv2.circle(image,face['keypoints']['mouth_left'],1,[0,0,255],-1)
    cv2.circle(image,face['keypoints']['mouth_right'],1,[0,0,255],-1)

    cv2.circle(image,face['keypoints']['nose'],1,[255,0,255],-1)


cv2.imshow('Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()