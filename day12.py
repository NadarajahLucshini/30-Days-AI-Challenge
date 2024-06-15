import numpy as np
import imutils
import cv2
import time
import os

# File paths (ensure these files are in the correct path)
prototxt = "MobileNetSSD_deploy.prototxt"
model = "MobileNetSSD_deploy.caffemodel"

# Check if model files exist
if not os.path.isfile(prototxt):
    print(f"Error: '{prototxt}' file not found")
    exit()
if not os.path.isfile(model):
    print(f"Error: '{model}' file not found")
    exit()

# Confidence threshold
confThresh = 0.2

# Classes and colors
CLASSES = ["background", "car", "bicycle"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

print("Loading model...")

# Load the Caffe model
try:
    net = cv2.dnn.readNetFromCaffe(prototxt, model)
except cv2.error as e:
    print(f"Error loading model: {e}")
    exit()

print("Model Loaded")
print("Starting Camera Feed")

# Initialize video stream
vs = cv2.VideoCapture(0)
time.sleep(2.0)

while True:
    # Read the next frame from the video stream
    ret, frame = vs.read()
    if not ret:
        break

    # Resize the frame to have a width of 1000 pixels
    frame = imutils.resize(frame, width=1000)
    (h, w) = frame.shape[:2]

    # Resize frame to 300x300 pixels and create a blob
    imResizeBlob = cv2.resize(frame, (300, 300))
    blob = cv2.dnn.blobFromImage(imResizeBlob, 0.007843, (300, 300), 127.5)

    # Set the blob as input to the network
    net.setInput(blob)
    
    try:
        detections = net.forward()
    except cv2.error as e:
        print(f"Error during forward pass: {e}")
        break

    # Loop over the detections
    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        # Filter out weak detections
        if confidence > confThresh:
            idx = int(detections[0, 0, i, 1])
            class_name = CLASSES[idx]

            # Display the class name and confidence
            label = "{}: {:.2f}%".format(class_name, confidence * 100)
            print("Object:", label)

            # Draw bounding box and label on the frame
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # Draw the prediction on the frame
            cv2.rectangle(frame, (startX, startY), (endX, endY), COLORS[idx], 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(frame, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)

   
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(10)
    if key == ord("q"):
        break


vs.release()
cv2.destroyAllWindows()
