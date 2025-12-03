# Gesture_Flow

This project implements a real-time Sign Language Recognition System using Python, OpenCV, and MediaPipe.
It captures live video from a webcam, detects hand gestures, and translates them into corresponding sign language characters (A–Z or a selected subset).
Recognized gestures are displayed directly on the video stream along with a subtle watermark crediting the creator: Made by Gurmeet Kaur.

## Features
- Real-time hand gesture detection using webcam
- Recognition of basic sign language gestures (A-Z or a subset)
- Display of recognized sign on the video feed
  
## Requirements
- Python 3.7+
- OpenCV
- Mediapipe (for hand tracking)
- Numpy

## How to Run
1. Install dependencies:
   ```bash
   pip install opencv-python mediapipe numpy
   ```
2. Run the main script:
   ```bash
   python main.py
   ```

## 📝 Notes

Best results occur with:
---

Plain background

Consistent lighting

Clear hand positioning

---
This is a foundational prototype.
---
You can enhance it by:
---

Adding a trained classifier

Supporting full-word recognition

Integrating TensorFlow Lite models

Adding dataset capture functionality

---
👤 Developer
---

Gurmeet Kaur
Cybersecurity & Technology Enthusiast
