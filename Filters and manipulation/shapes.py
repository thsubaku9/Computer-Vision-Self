import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

cv2.line(img,(0,0),(255,511),(255,0,0),5)
cv2.line(img,(255,511),(511,0),(0,0,255),5)
cv2.rectangle(img,(200,200),(300,300),(127,255,127),-1)
pts = np.array([[50,50],[80,80],[60,70],[100,80],[70,60]])
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255),6)
cv2.imshow("line",img)
cv2.waitKey()
cv2.destroyAllWindows()
