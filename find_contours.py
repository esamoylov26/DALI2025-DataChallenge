# Lisa Samoylov 01/28/25
# Dali Data Challenge 
# GOAL: Attempt to create the contours used in a mask 

# Does not work - it finds the contour of the WHOLE img and not the blue 
# Suspect lines 35-47 since that's where the contour is being created 

import cv2
import numpy as np

# Read the image
image = cv2.imread('Barnacles/mask1.png')
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

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours
for contour in contours:
    cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

# Show the image
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()