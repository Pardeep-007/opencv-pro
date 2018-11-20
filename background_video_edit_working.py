import cv2
import numpy as np
cap = cv2.VideoCapture(1)
vid= cv2.VideoCapture('D:/anim.mp4')
panel = np.zeros([100, 200], np.uint8)
cv2.namedWindow('panel')
def nothing(x):
    pass
cv2.createTrackbar('Low - R', 'panel', 32, 255, nothing)
cv2.createTrackbar('Low - G', 'panel', 28, 255, nothing)
cv2.createTrackbar('Low - B', 'panel', 255, 255, nothing)


cv2.createTrackbar('High - R', 'panel', 76, 255, nothing)
cv2.createTrackbar('High - G', 'panel', 255, 255, nothing)
cv2.createTrackbar('High - B', 'panel', 255, 255, nothing)


while True:
    _, iframe = cap.read()
    frame=cv2.resize(iframe, (1180, 686))
    r, ivid_frame= vid.read()
    vid_frame=cv2.resize(ivid_frame, (1180, 686))


    roi = frame

    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    lr = cv2.getTrackbarPos('Low - R', 'panel')
    lg = cv2.getTrackbarPos('Low - G', 'panel')
    lb = cv2.getTrackbarPos('LOW - B', 'panel')
    hr = cv2.getTrackbarPos('High - R', 'panel')
    hg = cv2.getTrackbarPos('High - G', 'panel')
    hb = cv2.getTrackbarPos('High - B', 'panel')

    lower_green = np.array([lr, lg, lb])
    upper_green = np.array([hr, hg, hb])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    mask_inv = cv2.bitwise_not(mask)

    bg = cv2.bitwise_and(roi, vid_frame, mask=mask)
    grm = cv2.bitwise_and(roi,roi, mask=mask_inv)
    fg = cv2.bitwise_and(vid_frame, roi, mask=mask_inv)
    tryy= cv2.bitwise_or(vid_frame,vid_frame,mask=mask)
    new_try= cv2.bitwise_or(tryy,grm)



    cv2.imshow('plzz b',new_try)




    #cv2.imshow('medium',nmed)



    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()