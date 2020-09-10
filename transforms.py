import cv2
import numpy as np

def show_img(title,img):
    cv2.imshow(title,img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

img = cv2.imread("C:\\Users\\kernel\\Pictures\\Saved Pictures\\Metal_gear_solid_5_ground_zeroes-2481092.jpg")
img = cv2.resize(img,(int(img.shape[0]/3),int(img.shape[1]/3)))
show_img("standard",img)
height,width = img.shape[:2]

x_shift = 50
y_shift = 50
Translation_Mat = np.float32([[1,0,x_shift],[0,1,y_shift]])
img_translate = cv2.warpAffine(img,Translation_Mat,(height,width))
show_img("translate",img_translate)

Rotation_Mat = cv2.getRotationMatrix2D((width/2,height/2),90,0.5)
img_rotate = cv2.warpAffine(img,Rotation_Mat,(height,width))
show_img("center_rotation",img_rotate)

downscale = cv2.pyrDown(img)
show_img("downscale",downscale)
upscale = cv2.pyrUp(img)
show_img("upscale",upscale)
