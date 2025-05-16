# 🔺 Shape Detection with OpenCV

A simple Python program that detects basic geometric shapes (Triangle, Square, Rectangle, Pentagon, Circle) from an image or live webcam feed using OpenCV.

## 🧠 Features

- Detects and labels shapes in images: Triangle, Square, Rectangle, Pentagon, and Circle.
- Filters out noisy or small contours to reduce false detections.
- Can process either a static image or a live video feed.
- Uses contour approximation and aspect ratio to distinguish between rectangles and squares.

## 📸 Example

### ![Example](test.png)
The program reads an image and detects shapes like:

![Example](output.png)

### Output (Labeled Shapes)
Contours are drawn and shapes are labeled on the image.

## 🧾 Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy

Install dependencies with:

```bash
pip install opencv-python numpy
```

🧠 How It Works

- Converts the image to grayscale.
- Applies Gaussian Blur to reduce noise.
- Uses Canny edge detection to find edges.
- Finds contours in the image.
- Approximates contours to polygons.
- Classifies shapes based on:
    Number of polygon vertices
    Aspect ratio (for rectangles vs squares)
Draws contours and labels the detected shapes.
