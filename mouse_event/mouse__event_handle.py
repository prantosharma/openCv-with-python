import numpy as np
import cv2

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print (events)

#mouse call back function

def click_e(event,x,y,flags,param):
     if event == cv2.EVENT_LBUTTONDOWN:
         print(x,' ',y)
         strn=str(x)+' '+str(y)
         font=cv2.FONT_HERSHEY_SIMPLEX
         cv2.putText(img,strn,(x,y),font,.5,(255,0,0),1)
         cv2.imshow('image',img)
     if event == cv2.EVENT_RBUTTONDOWN:
         print(y, ' ', x)
         strn = str(y) + ' ' + str(x)
         font = cv2.FONT_HERSHEY_SIMPLEX
         cv2.putText(img, strn, (x, y), font, .5, (255, 255, 0), 1)
         cv2.imshow('image', img)


img=np.zeros((512,512,3),np.uint8)
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_e)

cv2.waitKey(0)
cv2.destroyAllWindows()




#create a circle

# def draw_circle(event,x,y,flags,param):
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(img,(x,y),100,(255,0,0),-1)
#
# # Create a black image, a window and bind the function to window
# img = np.zeros((512,512,3), np.uint8)
# cv2.imshow('image',img)
# cv2.setMouseCallback('image',draw_circle)
#
# while(1):
#     cv2.imshow('image',img)
#     if cv2.waitKey(20) & 0xFF == 27: #Esc to stop
#         break
# cv2.destroyAllWindows()