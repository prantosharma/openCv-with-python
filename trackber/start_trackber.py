import numpy as np
import cv2

def track_fun(x): #this function print the trackber position value
    print(x)
#create black image and window
img=np.zeros((255,500,3),np.uint8)

cv2.createTrackbar('B','image',0,255, track_fun) #track_fun is a callback function
cv2.createTrackbar('G','image',0,255, track_fun)
cv2.createTrackbar('R','image',0,255, track_fun)
while(True):
    cv2.imshow('image',img)
    k = cv2.waitKey(1)
    if k==27:
        break
cv2.destroyAllWindows()
