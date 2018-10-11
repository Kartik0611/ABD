import cv2
import numpy as np
import os

cap = cv2.VideoCapture(0)
count = 0
mean=[]
std=[]
n=20
s=2
t1=200	#above which is considered as high (white)

while cap.isOpened():

    ret,frame = cap.read()
    if ret == False:
    	print("Frame is empty")
    	break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret,thresh1 = cv2.threshold(gray,t1,255,cv2.THRESH_BINARY)
    cv2.imshow('window-name',thresh1)
    
    cv2.imwrite("frame%d.jpg" % count, thresh1)
    r=cv2.imread('frame%d.jpg' % count,0)
    #np.set_printoptions(threshold=np.nan)
    #print(b)
    os.remove("frame%d.jpg" %count)
    z=np.mean(r)
    q=np.std(r)
    mean.append(z)
    std.append(q)
    #print("\n")
    #print("mean = \n")
    #print(mean)
    #print("\n")
    #print("standard deviation =\n")
    #print(std)		
    count = count + 1
    
    
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()



