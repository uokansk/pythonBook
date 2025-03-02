import cv2
import time
import numpy as np
SIZE = (640, 360)
img1 = cv2.imread("image.jpg")
img1 = img1+50

# img2 = img1.copy()
img2 = cv2.resize(img1.copy(), SIZE)

img2 = img2.astype(np.float64)
# увеличиваем значение всех элементов на 50
img2 += 50
# все элементы, которые больше 255, делаем равными 255
# все элементы, которые меньше 0, делаем равными 0
img2 = np.clip (img2 , 0, 255)
# меняем тип массива на исходный - uint8
img2 = img2.astype(np.uint8)
# выводим изображение на экран
cv2.imshow("ttt", img2)
# выводим уменьшенный оригинал для сравнения
# cv2.imshow(cv2.resize(img1.copy(), SIZE))
k = cv2.waitKey(0)

