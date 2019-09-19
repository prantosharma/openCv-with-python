import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('messi5.jpg',cv2.IMREAD_GRAYSCALE)  #cv2.IMREAD_GRAYSCALE=0 same
lap=cv2.Laplacian(img, cv2.CV_64F, ksize=3)
lap=np.uint8(np.absolute(lap))
sobelX=cv2.Sobel(img,cv2.CV_64F,1,0)
sobelY=cv2.Sobel(img,cv2.CV_64F,0,1)

sobelX=np.uint8(np.absolute(sobelX))
sobelY=np.uint8(np.absolute(sobelY))


titles=['orginal image','laplacian','SobelX','sobelY']
images=[img,lap,sobelX,sobelY]

for i in range(4):
    plt.subplot(2,2,i+1), plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()