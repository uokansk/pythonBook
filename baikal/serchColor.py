import cv2
import numpy as np

# if __name__ == '__main__':
#     def callback(*arg):
#         pass
# cv2.namedWindow('result')

cap = cv2.VideoCapture(0)
# hsv_min = np.array((0, 75, 95), np.uint8)
# hsv_max = np.array((215, 255, 255), np.uint8)
while True:
    ret, img = cap.read()
    cv2.imshow("img", img)
    img= img[0:480, 250:480]
    cv2.imshow("img1", img)
    # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # thresh = cv2.inRange(hsv, hsv_min, hsv_max)
    # cv2.imshow('thresh',thresh)
    # moments = cv2.moments(thresh, 1)
    # dM01 = moments['m01']
    # dM10 = moments['m10']
    # dArea = moments['m00']
    # if dArea > 100:
    #     x = int(dM10 / dArea)
    #     y = int(dM01 / dArea)
    #     cv2.circle(img, (x, y), 10, (0, 0, 255), -1)
    #
    # cv2.imshow('result', img)
    ch = cv2.waitKey(5)
    if ch == 27:
        break
cap.release()
cv2.destroyAllWindows()
