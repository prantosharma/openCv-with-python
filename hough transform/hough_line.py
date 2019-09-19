import numpy as np
import cv2

#READ IMAGE
img=cv2.imread('sudoku.png',cv2.IMREAD_COLOR) #if i use 1(cv2.imread_color)it gives same result
#CONVERT TO GRAYSCALE IMAGE
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#FINF THE IMAGE EDGE WITH CANNY DETECTOR
edges=cv2.Canny(gray,50,150)
cv2.imshow('edge',edges)
#DETECT LINES
lines=cv2.HoughLinesP(edges,1,np.pi/180,100, minLineLength=100,maxLineGap=10)
for line in lines:
    x1,y1,x2,y2=line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),3)

#SHOW IMAGE
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

