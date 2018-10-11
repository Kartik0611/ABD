import cv2
import numpy as np

cap = cv2.VideoCapture(0)
count = 0
mean=[]
std=[]
n=10
s=15


while cap.isOpened():

    ret,frame = cap.read()
 
    cv2.imshow('window-name',frame)
    
    
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()



