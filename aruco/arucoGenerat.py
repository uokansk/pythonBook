import cv2 as cv
import numpy as np
import argparse
import sys

# Загрузить предопределенный словарь
dictionary = cv.aruco.DICT_6X6_50

# Сгенерировать маркер
markerImage = np.zeros((200, 200), dtype=np.uint8)
markerImage = cv.aruco.drawMarker(dictionary, 33, 200, markerImage, 1)
ddd = cv.aruco.dr
cv.imwrite("marker33.png", markerImage)
