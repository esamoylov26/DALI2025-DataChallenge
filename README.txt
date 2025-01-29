Identify barnacles by counting the masks 

========================
This process is an attempt to automate the barnacle counting (II) 

ASSUME GIVEN: mask with barnacle contours (so, raw image --> contours --> mask) 
GOAL: Count the number of contours (blobs) 

IDEA: 
- make_ellipses.py can successfully identify some blobs in the mask contours 
0) tinker with the parameters in make_ellipses to identify the tiniest blobs (and count them) 
1) tinker with the parameters again in make_ellipses to identify the larger blobs (and count them) 
2) keep tinkering with parameters to identify even larger blobs (and count them) until all blobs counted for 
3) once all blobs counted for, correct the overcount in the last frame

VISUALIZATIONS: 
- the images in output_imgs show make_ellipses attempt to identify the blobs 
- !!! some may identify the same blob (there is blob count overlap) !!! 

FEASIBILITY: 
- unlike the other attempts, at least make_ellipses does it's one job, even if not very well 
- also - there was a bug where altering the img file name somehow affected the number of blobs identified 
- so it's very possible that this approach might not work, but it's worth exploring more 

IMPORTANT FILES 
========================
output_imgs/ 
-- contains the output images from make_ellipses.py
-- img_output_name.png = AREA_CIRCULARITY_CONVEXITY_INERTIA.png

Barnacles/ 
-- contains the given files for the data challenge 

make_ellipses.py 
-- attempt to identify the barnacle contours in the masks

logs.txt 
-- contains some other comments, trials, and thoughts 

find_circles.py
-- one attempt to try and draw circles around the barnacle contours (blobs) in the masks
-- (you need to exit the img window in order for it to refresh)
-- can successfully draw circles around some blobs, but otherwise it totally misses
-- does not work and scrapped in favor of make_ellipses.py

find_contours.py
-- one attempt to try and make the contours around the barnacles (to get the masks)
-- does not work 

grid_search.py
-- at one point wanted to see if could find "optimal" parameters 
so that make_ellipses could catch the most blobs in one go 
-- doesn't quite work out because we want all blobs, not just the most optimal ones 
