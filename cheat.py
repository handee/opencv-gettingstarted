
# these imports let you use opencv
import cv2 #opencv itself
import common #some useful opencv functions
import video # some video stuff
import numpy as np # matrix manipulations

cap = video.create_capture(0)
flag, img = cap.read()
n=0; #let us have a counter
flag, img = cap.read() # get an initial frame
cv2.namedWindow('outputwindow') # open a window for output
cv2.imshow('outputwindow',img) # put the image in the output window


# exercise 3a
fbuffer=35
alpha=float(1.0/fbuffer) 
difference_thresh=10
movingaverage=np.float32(img)

while True:

#read a frame from the video capture obj
    flag, img = cap.read()

# exercise 3b:
    cv2.accumulateWeighted(img,movingaverage,alpha) 
    res=cv2.convertScaleAbs(movingaverage)
    # show the background model 
    #output_image=res.copy()  

# exercise 3c:
    difference_img = cv2.absdiff(res, img)
    #output_image=difference_img.copy()  
   
#exercise 3d: 

# exercise 1: make it grey    

    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# exercise 2: import haar cascade, detect faces
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(grey, 1.3, 5)
    for (x,y,w,h) in faces:
         cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
# remember to change this line so you're visualising the right one
    #output_image=img.copy()
    cv2.imshow('outputwindow',output_image) # put the image in the output window

    # wait for someone to press escape then destroy the output window 
    if cv2.waitKey(2) & 0xff == 27:
        cv2.destroyAllWindows()
        break
    print "Finished frame {}".format(n)

