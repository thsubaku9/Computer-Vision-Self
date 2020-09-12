import cv2
import numpy as np

img = cv2.imread("C:\\Users\\kernel\\Pictures\\Saved Pictures\\meme.jpg")

img2 = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
ret,thresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow("thresholded",thresh)

b,g,r = cv2.split(img)
_,otsu_b = cv2.threshold(b,127,255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
_,otsu_g = cv2.threshold(g,100,255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
_,otsu_r = cv2.threshold(r,80,255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
otsu_out = cv2.merge([otsu_b,otsu_g,otsu_r])
cv2.imshow("otsu RGB",otsu_out)

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = cv2.filter2D(img,cv2.CV_8UC1,np.matmul(cv2.getGaussianKernel(3,1),cv2.getGaussianKernel(3,1).T))
adaptTh = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,7,2)
cv2.imshow("adapt",adaptTh)

cv2.waitKey(0)
cv2.destroyAllWindows()
