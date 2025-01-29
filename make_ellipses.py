# Lisa Samoylov 01/28/25
# Dali Data Challenge 
# GOAL: Attempt to count the number of barnacles by counting each of the blobs in a mask

import cv2 
import numpy as np 

# Example from https://www.geeksforgeeks.org/find-circles-and-ellipses-in-an-image-using-opencv-python/
# OpenCV help from Google Gemini & GeeksForGeeks

# LOADING IMAGE
#====================================
image = cv2.imread('Barnacles/mask2.png', 0) 

# IMAGE RESIZING 
#====================================
# Get screen resolution
screen_width = 1920  
screen_height = 1080  

# Calculate aspect ratio of the image
aspect_ratio = image.shape[1] / image.shape[0]

# Resize the image while maintaining aspect ratio
# !!! Tinker with these so the img fit your screen !!!
if screen_width / screen_height > aspect_ratio:
    new_width = int(screen_height * aspect_ratio)
    new_height = int(screen_height)

else:
    new_width = int(screen_width)
    new_height = int(screen_width / (aspect_ratio))

image = cv2.resize(image, (int(new_width/1.5), int(new_height/1.5)))

# SETTING UP FILTER 
# ===========================================
# Initialize parameter setting using cv2.SimpleBlobDetector 
params = cv2.SimpleBlobDetector_Params() 

# Set Area filtering parameters 
params.filterByArea = True
params.minArea = 100

# Set Circularity filtering parameters 
params.filterByCircularity = True
params.minCircularity = 0.2

# Set Convexity filtering parameters 
params.filterByConvexity = True
params.minConvexity = 0.2
	
# Set inertia filtering parameters 
params.filterByInertia = True
params.minInertiaRatio = 0.01


# Create a detector with the parameters 
detector = cv2.SimpleBlobDetector_create(params) 
	
# Detect blobs 
keypoints = detector.detect(image) 

# Draw blobs on our image as red circles 
blank = np.zeros((1, 1)) 
blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 0, 255), 
						cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) 

number_of_blobs = len(keypoints) 

# PARAMETER WRITING 
# ===================================
text = ["Number of Circular Blobs: " + str(len(keypoints)),
        "Min Area: " + str(round(params.minArea,2)), 
        "Min Circularity: " + str(round(params.minCircularity,2)), 
        "Min Convexity: " + str(round(params.minConvexity,2)), 
        "Min Inertia Ratio: " + str(round(params.minInertiaRatio,2))]

print(round(params.minArea,2),round(params.minCircularity,2), round(params.minConvexity,2), round(params.minInertiaRatio,2))

# Initial y-coordinate
x, y = 50, 50  # Starting position

# Line spacing
line_spacing = 40

# Add each line to the image
for line in text:
    cv2.putText(blobs, line, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 100, 255), 2)
    y += line_spacing  # Move to next line

# Show blobs 
cv2.imshow("Filtering Circular Blobs Only", blobs) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 

# Saving the image to an output folder  
name = "" + str(round(params.minArea,2)) + "_" + str(round(params.minCircularity,2))+ "_" + str(round(params.minConvexity,2))+ "_" + str(round(params.minInertiaRatio,2))
name = name + ".jpg" 
cv2.imwrite('output_imgs/' + name, blobs) 
# cv2.imwrite('output_imgs/saved_image.jpg', blobs) 

# grid_search.py
# Best Parameters: {'minThreshold': 10, 'maxThreshold': 300, 'minArea': 30, 'maxArea': 5000, 'minCircularity': 0.1, 'minConvexity': 0.5, 'minInertiaRatio': 0.01}