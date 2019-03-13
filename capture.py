"""
This is an exercise to capture video, but it's from the computer camera and not the Vector camera
"""

import cv2, time

#1. Create an object. Zero for external camera
video = cv2.VideoCapture(2)

a = 0
while True:
  a = a+ 1

  #3. Create a frame object
  check, frame = video.read()

  print(check)
  print(frame) # representing image

  #4. Show the frame
  cv2.imshow("Capturing", frame)


  #5. For press any key to out (miliseconds)
  #cv2.waitKey(0)

  #6. For playing
  key=cv2.waitKey(1)

  if key == ord('q'):
    break

print(a)
#2. Shutdown the camera
video.release()

cv2.destroyAllWindows