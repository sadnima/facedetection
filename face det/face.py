import cv2
import numpy as np
import face_recognition

elon=face_recognition.load_image_file("images\elon1.jpg")
elon=cv2.cvtColor(elon,cv2.COLOR_BGR2RGB)
Test=face_recognition.load_image_file("images\elontest.jpg")
Test=cv2.cvtColor(Test,cv2.COLOR_BGR2RGB)
facloc=face_recognition.face_locations(elon)[0]
encodeElon=face_recognition.face_encodings(elon)[0]
cv2.rectangle(elon,(facloc[3],facloc[0]),(facloc[1],facloc[2]),(255,0,255),2)


faceloctest=face_recognition.face_locations(Test)[0]
encodetest=face_recognition.face_encodings(Test)[0]
cv2.rectangle(Test,(faceloctest[3],faceloctest[0]),(faceloctest[1],faceloctest[2]),(255,0,255),2)
results=face_recognition.compare_faces([encodeElon],encodetest)
facedis=face_recognition.face_distance([encodeElon],encodetest)
print(results,facedis)
cv2.putText(Test,f'{results} {round(facedis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
                    

cv2.imshow("Elon Mask",elon)
cv2.imshow("ElonTest",Test)
cv2.waitKey(0)