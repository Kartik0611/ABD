import cv2
import numpy as np

cap = cv2.VideoCapture(0)
count = 0
mean=[]
std=[]
n=20
s=2


while cap.isOpened():

    ret,frame = cap.read()
    if ret == False:
    	print("Frame is empty")
    	break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('window-name',gray)
    
    
    for i in range(1,n+1):
    
    	if count == s*i :
    		cv2.imwrite("frame%d.jpg" % count, frame)
    		r=cv2.imread('frame%d.jpg' % count,0)
    		#cv2.imshow('image1',img1)
    		#h,w,c=img1.shape
		#b,g,r=cv2.split(img1)
		#np.set_printoptions(threshold=np.nan)
		#print(b)
		z=np.mean(r)
		q=np.std(r)
		mean.append(z)
		std.append(q)
		if i == n :
			print("\n")
			print("mean = \n")
			print(mean)
			print("\n")
			print("standard deviation =\n")
			print(std)		
    count = count + 1
    
    
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()



