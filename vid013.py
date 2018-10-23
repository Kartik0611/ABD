import cv2
import numpy as np
import os
import time

cap = cv2.VideoCapture(0)
count = 0
mean=[]
std=[]
n=20
s=2
t1=100	#above which is considered as high (white)


while cap.isOpened():

    ret,frame = cap.read()
    if ret == False:
    	print("Frame is empty")
    	break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret,thresh1 = cv2.threshold(gray,t1,255,cv2.THRESH_BINARY)
    #cv2.imshow('window-name',thresh1)
    
    #cv2.imwrite("frame%d.jpg" % count, thresh1)
    #r=cv2.imread('frame%d.jpg' % count,0)
    #np.set_printoptions(threshold=np.nan)
    #print(b)
    #os.remove("frame%d.jpg" %count)
    z=np.mean(frame)
    q=np.std(frame)
    mean.append(z)
    std.append(q)
    
    im2, contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.imwrite("aaacontour.jpg",im2)
    #print(hierarchy)
    imcoun=cv2.drawContours(frame,contours,-1,(255,255,0),5);
    cv2.imshow("aaaadraw.jpg",imcoun)
    
    #cv2.drawContours(thresh1,contours,-1,(0,255,50),10);
    
    
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



