import cv2

vid = cv2.VideoCapture(0)
print('cam1')
while True:
    if cv2.waitKey(10) == 27:
        break
    ret, img = vid.read()
    v = int(img.shape[0] * 0.5)
    d = int(img.shape[1] * 0.5)
    img = cv2.resize(img, (d, v))

    cv2.rectangle(img, (140, 100), (180, 140), (0, 255, 255),
                  3)  # (140, 100) x y левого верхнего угла, (180,140) x y правого нижнего угла
    k = 0
    for x in range(140, 180):
        for y in range(100, 140):
            b, g, r = img[y][x]
            if b < 50 and g < 50 and r > 100:
                img[y, x] = (255, 255, 0)
                k += 1

    cv2.putText(img, str(k), (162, 120), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
    cv2.imshow('colorpic', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
