import numpy as np
import cv2

img=cv2.imread('gradient.png',0)

#threshold has tow value.RET and THRESHOLD.for ret value the ' _ ' is here.
#thresh_binary is a thresholding type
_, th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#some other type of thresholding(THRESH_BINARY_INV,THRESH_TRUNC,THRESH_TOZERO,THRESH_TOZERO_INV)

cv2.imshow('image',img)
cv2.imshow('th1',th1)


cv2.waitKey(0)
cv2.destroyAllWindows()