import cv2
import numpy as np
import cv2.aruco as aruco

cap = cv2.VideoCapture(0)


# def findAruco(img, marker_size=5, total_markers=1000, draw=True):
#     gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#     key = getattr(aruco, f'DICT_{marker_size}X{marker_size}_{total_markers}')
#     arucoDict = aruco.Dictionary
#     arucoParam = aruco.DetectorParameters
#     bbox, ids, _ = aruco.detectMarkers(gray, arucoDict, parameters=arucoParam)
#     print(ids)


while True:
    ret, frame = cap.read()
    cv2.imshow("img", frame)
    # findAruco(frame)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
