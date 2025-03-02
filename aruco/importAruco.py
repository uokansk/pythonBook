import cv2
import numpy as np
import cv2.aruco as aruco

marker_size = 100
with open('camera_cal.npy', 'rb') as f:
    camera_matrix = np.load(f)
    camera_distortion = np.load(f)

aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_50)

# VideoCap = False

cap = cv2.VideoCapture(0)
camera_width = 640
camera_height = 480
camera_frame_rate = 40

ret, frame = cap.read()
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

corners, ids, rejected = aruco.detectMarkers(gray_frame, aruco_dict, camera_matrix, camera_distortion)

if ids is not None:
    aruco.drawDetectedMarkers(frame, corners)
    rvec, tvec, _objPoints = aruco.estimatePoseSingleMarkers(corners, marker_size, camera_matrix, camera_distortion)

    # for marcer in range(len(ids)):
    #     aruco.drawAxis()
cv2.imshow('frame', frame)
cv2.waitKey(0)


while True:
    ret, frame = cap.read()
    cv2.imshow("img", frame)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
