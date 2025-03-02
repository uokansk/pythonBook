import numpy as np
import cv2
import math
import socket
import pickle
import time

listX = [0] * 640

cap = cv2.VideoCapture(1)

ret, image = cap.read()
frameCopy = image.copy()
# cv2.imshow('win2', image)
frameCopy = frameCopy[0:480, 280:480]
cmap = cv2.cvtColor(frameCopy, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(cmap, 120, 255, cv2.THRESH_BINARY)
v = int(thresh1.shape[0])
d = int(thresh1.shape[1])
cv2.imshow("thresh1", thresh1)
r = 0

for y in range(0, v):
    flag = 0
    for x in range(50, d):
        fff = thresh1[y][x]
        if fff < 100 and flag == 0:
            x1 = x
            flag = 1

        if fff > 100 and flag == 1:
            x2 = x
            mid = int((x1 + x2) / 2)
            listX[y] = mid + 280
            cv2.circle(frameCopy, (listX[y], y), 3, (0, 0, 255), -1)
            break

cv2.imshow("frameCopy", frameCopy)

hsv_min = np.array((57, 57, 57), np.uint8)
hsv_max = np.array((255, 215, 255), np.uint8)

# hostAddress = '18:67:B0:82:F0:B3'
# channel = 4
# backlog = 1
# mySocket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
# mySocket.bind((hostAddress, channel))
# print("проверка работы клиента")
# mySocket.listen()
# print("соединение...")
# client, address = mySocket.accept()

while True:
    ret, img = cap.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv, hsv_min, hsv_max)
    # cv2.imshow('thresh', thresh)
    moments = cv2.moments(thresh, 1)
    dM01 = moments['m01']
    dM10 = moments['m10']
    dArea = moments['m00']
    err = 0
    y = 0
    if dArea > 10:
        x = int(dM10 / dArea)
        y = int(dM01 / dArea)
        cv2.circle(img, (x, y), 10, (0, 0, 255), -1)
        err = x - listX[y]
        cv2.putText(img, str(listX[y]), (40, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
        s = str(x) + ' ' + str(y) + ' ' + str(err)
        cv2.putText(img, s, (x + 20, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    for y in range(0, 640):
        cv2.circle(img, (listX[y], y), 4, (0, 0, 255), -1)

    cv2.imshow("img", img)
    # if y > 400:
    #     err = 5000
    #     break
    # a = int(input("вводите"))
    # dataToSend = err
    # bytesToSend = pickle.dumps(dataToSend)  # преобразование данных в байтовую систему для EV3
    # client.send(bytesToSend)  # отправка данных в модуль EV3
    if cv2.waitKey(1) == ord('q'):

        break
cap.release()
cv2.destroyAllWindows()
