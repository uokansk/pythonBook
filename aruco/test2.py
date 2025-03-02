import cv2
import numpy as np
import cv2.aruco as aruco
import time

dict_mark = aruco.getPredefinedDictionary(aruco.DICT_5X5_1000)
param_mark = aruco.DetectorParameters
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    img = frame
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    marker_corners, marker_IDs, reject = aruco.detectMarkers(gray_frame, dict_mark)

    if marker_corners:
        for ids, corners in zip(marker_IDs, marker_corners):
            cv2.polylines(img, [corners.astype(np.int32)], True, (0, 255, 255), 4, cv2.LINE_AA)
            corners = corners.reshape(4, 2)
            corners = corners.astype(int)
            top_right = corners[0].ravel()
            cv2.putText(img, f"id: {ids[0]}", top_right, cv2.FONT_HERSHEY_PLAIN, 1.3, (0, 0, 255), 2, cv2.LINE_AA)

    # cv2.imshow('im', aruco.drawDetectedMarkers(img, marker_corners, marker_IDs, (0, 255, 255)))
    cv2.imshow('image', img)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
