import cv2
vs = cv2.VideoCapture(0)

while True:
    _,img = vs.read()
    cv2.imshow("VideoStrem",img)
    key = cv2.waitKey(1)
    print(key)

    if key == ord("c"):
        break

vs.release()
cv2.destroyAllWindows()
