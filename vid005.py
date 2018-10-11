import cv2
cap = cv2.VideoCapture(0)
count = 0
while cap.isOpened():
    ret,frame = cap.read()
    cv2.imshow('window-name',frame)
    
    cv2.imwrite("frame%d.jpg" % count, frame)
    img1=cv2.imread('frame%d.jpg' % count,0)
    cv2.imshow('image1',img1)
    #if count == 2 or count == 4 :
    #	img1=cv2.imread('frame%d.jpg' % count,1)
    #	cv2.imshow('image%d' % count,img1)
    #	print(img1)
	
	
    count = count + 1
    
    
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()



