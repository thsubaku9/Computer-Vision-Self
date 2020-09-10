import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("C:\\Users\\kernel\\Pictures\\Saved Pictures\\Metal_gear_solid_5_ground_zeroes-2481092.jpg")
img = cv2.resize(img, (600, 600))
cv2.imshow("IMG",img)
cv2.waitKey(1000)
cv2.destroyAllWindows()


color = ('b','g','r')


for i,col in enumerate(color):
    hist = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color = col)
    plt.xlim([0,256])

plt.show()
