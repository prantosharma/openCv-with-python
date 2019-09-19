import numpy as np
import cv2
haar_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('we2.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
face=haar_cascade.detectMultiScale(gray,1.1,4)


for (x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()