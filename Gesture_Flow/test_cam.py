import cv2

cap = cv2.VideoCapture(0)
print("Camera opened:", cap.isOpened())
cap.release()
