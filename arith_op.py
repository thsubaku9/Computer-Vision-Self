import cv2
import numpy as np

img = cv2.imread("C:\\Users\\kernel\\Pictures\\Saved Pictures\\meme.jpg")

square = np.zeros((300,300),np.uint8)
cv2.rectangle(square,(50,50),(250,250),255,-1)
cv2.imshow("Square",square)

ellipse = np.zeros((300,300),np.uint8)
cv2.ellipse(ellipse, (150,150), (150,50), 45 , 0, 360, 255, -1)
cv2.ellipse(ellipse, (150,150), (150,50), 135 , 0, 360, 255, -1)
cv2.imshow("Ellipse",ellipse)

anded = cv2.bitwise_and(square,ellipse)
cv2.imshow("anded",anded)

ored = cv2.bitwise_or(square,ellipse)
cv2.imshow("ored",ored)


noted = cv2.bitwise_not(ellipse)
cv2.imshow("noted",noted)

xored = cv2.bitwise_xor(square,ellipse)
cv2.imshow("xored",xored)


cv2.waitKey(20000)
cv2.destroyAllWindows()
