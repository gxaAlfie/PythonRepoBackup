# Color Range in HSV => Range of Color [Blue, Green, Red]
# formula for lower: [H - 10, 100, 100]
# formula for upper: [H + 10, 255, 255]

# Blue Color HSV: [120,255,255]
# Green Color HSV: [60,255,255]
# Red Color HSV: [0,255,255]

# HSV Range (OpenCV) => H: 0 - 179, S: 0 - 255, V: 0 - 255

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    blue = np.uint8([[[ 255, 0, 0 ]]])
    hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([110,100,100])
    upper_blue = np.array([130,255,255])

    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # define range of green color in HSV
    green = np.uint8([[[ 0, 255, 0 ]]])
    hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)

    lower_green = np.array([50,100,100])
    upper_green = np.array([70,255,255])

    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    # define range of red color in HSV
    red = np.uint8([[[ 0, 0, 255 ]]])
    hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)

    lower_red = np.array([-10,100,100])
    upper_red = np.array([10,255,255])

    red_mask = cv2.inRange(hsv, lower_red, upper_red)

    blue_green_mask = cv2.bitwise_or(blue_mask, green_mask)
    bgr_mask = cv2.bitwise_or(blue_green_mask, red_mask)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask = bgr_mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',bgr_mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
