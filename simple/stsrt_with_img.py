import cv2

img = cv2.imread('lena.jpg',-1)  #use three tpye number 0,1,-1

print(img)

cv2.imshow('photo',img)

k=cv2.waitKey(0)
if k ==27: #Esc to stop
    cv2.destroyAllWindows()  #destroy a perticular window
elif k==ord("s"): #builtin function ord()
    cv2.imwrite('lena_copy.jpg',img)
    cv2.destroyAllWindows()
        