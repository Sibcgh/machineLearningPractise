import cv2
import numpy as np


def nothing(x):
    pass


cv2.namedWindow("Tracking")
cv2.createTrackbar("L H", "Tracking", 0, 255, nothing)
cv2.createTrackbar("L S", "Tracking", 0, 255, nothing)
cv2.createTrackbar("L V", "Tracking", 0, 255, nothing)
cv2.createTrackbar("U H", "Tracking", 255, 255, nothing)
cv2.createTrackbar("U S", "Tracking", 255, 255, nothing)
cv2.createTrackbar("U V", "Tracking", 255, 255, nothing)

while True:
    frame = cv2.imread('smarties.png')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # cv2 -> hsv conversion

    l_h = cv2.getTrackbarPos("L H", "Tracking")
    l_s = cv2.getTrackbarPos("L S", "Tracking")
    l_v = cv2.getTrackbarPos("L V", "Tracking")

    u_h = cv2.getTrackbarPos("U H", "Tracking")
    u_s = cv2.getTrackbarPos("U S", "Tracking")
    u_v = cv2.getTrackbarPos("U V", "Tracking")



    l_b = np.array([l_h,l_s,l_v]) # Lower colour range of blue 
    u_b = np.array([u_h, u_s, u_v])

    maskedVal = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask=maskedVal)

    cv2.imshow("frame",frame)
    cv2.imshow("maskedVal", maskedVal)
    cv2.imshow("res",res)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
