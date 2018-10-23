import cv2
import numpy as np

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
    z=np.mean(thresh1)
    #q=np.std(thresh1)
    #mean.append(z)
    print(" mean =\n")
    print(z)
    
    
    """
    import numpy as np
    import cv2

    im = cv2.imread('test.jpg')
    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,127,255,0)
    image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    img = cv2.drawContours(img, contours, -1, (0,255,0), 3)
    
    cnt = contours[4]
    img = cv2.drawContours(img, [cnt], 0, (0,255,0), 3)


    
    """
    
    
    #std.append(q)
    
    """
    for i in range(1,n+1):
    
    	if count == s*i :
    		cv2.imwrite("frame%d.jpg" % count, thresh1)
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
    """	
    count = count + 1
    
    
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()



