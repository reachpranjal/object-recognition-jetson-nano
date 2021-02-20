import jetson.inference
import jetson.utils
import time
import cv2
import numpy as np 

# Return the time as a floating point number expressed in seconds
# since the epoch, in UTC
timeStamp = time.time() 

# Initializing Filter FPS
fpsFilt=0  

# Initialize the Neural Network
net=jetson.inference.detectNet('ssd-mobilenet-v2',threshold=.5)

# Set display window resolution
dispW=640
dispH=480

# default flip=0
flip=2

# Set font
font=cv2.FONT_HERSHEY_SIMPLEX

# Video Capture from USB Camera only and set display window size
cam=cv2.VideoCapture('/dev/video0')
cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)


while True:
    # read camera frame
    _,img = cam.read()
    
    height=img.shape[0]
    width=img.shape[1]

    frame=cv2.cvtColor(img,cv2.COLOR_BGR2RGBA).astype(np.float32)
    frame=jetson.utils.cudaFromNumpy(frame)

    detections=net.Detect(frame, width, height)
    
    for detect in detections:
        ID=detect.ClassID
        top=detect.Top
        left=detect.Left
        bottom=detect.Bottom
        right=detect.Right
        item=net.GetClassDesc(ID)
        print(item,top,left,bottom,right)
    dt=time.time()-timeStamp
    timeStamp=time.time()
    fps=1/dt
    fpsFilt=.9*fpsFilt + .1*fps
    cv2.putText(img,str(round(fpsFilt,1))+' fps',(0,30),font,1,(0,0,255),2)
    cv2.imshow('detCam',img)
    cv2.moveWindow('detCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
