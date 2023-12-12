#Import modules and libraries
import Import_Image2
import Image_Processing2
import cv2

#Create main function
def main():
    #Call Capture Image Function and pass image to Variable Image
    Import_Image2.CaptureImage()
    Image_Processing2.Process_Image()


#call main
main()

