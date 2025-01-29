# DALI2025-DataChallenge
--------------------------
Data challenge submission for the Barnacles Data Team Application. 

# Brainstorm an idea for a system that can help the scientists get their work done faster. 
The scientists already seem to have a system in place to count the barnacles: Take a photo and then count them by hand. At a glance, the slowest part is manually counting the barnacles. One way to speed up the scientists' process would be to get a computer to help them count the barnacles. 

Hypothetically/Vaguelt 
I) (Potentially) do some image preprocessing to make it easier for a computer to work with the image 
II) Run a computer process on the image to identify (and count) the barnacles
III) Have the computer output an image or other graphic to make the count readable/usable by the scientists.

# Identify one or more critical subtasks that are necessary to solving the task. Define these tasks clearly by thinking about what information each one will receive and what outputs they are responsible for providing. 
I) Image preprocessing: Given a raw-photo that a scientist took on site, process the photo by adding colors, contours, etc. that'd be helpful for a computer and return the altered photo 
--> !!! When you process the image, make sure that the process is accurate for II)'s needs

II) Process to count the barnacles: Given the processed photo from I) run a process that counts the barnacles i.e. returns an integer. 
--> !!! The process in I) depends on how you plan to count the barnacles. 

E.G. 
Count the barnacles by 
i) Coloring the barnacles red (Preprocessing)
ii) Count the number of red pixels in total (TOTAL_RED)
iii) Estimate the average number of (red) pixels a barnacle takes up (AVG_BARN)
iv) compute TOTAL_RED/AVG_BARN to estimate the number of barnacles in the photo 


III) Test the process to count the barnacles. 

# Pick a subtask that you are interested in working on, and think about how you can evaluate performance on it. What metrics do you care about, and is it practical for you to compute them with just the data we’ve provided for you?
I'm interested in the automation process. One easy way to evaluate it's performance is to take the process on II) against the images where the scientists know the number of barnacles for. In this case, it'd be image1 and image2. 

- (The process could also be checked against a portion of the image to check for places it could go wrong - E.g. Take a portion of image1 that's more barnacle-dense or where the barnacles are deeper in the rock- and run the test on that. The only caveat is that the scientists might not know the _exact_ count for the barnacles in a portion of the image)

- With the masks that have been given, I'd say it's possible to compute said metrics. I don't know if counting the barnacles individually is the most practical. Another way would be to estimate the total area in the images that the barnacles take up and divide that estimate by the estimated area that a singular barnacle takes up. (I did not implement this though).

# Build a prototype which attempts to do your identified subtask
See the other files in the folder. 

# Make some conclusions! If you built some type of automation prototype, is your approach worth pursuing? What might work better? If you build a visualization, what does your prototype tell you?

# Tell us about your learning process. As stated, one of the main points of this application process is for you to learn new things. What is something you learned that excited you?

I opened ChatGPT to help me navigate OpenCV and help me write some of the code. Then I just messed around with the parameters to see what worked and didn't quite work. 
It was a lot of fun messing around with OpenCV and playing around with their methods and parameters to identify contours (E.g. SimpleBlobDetector to detect the blue masks, GridSearch to identify the range of parameters that SimpleBlobDetector would work on, etc.) 
