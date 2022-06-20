# pip install opencv-python
import cv2

img_capture = cv2.VideoCapture(0)
result = True

while result:
    ret, frame = img_capture.read()
    cv2.imwrite("outputs\webcamoutput.jpg", frame)
    result = False
    print("Image Captured")

img_capture.release()
