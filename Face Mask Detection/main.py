# Import packages
import cv2
import tensorflow as tf
import numpy as np

# Import model
model = tf.keras.models.load_model('model.h5')

# Create video capturing instance
cap = cv2.VideoCapture(0)

while (True):
  ret, frame = cap.read()

  face = frame
  face = cv2.resize(face, (224, 224)) # Resize image
  face = np.array([face]) # Adding extra dimension
  face = face / 255.0 # Scale image

  prediction = model.predict(face) # Predict 
  
  # Print text
  if prediction >0.5:
    cv2.putText(frame, "MASK FOUND", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)     
  else:
    cv2.putText(frame, "NO MASK FOUND", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)  
  
  cv2.imshow('Frame', frame)

  # Quit using 'q' key
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()