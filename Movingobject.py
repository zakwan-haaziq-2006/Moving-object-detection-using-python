import cv2
import imutils

FirsFrame = None
print("Initializing the camera...")
area = 700
cam = cv2.VideoCapture(0)
while True:
    text = "Normal"
    _,img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gaussian = cv2.GaussianBlur(gray,(11,11),1)
    
    if FirsFrame is None :
        FirsFrame = gaussian
        continue
    
    img_Diff = cv2.absdiff(FirsFrame,gaussian)
    
    thresh = cv2.threshold(img_Diff,25,255,cv2.THRESH_BINARY)[1]
    
    cnts = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    
    
    for c in cnts:
        if cv2.contourArea(c) > area :
            
            (x,y,w,h) = cv2.boundingRect(c)
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
            text = "Moving Object Detected..."
    cv2.putText(img,text,(10,20),1,cv2.FONT_HERSHEY_COMPLEX,(0,0,255),2)

    cv2.imshow("Frame",img)
    
    key = cv2.waitKey(10)
    if key == 27 :
        break
cam.release()
cv2.destroyAllWindows()    