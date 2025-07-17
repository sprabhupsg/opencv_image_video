import cv2
import time  


haar_cascade = 'C:\\opencv_image_video\\data\\cars_data\\cars.xml'
car_cascade = cv2.CascadeClassifier(haar_cascade)
if car_cascade.empty():
    raise Exception("Error loading Haar cascade file.")

video = 'C:\\opencv_image_video\\data\\car-video.mp4'

cap = cv2.VideoCapture(video)

if not cap.isOpened():
    raise Exception("Error opening video file.")

car_detected = False  
detection_time = None  

while cap.isOpened():
    ret, frames = cap.read()
    if not ret:
        break 

    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    
    if len(cars) > 0 and not car_detected:
        car_detected = True
        detection_time = time.time()
        print("Car detected!")

    if car_detected and time.time() - detection_time > 5:  
        break

    for (x, y, w, h) in cars:
        cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('video', frames)

    if cv2.waitKey(33) == 27: 
        break

cap.release()  
cv2.destroyAllWindows()