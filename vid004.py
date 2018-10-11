import cv2
cap = cv2.VideoCapture("vtest1.webm")
count = 0
while cap.isOpened():
    ret,frame = cap.read()
    cv2.imshow('window-name',frame)
    
    vidframe=cap.get(cv2.CAP_PROP_POS_FRAMES)
    
    if vidframe < 20:
    
    	cv2.imwrite("frame%d.jpg" % count, frame)
    
    
    if count == 0:
    	img1=cv2.imread('frame1.jpg',0)
    	cv2.imshow('image1',img1)
    	print(img1)
	
	
    count = count + 1
    
    
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()



