import cv2

cap = cv2.VideoCapture(0) #This creates an object named cap. It captures images from your webcam, which is defined by the number 0.

while True:
	returnCheck, img = cap.read() #Tries to capture an image (read an image from the webcam). Stores the image in img.
	cv2.imshow("Webcam", img) #cv2.imshow() displays an image.  Can be from a webcam, a file, etc.
	if cv2.waitKey(2) & 0xFF == ord('q'): #if the user presses the q key...
		break #exit the while loop.

cap.release() #This tells Windows "hey, we're done with the webcam, you can have it back now"
cv2.destroyAllWindows() #We're done, so destroy any Windows created by opencv.