import cv2
import numpy as np

img = cv2.imread("C:\\Users\\kernel\\Pictures\\Saved Pictures\\meme.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img,(5,5),1)
_,img_thresh = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
cv2.imshow("Thresh",img_thresh)

kernel = np.ones((5,5),np.uint8)

erode = cv2.erode(img_thresh,kernel,iterations = 1)
cv2.imshow("Erode",erode)

dilute = cv2.dilate(img_thresh,kernel,iterations = 1)
cv2.imshow("Dilate",dilute)

opening = cv2.morphologyEx(img_thresh,cv2.MORPH_OPEN,kernel)
cv2.imshow("opening",opening)

closing = cv2.morphologyEx(img_thresh,cv2.MORPH_CLOSE,kernel) 
cv2.imshow("closing",closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
