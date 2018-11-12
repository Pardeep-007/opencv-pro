import cv2
import numpy as np

cam=cv2.VideoCapture(0)
vid=cv2.VideoCapture('D:/videoplayback.mp4')
obj=cv2.createBackgroundSubtractorMOG2()
while True:

    _,frame=cam.read()
    i,v_f=vid.read()
    bg= obj.apply(frame)
    #f = cv2.bitwise_and(frame,frame, mask=bg)

    #nit=cv2.resize(g,(1366,768))
    sp_r=cv2.resize(v_f, (1366,768))
    f_rr=cv2.resize(bg,(1366,768))
    g= cv2.bitwise_or(sp_r,sp_r,mask=f_rr)
    cv2.imshow('sp',bg)
    cv2.imshow('may_BE',g)
    #cv2.imshow('black_bg',f_rr)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()

