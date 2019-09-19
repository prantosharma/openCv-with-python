import numpy as np
import cv2
#READ IMAGE
img=cv2.imread('circle.png',cv2.IMREAD_COLOR)
#GRAY THIS IMAGE
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

edges=cv2.Canny(gray,30,255)
cv2.imshow('edges',edges)
#BLUR IMAGE TO REDUCE NOISE
blur=cv2.medianBlur(gray,5)
#APPLY HOUGH TRANSFORM TO THE CIRCLE
circles=cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,
                          135,param1=200,param2=10,minRadius=5,maxRadius=30)
# #DRAW DETECTED CIRCLE
if circles is not None:
     circles=np.uint16(np.around(circles))
     for i in circles[0,:]:
         #DRAW OUTER CIRCLE
         cv2.circle(img,(i[0],i[1]),i[2],(255,0,0),2)
         #DRAW INNER CIRCLE
         cv2.circle(img,(i[0],i[1]),2,(0,255,0),3)

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()


