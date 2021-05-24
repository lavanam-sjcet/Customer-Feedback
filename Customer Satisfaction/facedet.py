import numpy as np
import cv2 
from newmodel import FacialExpressionModel
import matplotlib.pyplot as plt
def convertToRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def detect_faces(cascade, test_image, scaleFactor = 1.1):
    # create a copy of the image to prevent any changes to the original one.
    image_copy = test_image.copy()
    font = cv2.FONT_HERSHEY_SIMPLEX
    model = FacialExpressionModel("face_model.json", "test.pickle")
    #convert the test image to gray scale as opencv face detector expects gray images
    gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
    
    # Applying the haar classifier to detect faces
    faces_rect = cascade.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors=5)
    
    for (x, y, w, h) in faces_rect:
        cv2.rectangle(test_image, (x, y), (x+w, y+h), (0, 255, 0), 15)
        fc = gray_image[y:y+h, x:x+w]
                    
        roi = cv2.resize(fc, (48, 48))
        # emotion prediction from face
        pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis])
        
##        if pred=="Angry":
##            angcnt+=1
##        if pred=="Disgust":
##            discnt+=1
##        if pred=="Fear":
##            fearcnt+=1
##        if pred=="Happy":
##            hapcnt+=1
##        if pred=="Sad":
##            sadcnt+=1
##        if pred=="Surprise":
##            surcnt+=1
##        if pred=="Neutral":
##            neucnt+=1
        
        # add text in the window
        cv2.putText(test_image, pred, (x, y), font, 1, (255, 255, 0), 2)
        cv2.rectangle(test_image,(x,y),(x+w,y+h),(255,0,0),2)
    return test_image

test_image2 = cv2.imread('a1.jpg')

haar_cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#call the function to detect faces
faces = detect_faces(haar_cascade_face, test_image2)

#convert to RGB and display image
cv2.imshow("image",faces)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("----")
