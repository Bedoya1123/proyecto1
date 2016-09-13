
# coding: utf-8

# In[ ]:


import numpy as np
import cv2
 

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
capture = cv2.VideoCapture(0)
 
while(True):
    
    ret, imagen = capture.read()
    
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
 
    for (x,y,w,h) in faces:
        cv2.rectangle(imagen,(x,y),(x+w,y+h),(125,255,0),2)
 
    cv2.imshow('img',imagen)
     
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()
cv2-destroyAllWindows()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



