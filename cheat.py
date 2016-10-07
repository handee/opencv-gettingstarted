
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
    grey_difference_img = cv2.cvtColor(difference_img, cv2.COLOR_BGR2GRAY)
    ret,motionmask = cv2.threshold(grey_difference_img,difference_thresh,255,cv2.THRESH_BINARY)
#exercise 4a
    motionmask_visualisation= cv2.cvtColor(motionmask, cv2.COLOR_GRAY2BGR)
    output_image=motionmask_visualisation.copy()  
# exercise 1: make it grey    
    
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# exercise 2: import haar cascade, detect faces
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(grey, 1.2, 2)
    for (x,y,w,h) in faces:
         print "found a face"
         cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        # exercise 4b
         cv2.rectangle(motionmask_visualisation,(x,y),(x+w,y+h),(255,0,0),2)
         faceregion=img[y:y+h,x:x+w]
         motionmask_visualisation[y:y+h,x:x+w]=faceregion
# remember to change this line so you're visualising the right one
    output_image=motionmask_visualisation.copy()
    cv2.imshow('outputwindow',output_image) # put the image in the output window

    # wait for someone to press escape then destroy the output window 
    if cv2.waitKey(2) & 0xff == 27:
        cv2.destroyAllWindows()
        break
    print "Finished frame {}".format(n)
    n=n+1

