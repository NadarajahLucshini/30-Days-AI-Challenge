

import cv2


alg = "haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(alg)


if haar_cascade.empty():
    print("Error loading cascade file. Check the file path.")
else:
    cam = cv2.VideoCapture(0)

    while True:
        _, img = cam.read()
        grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face = haar_cascade.detectMultiScale(grayImg, 1.3, 4)

        for (x, y, w, h) in face:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

        cv2.imshow("facedetection", img)

        key = cv2.waitKey(10)
        if key == 27:  # Press 'Esc' to exit
            break

    cam.release()
    cv2.destroyAllWindows()

    