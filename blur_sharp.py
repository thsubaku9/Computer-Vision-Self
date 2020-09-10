import cv2
import numpy as np

def gauss_kern(dim):
    gaussMat = np.zeros((dim,dim),np.float32)
    averaging_value = 0
    for i in range(0,dim):
        for j in range(0,dim):
            gaussMat[i][j] = (np.exp((-(i - int(dim/2))**2 -(j - int(dim/2))**2)/2))
            averaging_value += gaussMat[i][j]    
    return gaussMat/averaging_value

def sharp_kern(dim):
    sharpkern = np.ones((dim,dim)) * -1
    mid = int(dim/2)
    sharpkern[mid][mid] = dim*dim
    return sharpkern

img = cv2.imread("C:\\Users\\kernel\\Pictures\\Saved Pictures\\meme.jpg")
cv2.imshow("img",img)

kernel_9x9 = np.ones((9,9),np.float32)/(np.multiply(9,9))
blurred = cv2.filter2D(img,cv2.CV_8U,kernel_9x9)
cv2.imshow("9x9 blur",blurred)

gaussMat = gauss_kern(3)
blurred2 = cv2.filter2D(img,-1,gaussMat)
cv2.imshow("gauss",blurred2)

bilateral = cv2.bilateralFilter(img,9,75,75)
cv2.imshow("bilateral",bilateral)

sharpener = sharp_kern(5)
sharpener[2][2] = 5*5
sharped = cv2.filter2D(img,-1,sharpener)
cv2.imshow("sharp",sharped)

cv2.waitKey(10000)
cv2.destroyAllWindows()
