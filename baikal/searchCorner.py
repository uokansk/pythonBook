import numpy as np
import cv2
import math

cap = cv2.VideoCapture(0)
x_tochka = 0
y_tochka = 0
x = 1
y = 1
while True:
    ch = cv2.waitKey(5)
    if ch == 27:
        break
    ret, image = cap.read()
    cv2.imshow('win2', image)
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow('win', hsv_img)

    hsv_min = np.array((5, 255, 24), np.uint8)
    hsv_max = np.array((255, 255, 61), np.uint8)
    hsv_msk = cv2.inRange(hsv_img, hsv_min, hsv_max)
    contours, hierarchy = cv2.findContours(hsv_msk, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    for icontour in contours:
        rect = cv2.minAreaRect(icontour)
        area = int(rect[1][0] * rect[1][1])
        x = int(rect[0][0])
        y = int(rect[0][1])
        X_catet = x_tochka - x
        Y_catet = y - y_tochka
        gipotenuza = int(math.sqrt((X_catet) ** 2 + (Y_catet) ** 2))
        angle = 180.0 / math.pi * math.acos(x / gipotenuza)
        cv2.putText(image, str(int(angle)), (40, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 0), 2)
        cv2.imshow('contours', image)
cap.release()
cv2.destroyAllWindows()
