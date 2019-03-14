"""
This is an exercise to capture video, but it's from the computer camera and not the Vector camera
"""

import cv2, time
import numpy as np

#1. Create an object. Zero for external camera
cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# Define the codec and create VideoWriter object
#fourcc = cv2.cv.CV_FOURCC(*'DIVX')
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
out = cv2.VideoWriter('output.avi', -1, 20.0, (640,480))
"""
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,180)

        writer = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*"MJPG"), 30,(640,480))

        for frame in range(1000):
            writer.write(out)

        writer.release()
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

"""

a = 0
while True:
  a = a+ 1
  #3. Create a frame object
  check, frame = cap.read()

  print(check)
  print(frame) # representing image

  #4. Show the frame
  cv2.imshow("Capturing", frame)
  #cap.write(frame)


  #5. For press any key to out (miliseconds)
  #cv2.waitKey(0)

  #6. For playing
  key=cv2.waitKey(1)

  if key == ord('q'):
    break

print(a)

#2. Shutdown the camera
out.release()
cap.release()
cv2.destroyAllWindows