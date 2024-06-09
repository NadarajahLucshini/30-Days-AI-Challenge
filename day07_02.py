import cv2
import numpy as np
import os

haar_file = 'haarcascade_frontalface_default.xml'
datasets = 'datasets'

# Training phase
print('Training...')

# Initialize variables
(images, labels, names, id) = ([], [], {}, 0)

# Read the datasets
for (subdirs, dirs, files) in os.walk(datasets):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(datasets, subdir)
        for filename in os.listdir(subjectpath):
            path = os.path.join(subjectpath, filename)
            label = id
            images.append(cv2.imread(path, 0))
            labels.append(int(label))
        id += 1

# Define the size of the images
(width, height) = (130, 100)

# Convert lists to numpy arrays
(images, labels) = [np.array(lis) for lis in [images, labels]]

# Create a model and train it
model = cv2.face.FisherFaceRecognizer_create()
model.train(images, labels)

# Load the Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(haar_file)

# Initialize the webcam
webcam = cv2.VideoCapture(0)
cnt = 0

while True:
    # Read frame from webcam
    _, im = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))

        # Predict the face
        prediction = model.predict(face_resize)
        cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
        if prediction[1] < 800:
            cv2.putText(im, '%s - %.0f' % (names[prediction[0]], prediction[1]), (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            print(names[prediction[0]])
        else:
            cv2.putText(im, 'Unknown', (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('OpenCV', im)

    # Exit the loop when 'q' is pressed
    key = cv2.waitKey(10)
    if key == ord('q'):
        break

# Release the webcam and close windows
webcam.release()
cv2.destroyAllWindows()
