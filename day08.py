from facial_emotion_recognition import EmotionRecognition
import cv2

er = EmotionRecognition(device='cpu')
cam = cv2.VideoCapture(0)

while True:
    success, frame = cam.read()
    if not success:
        break  # Break the loop if there's an issue with the camera input

    frame = er.recognise_emotion(frame, return_type='BGR')
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(10)
    if key == 27:  # Press 'Esc' to exit
        break

cam.release()
cv2.destroyAllWindows()
