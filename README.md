# 30-Days-AI-Challenge
Basic code of AI developing

# day03

## Webcam Video Stream with OpenCV

This script captures video from the webcam and displays it in a window using OpenCV. The video stream continues until the user presses the 'c' key to stop the program.

  ### Prerequisites

- Python 3.x
- OpenCV library (`opencv-python`)

  ### Installation

To install OpenCV, you can use pip:

```bash
pip install opencv-python
```
# day04

## Simple Motion Detection using Webcam

This Python script detects motion in a video stream captured from the webcam. It uses OpenCV and imutils libraries to perform motion detection.

### Prerequisites

- Python 3.x
- OpenCV (`opencv-python`)
- Imutils (`imutils`)

### Installation

You can install the required libraries via pip:

```bash
pip install opencv-python imutils
```

### Script Details

The script performs the following steps:

1. **Initialize Video Capture:**
   It initializes the video capture object to capture frames from the webcam.

2. **Initialize the First Frame:**
   It initializes the first frame in the video stream to compare subsequent frames for motion detection.

3. **Define Minimum Area for Motion Detection:**
   A minimum area is defined to filter out small changes and noise in the video stream.

4. **Motion Detection Loop:**
   The script enters an infinite loop where it captures frames from the webcam and detects motion.
   - It resizes each frame, converts it to grayscale, and applies Gaussian blur to reduce noise.
   - It computes the absolute difference between the current frame and the first frame.
   - Thresholding and dilation operations are applied to obtain a binary image highlighting areas with motion.
   - Contours are detected on the thresholded image, and if the contour area exceeds the defined minimum area, a bounding box is drawn around the detected motion area.
   - Text indicating the room status ("Normal" or "Motion Detected") is displayed on the frame.
   - The frame is displayed in a window named "Security Feed".

5. **Break the Loop:**
   If the user presses the 'c' key, the loop breaks, and the program exits.

# day05

## Real-Time Face Detection using Haar Cascades

This Python script detects faces in real-time from the video stream captured by a webcam. It utilizes OpenCV's Haar Cascade classifier for face detection.

### Prerequisites

- Python 3.x
- OpenCV (`opencv-python`)

### Installation

You can install the required libraries via pip:

```bash
pip install opencv-python
```

### Script Details

The script performs the following steps:

1. **Load Haar Cascade Classifier:**
   It loads the Haar Cascade classifier for frontal face detection.

2. **Video Capture Initialization:**
   The script initializes the video capture object to capture frames from the webcam.

3. **Face Detection Loop:**
   It enters an infinite loop where it continuously reads frames from the webcam and detects faces.
   - Each frame is converted to grayscale for face detection.
   - The `detectMultiScale` function of the Haar Cascade classifier is used to detect faces in the grayscale frame.
   - Detected faces are outlined with rectangles drawn on the original color frame.
   - The frame with face rectangles is displayed in a window named "facedetection".

4. **Exit Condition:**
   If the user presses the 'Esc' key, the loop breaks, and the program exits.

# day06

## Real-Time Object Tracking using Color Detection

This Python script tracks objects in real-time from the video stream captured by a webcam. It detects objects of a specific color range using color segmentation and tracks their movement.

### Prerequisites

- Python 3.x
- OpenCV (`opencv-python`)
- Imutils (`imutils`)

### Installation

You can install the required libraries via pip:

```bash
pip install opencv-python imutils
```

### Script Details

The script performs the following steps:

1. **Define Color Range:**
   It defines the lower and upper bounds of the color range to be tracked in HSV color space.

2. **Video Capture Initialization:**
   The script initializes the video capture object to capture frames from the webcam.

3. **Object Tracking Loop:**
   It enters an infinite loop where it continuously reads frames from the webcam and tracks objects.
   - Each frame is resized and blurred to reduce noise.
   - The frame is converted from BGR to HSV color space for color segmentation.
   - A mask is created by thresholding the HSV frame to isolate the color range.
   - Morphological operations (erosion and dilation) are applied to the mask to remove noise.
   - Contours are detected on the mask to identify the objects.
   - The largest contour is chosen as the object of interest, and its position and size are determined.
   - Based on the position and size of the object, its movement direction (front, left, right, or stop) is determined and printed.

4. **Exit Condition:**
   If the user presses the 'q' key, the loop breaks, and the program exits.




