import cv2
import numpy as np
from sklearn.cluster import KMeans

def calculate_hsv_range(hsv_values):
    if len(hsv_values) > 0:
        lower_hsv = np.min(hsv_values, axis=0)
        upper_hsv = np.max(hsv_values, axis=0)
        return lower_hsv, upper_hsv
    else:
        return None, None

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    if not ret:
        break

    # Resize frame
    frame = cv2.resize(frame, (640, 480))

    # Convert the image to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Reshape the frame to be a list of pixels
    pixels = hsv_frame.reshape((-1, 3))

    # Perform k-means clustering to find the dominant color
    kmeans = KMeans(n_clusters=1)
    kmeans.fit(pixels)
    dominant_hsv = kmeans.cluster_centers_.astype(int)

    # Define the range for the dominant color
    hsv_values = hsv_frame.reshape(-1, 3)
    lower_hsv, upper_hsv = calculate_hsv_range(hsv_values)

    if lower_hsv is not None and upper_hsv is not None:
        print(f'Dominant HSV: {dominant_hsv}')
        print(f'Lower HSV: {lower_hsv}')
        print(f'Upper HSV: {upper_hsv}')

    # Create a mask based on the dominant color range
    mask = cv2.inRange(hsv_frame, lower_hsv, upper_hsv)
    
    # Find contours of the object
    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    if len(cnts) > 0:
        # Assume the largest contour is the object
        c = max(cnts, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        
        # Draw a rectangle around the detected object
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Frame', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
