import cv2

vdo=cv2.VideoCapture(0)

while(1):
    ret, frame=vdo.read()
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


vdo.release()
cv2.destroyAllWindows()