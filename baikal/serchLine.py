import numpy as np
import cv2
import math
listX = []
line = [0] * 640
cap = cv2.VideoCapture(0)

ret, image = cap.read()
frameCopy = image.copy()
# cv2.imshow('win2', image)
cmap = cv2.cvtColor(frameCopy, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(cmap, 100, 255, cv2.THRESH_BINARY)
v = int(thresh1.shape[0])
d = int(thresh1.shape[1])
cv2.imshow("thresh1", thresh1)
r = 0

for y in range(0, v):
    flag = 0
    for x in range(50, d - 50):
        fff = thresh1[y][x]
        if fff < 50 and flag == 0:
            x1 = x
            flag = 1

        if fff > 50 and flag == 1:
            x2 = x
            line[y] = int((x1 + x2) / 2)
            listX.append(line[y])
            cv2.circle(frameCopy, (line[y], y), 3, (0, 0, 255), -1)

            break
cv2.imshow("frameCopy", frameCopy)

cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()

print(listX)
