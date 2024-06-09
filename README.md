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

# day07
Certainly! Below is a README file that provides instructions and explanations for your face dataset creation script using OpenCV.

---

## Face Dataset Creation Script

This script captures images from a webcam, detects faces using a Haar Cascade Classifier, and saves the detected faces into a specified directory. This can be used to create a dataset for training face recognition models.

### Requirements

- Python 3.x
- OpenCV library (`opencv-python`)
- Haar Cascade XML file (`haarcascade_frontalface_default.xml`)

## Installation

1. Ensure you have Python 3.x installed. If not, download and install it from [python.org](https://www.python.org/downloads/).

2. Install the OpenCV library using pip:

   ```bash
   pip install opencv-python
   ```

3. Download the Haar Cascade XML file from [OpenCV GitHub repository](https://github.com/opencv/opencv/tree/master/data/haarcascades) and save it as `haarcascade_frontalface_default.xml` in your working directory.

### Usage

1. Place the `haarcascade_frontalface_default.xml` file in the same directory as your script.

2. Run the script:

   ```bash
   python face_dataset.py
   ```

3. Enter the name of the subdirectory where you want to save the captured face images when prompted.

4. The script will start the webcam and begin capturing images. It will detect faces in the webcam feed, draw rectangles around detected faces, and save the face images in the specified subdirectory.

5. The script will save 50 face images by default. You can stop the script early by pressing the "q" key.

### Script Explanation

- **Input Prompt**: The script prompts you to enter a name for the subdirectory where the face images will be saved.

- **Directory Creation**: The script creates a directory named `datasets` if it doesn't already exist, and within that directory, it creates a subdirectory with the name you provided.

- **Face Detection and Saving**:
  - The script initializes the Haar Cascade face detector.
  - It captures frames from the webcam.
  - Converts each frame to grayscale (since the face detector works on grayscale images).
  - Detects faces in the frame.
  - For each detected face, it draws a rectangle around it, resizes the face image to 130x100 pixels, and saves it in the specified subdirectory.
  - The script captures and saves 50 images by default.

- **Stopping the Script**: The script runs in a loop and can be stopped by pressing the "q" key.

### Example Output

The captured images will be saved in the following structure:

```
datasets/
└── sub_data_name/
    ├── 1.png
    ├── 2.png
    ├── 3.png
    ├── ...
    └── 50.png
```

Each image is a grayscale face image of size 130x100 pixels.

Here's the updated README file that includes the necessary steps and explanations for running your face recognition script:

---
## day07_02
## Face Recognition Script

This script captures images from a webcam, detects faces using a Haar Cascade Classifier, and recognizes faces using a trained FisherFaceRecognizer model. This can be used for creating a face recognition system.

### Requirements

- Python 3.x
- OpenCV library (`opencv-contrib-python`)
- Haar Cascade XML file (`haarcascade_frontalface_default.xml`)

### Installation

1. Ensure you have Python 3.x installed. If not, download and install it from [python.org](https://www.python.org/downloads/).

2. Install the required OpenCV library using pip:

   ```bash
   pip install opencv-contrib-python
   ```

3. Download the Haar Cascade XML file from [OpenCV GitHub repository](https://github.com/opencv/opencv/tree/master/data/haarcascades) and save it as `haarcascade_frontalface_default.xml` in your working directory.

### Dataset Preparation

1. Create a directory named `datasets` in your working directory.

2. Within the `datasets` directory, create subdirectories for each person you want to recognize. Name each subdirectory after the person (e.g., `person1`, `person2`, etc.).

3. Collect face images of each person and save them in their respective subdirectories. Ensure the images are grayscale and have good lighting.

### Usage

1. Ensure the `haarcascade_frontalface_default.xml` file is in the same directory as your script.

2. Run the script:

   ```bash
   python face_recognition.py
   ```

3. The script will start by training the model with the images in the `datasets` directory. It will then initialize the webcam and begin capturing frames for face detection and recognition.

4. The script will display the webcam feed with detected faces and recognized names. Press the "q" key to exit the webcam feed.

### Script Explanation

- **Training Phase**:
  - The script initializes variables to store images, labels, names, and IDs.
  - It traverses the `datasets` directory, reading images and assigning labels to each person's images.
  - The images and labels are converted to numpy arrays.
  - The script creates a FisherFaceRecognizer model and trains it with the images and labels.

- **Face Detection and Recognition**:
  - Loads the Haar Cascade classifier for face detection.
  - Initializes the webcam and enters a loop to continuously read frames from the webcam.
  - Converts each frame to grayscale and detects faces.
  - For each detected face, resizes it to the required dimensions and predicts the identity using the trained model.
  - Draws rectangles around detected faces and displays the name and confidence level if the prediction confidence is below a threshold (800 in this case), otherwise labels it as "Unknown".
  - Displays the frame with annotations in a window.
  - Exits the loop when the 'q' key is pressed.

- **Cleanup**: Releases the webcam and closes all OpenCV windows when the loop exits.




