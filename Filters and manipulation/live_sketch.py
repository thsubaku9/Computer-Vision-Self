import cv2
import numpy as np
import _thread


sharpener = np.ones((5,5)) *-1
sharpener[2][2] = 5*5

def start_capture(filter_fn,video_feed,caption):
    while True:
        _,frame = video_feed.read()
        cv2.imshow(caption,filter_fn(frame))
        if cv2.waitKey(1) == 13:            
            break

def identity(frame):
    return frame

def sketcher(frame):
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    smooth = cv2.medianBlur(gray,5)
    canny = cv2.Canny(smooth,50,200)    
    _,mask = cv2.threshold(canny,50,255,cv2.THRESH_BINARY_INV)
    return mask

def cartoonate(frame):
    img_pyr = frame
    for i in range(2):
        img_pyr = cv2.pyrDown(img_pyr)
    for j in range(5):
        img_pyr = cv2.bilateralFilter(img_pyr,3,7,9)
    for i in range(2):
        img_pyr = cv2.pyrUp(img_pyr)

    global sharpener
    img_gray = cv2.cvtColor(img_pyr,cv2.COLOR_BGR2GRAY)
    img_blur = cv2.medianBlur(img_gray,7)
    img_edge = cv2.adaptiveThreshold(img_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,7,1.5)
    img_edge = cv2.cvtColor(img_edge,cv2.COLOR_GRAY2BGR)
    img_preout = cv2.filter2D(img_pyr,-1,sharpener)
    img_preout = cv2.addWeighted(img_preout,0.6,img_pyr,0.4,10)
    img_cartoon = cv2.bitwise_and(img_preout,img_edge)
    return img_cartoon
    
video_feed = cv2.VideoCapture(0)

_thread.start_new_thread(start_capture,tuple([sketcher,video_feed,"sketcher"]))
#_thread.start_new_thread(start_capture,tuple([identity,video_feed,"standard"]))
_thread.start_new_thread(start_capture,tuple([cartoonate,video_feed,"cartoonify"]))


#video_feed.release()
