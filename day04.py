import cv2
import imutils

# Initialize the video capture
vs = cv2.VideoCapture(0)

# Initialize the first frame in the video stream
firstFrame = None

# Define the minimum area for motion detection
area = 500

while True:
    # Capture frame-by-frame
    ret, img = vs.read()
    
    # Check if the frame is read correctly
    if not ret:
        print("Error: Failed to capture image.")
        break
    
    # Initialize the text for room status
    text = "Normal"
    
    # Resize the frame, convert it to grayscale, and blur it
    img = imutils.resize(img, width=1000)
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0)
    
    # If the first frame is None, initialize it
    if firstFrame is None:
        firstFrame = gaussianImg
        continue
    
    # Compute the absolute difference between the current frame and first frame
    imgDiff = cv2.absdiff(firstFrame, gaussianImg)
    threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]
    threshImg = cv2.dilate(threshImg, None, iterations=2)
    
    # Find contours on the thresholded image
    cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    
    # Loop over the contours
    for c in cnts:
        if cv2.contourArea(c) < area:
            continue
        # Compute the bounding box for the contour, draw it on the frame, and update the text
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Motion Detected"
        
    # Draw the text and timestamp on the frame
    cv2.putText(img, "Room Status: {}".format(text), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(img, "Press 'c' to close", (10, img.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    
    # Show the frame
    cv2.imshow("Security Feed", img)
    key = cv2.waitKey(1) & 0xFF
    
    # If the `c` key is pressed, break from the loop
    if key == ord("c"):
        break


vs.release()
cv2.destroyAllWindows()

