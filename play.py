# these imports let you use opencv
import cv2 #opencv itself
import common #some useful opencv functions
import video # some video stuff
import numpy as np # matrix manipulations

img=cv2.imread('noidea.jpg')
cv2.namedWindow('outputwindow') # open a window for output

# the line below just copies the input image to the output image.
# try replacing it with some code from the tutorial
output_image=img.copy()


cv2.imshow('outputwindow',output_image) # put the image in the output window

# wait for someone to press escape then destroy the output window 
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

