import cv2
import numpy as np

cap = cv2.VideoCapture(0)
count = 0
mean=[]
std=[]
n=10
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
    
    
    for i in range(1,n+1):
    
    	if count == s*i :
    		cv2.imwrite("frame%d.jpg" % count, thresh1)
    		r=cv2.imread('frame%d.jpg' % count,0)
    		#cv2.imshow('image1',img1)
    		#h,w,c=img1.shape
		#b,g,r=cv2.split(img1)
		#np.set_printoptions(threshold=np.nan)
		#print(b)
		
		#imgray = cv2.cvtColor(r, cv2.COLOR_BGR2GRAY)
		ret, thresh = cv2.threshold(r, 50, 255, 0)

		im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		if count == 10:
			cv2.imwrite("aaacontour.jpg",im2)
			print(hierarchy)
			imcoun=cv2.drawContours(im2,contours,-1,(255,255,0),25);
			cv2.imwrite("aaaadraw.jpg",imcoun)
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



