import cv2
import numpy as np
import winsound
import os

# Capturing frames
cap = cv2.VideoCapture(0)
while True:

    # Reading the captured frames-> frame1, frame2
    ret,frame1 = cap.read()
    ret,frame2 = cap.read()

    # Checking Difference in motion in 2 frames
    diff_frame = cv2.absdiff(frame1,frame2)

    # Converting BGR-> Gray and making frame blur
    gray = cv2.cvtColor(diff_frame,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    _,thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)

    # Dilating the frame to make get uniform contour
    dilated = cv2.dilate(thresh,None,iterations=100)

    # Finding the contours in the difference to get coordinates of motion 
    contour,x = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
 # print(" the number of contours", contour)
    for c in contour:

        # If the contourArea < 1000 ignore the frame
#Contour area is the amount of area the particular contour or the shape
#it is taking in the image, and it returns a floating type with a number
#of pixels in the contour.
        if cv2.contourArea(c) < 1000:
            continue

        # Drawing rectangle around the moving object
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,255),6)
        cv2.imshow("The Frame",frame1)


    # Press 'q' to exit the frame
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
