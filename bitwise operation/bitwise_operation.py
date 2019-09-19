import numpy as np
import cv2

first_img=np.zeros((255,500,3),np.uint8)
first_img=cv2.rectangle(first_img,(200,0),(300,100),(255,255,255),-1)
img1=cv2.imread('pic.png')

bitand=cv2.bitwise_and(img1, first_img)

cv2.imshow('image',first_img)
cv2.imshow('picture',img1)
cv2.imshow("bitwiseImage",bitand)

cv2.waitKey(0)
cv2.destroyAllWindows()