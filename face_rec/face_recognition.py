import numpy as np
import importlib
import cv2
import face_dataset
import face_training


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')   #load trained model
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter, the number of persons you want to include
id = 2 #two persons (e.g. Jacob, Jack)
names = ['']
for i in range(1,100):
    names.append(i)

#names = ['',str(face_id) ]  #key in names, start from the second place, leave first empty

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

flag = True

while flag:

    ret, img =cam.read()

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])        

        if (confidence < 100 and confidence >= 50):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
            name = "ID " + str(id)
            
        elif (confidence > 10 and confidence < 50):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
            name = "ID " + str(id) + " "

        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
            name = "ID " + str(id)

        id = ""
        
        cv2.putText(img, name, (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera',img) 

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
