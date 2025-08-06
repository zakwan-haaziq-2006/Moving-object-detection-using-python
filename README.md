# Moving-object-detection
A python project for detecting moving objects in the frame by capturing the frame live


# 🚶‍♂️ Moving Object Detection using OpenCV

This Python project performs **real-time moving object detection** using your webcam feed. It uses OpenCV and imutils to track motion by comparing each video frame to a static reference frame.

---

## 📸 How It Works

1. Captures video using your webcam.
2. Converts each frame to grayscale and applies Gaussian blur to reduce noise.
3. The first captured frame is saved as the **reference**.
4. Every new frame is compared to this reference using **frame differencing**.
5. If any object moves (i.e., the frame differs), a bounding box is drawn around it.

---

## 🧠 Features

- Real-time motion detection
- Bounding boxes around detected movement
- Adjustable sensitivity using `area` threshold
- ESC key to exit the program

---

## 🛠 Requirements

Install dependencies using the provided `requirement.txt`:

```bash
pip install -r requirement.txt
