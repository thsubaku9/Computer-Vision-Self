import cv2
import numpy as np

img = cv2.imread("F:\\Computer Vision\\chickadins.jpg")
b1 = cv2.GaussianBlur(img,(5,5),1)
b1 = cv2.GaussianBlur(b1,(5,5),1)

diff = cv2.subtract(img,b1)
cv2.imshow("diff",diff)

diff = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(diff,256,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,1)
cv2.imshow("thresh",thresh)


sobel_x = cv2.Sobel(img,-1,0,1,ksize = 5)
sobel_y = cv2.Sobel(img,-1,1,0,ksize = 5)
ored = cv2.bitwise_or(sobel_x,sobel_y)
cv2.imshow("result",ored)

laplacian = cv2.Laplacian(img,-1,5)
cv2.imshow("Laplacian",laplacian)

canny = cv2.Canny(img,50,250)
cv2.imshow("canny",canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
