import cv2
import numpy as np

img = cv2.imread("F:\\Computer Vision\\chickadins.jpg")

pt_org = np.float32([[200,200],[300,500],[450,100],[500,700]])

pt_non_affine = np.float32([[0,0],[0,420],[300,0],[300,420]])

M = cv2.getPerspectiveTransform(pt_org,pt_non_affine)

warp = cv2.warpPerspective(img,M,(500,300))

cv2.imshow("Non-affine warp",warp)

cv2.waitKey(0)
cv2.destroyAllWindows()
