import cv2
import numpy as np

#draw a black background with numpy but doing this comment the  imread  function

#img=np.zeros([600,700,3], np.uint8)

img=cv2.imread('lena.jpg',1)


#drawing different shape of lines

img=cv2.line(img,(0,0),(255,255),(255,0,0),5)
img=cv2.line(img,(255,0),(255,255),(255,0,0),5)
img=cv2.line(img,(0,255),(255,0),(255,0,0),5)
img=cv2.line(img,(200,100),(100,0),(255,0,0),5)
#arrowline
img=cv2.arrowedLine(img,(0,255),(0,255),(0,255,0),10)

#rectangle
img=cv2.rectangle(img,(384,0),(510,128),(0,255,0),6)
#fil linside
img=cv2.rectangle(img,(384,0),(510,128),(0,0,255),-1)
#put text
font=cv2.FONT_HERSHEY_PLAIN
img=cv2.putText(img,'OpenCv',(10,500),font,6,(255,255,0),7,cv2.LINE_8)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
