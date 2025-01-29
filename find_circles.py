# Lisa Samoylov 01/28/25
# Dali Data Challenge 
# GOAL: Attempt to count the number of barnacles by creating a circle around them

# I am less sure of how this works, so I abondoned it for make_ellipses.py

import cv2 
import numpy as np 
  
# Read image. 
image = cv2.imread('Barnacles/mask2.png', cv2.IMREAD_COLOR) 

# IMAGE RESIZING 
#====================================
# Get screen resolution
screen_width = 1920  
screen_height = 1080  

# Calculate aspect ratio of the image
aspect_ratio = image.shape[1] / image.shape[0]

# Resize the image while maintaining aspect ratio
# !!! These settings were tinkered with so that it fit on a Dell Screen !!!
if screen_width / screen_height > aspect_ratio:
    new_width = int(screen_height * aspect_ratio)
    new_height = int(screen_height)

else:
    new_width = int(screen_width)
    new_height = int(screen_width / (aspect_ratio))

image = cv2.resize(image, (int(new_width/1.5), int(new_height/1.5)))

# ===========================================
  
# Convert to grayscale. 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
  
# Blur using 3 * 3 kernel. 
gray_blurred = cv2.blur(gray, (3, 3)) 
  
# Apply Hough transform on the blurred image. 
detected_circles = cv2.HoughCircles(gray_blurred,  
                   cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, 
               param2 = 30, minRadius = 1, maxRadius = 40) 
  
# Draw circles that are detected. 
if detected_circles is not None: 
  
    # Convert the circle parameters a, b and r to integers. 
    detected_circles = np.uint16(np.around(detected_circles)) 
  
    for pt in detected_circles[0, :]: 
        a, b, r = pt[0], pt[1], pt[2] 
  
        # Draw the circumference of the circle. 
        cv2.circle(image, (a, b), r, (0, 255, 0), 2) 
  
        # Draw a small circle (of radius 1) to show the center. 
        cv2.circle(image, (a, b), 1, (0, 0, 255), 3) 
        cv2.imshow("Detected Circle", image) 
        cv2.waitKey(0) 