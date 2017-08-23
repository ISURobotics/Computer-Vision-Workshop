#Check out http://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/ for a great ball tracking tutorial.

import cv2
import numpy as np
cap = cv2.VideoCapture(0) #This creates an object named cap. It captures images from your webcam, which is defined by the number 0.
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920) #Now we're capturing a nice 1080p image!
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cap.set(cv2.CAP_PROP_AUTOFOCUS, 0) #Gets rid of autofocus - this can be annoying and mess with image processing.
cap.set(cv2.CAP_PROP_FOCUS, 0) #Set a fixed focal distance.
cap.set(cv2.CAP_PROP_BRIGHTNESS, 100) #Sets the brightness of your image. 0-255
cap.set(cv2.CAP_PROP_SATURATION, 200) #Sets the saturation(0-255)
cap.set(cv2.CAP_PROP_CONTRAST, 200)


#Let's set up some tresholding bounds.
blueLower = (90, 250, 80) #These values are in the HSV color space - hue, saturation, value. Ranges are 0-180, 0-255, 0-255.
blueUpper = (110, 255, 255)


while True:
	returnCheck, img = cap.read() #Tries to capture an image (read an image from the webcam). Stores the image in img.
	
	
#This is based off the blog post linked above!	
	hsvimg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #Creates a new image in the HSV color space... What's HSV?!
	mask = cv2.inRange(hsvimg, blueLower, blueUpper) #Creates a binary mask of where things are blue.
	mask = cv2.erode(mask, None, iterations = 3) #Filters out noise in the image to get a better mask
	mask = cv2.dilate(mask, None, iterations = 3)
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2] #makes an object (cnts, short for contours) that stores the locations of all boundaries in the mask.
	if len(cnts) > 0:
			# find the largest contour in the mask, then use
			# it to compute the minimum enclosing circle and
			# centroid
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"])) #a bit advanced, but it finds the center of the circle.

			# only proceed if the radius meets a minimum size
		if radius > 10:
				# draw the circle and centroid on the frame,
				# then update the list of tracked points
			cv2.circle(img, (int(x), int(y)), int(radius),(0, 255, 255), 4) #Draw the circle.
			cv2.circle(img, center, 5, (0, 0, 255), -1) #Make a dot on the center.
	
	
	
	
	
	
	cv2.imshow("Webcam", img) #cv2.imshow() displays an image.  Can be from a webcam, a file, etc.
	if cv2.waitKey(2) & 0xFF == ord('q'): #if the user presses the q key...
		break #exit the while loop.

cap.release() #This tells Windows "hey, we're done with the webcam, you can have it back now"
cv2.destroyAllWindows() #We're done, so destroy any Windows created by opencv.
