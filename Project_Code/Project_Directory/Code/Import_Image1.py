#Importing cv2 library
import cv2

#Starts computer camera 
cam = cv2.VideoCapture(0)

#Naming module
cv2.namedWindow("Python Computer Camera Image Capture Module")

img_counter = 0

while True:
    #reading the frames from computer camera
    ret,frame = cam.read()
    
    #Exception Handling if we fail to grab an image
    if not ret:
        print("failed to grab frame")
        break
    
    #Shows the computer camera to user
    cv2.imshow("Test",frame)

    #Allow User to choose to exit application by hiting Esc key
    k = cv2.waitKey(1)
    if k%256 == 27:
        print("Escape hit, closing the app")
        break

    #Binding the space bar to trigger take picture
    elif k%256 == 32:
        img_name = "opencv_frame_{}.png".format(img_counter) #Number image
        cv2.imwrite(img_name,frame)
        print("Screenshot Taken")
        img_counter += 1



cam.release()

#Remove all images taken 
#cam.destroyAllWindows()