import cv2

# Importing haarcascades for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

# Create video capturing instance
cap = cv2.VideoCapture(0)

start_detecting = False
blink_count = 0

while (True):
  ret, frame = cap.read()
  
  # Convert image to grayscale
  gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # Detect faces
  faces = face_cascade.detectMultiScale(gray_scale, 1.3, 5, minSize = (200, 200))

  if len(faces) > 0:
    for (x, y, w, h) in faces:

      # Draw rectangle where face is found
      frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

      # Crop face region to detect eyes
      face = gray_scale[y:y+h, x:x+w]

      # Detect eyes in cropped region
      eyes = eyes_cascade.detectMultiScale(face, 1.3, 5, minSize= (50, 50))
      
      # When no eyes are found (blink) we increase the blink count and
      # set start_detecting to False. This will ensure that next blink will 
      # be detected when user opens the eyes again  
      if len(eyes) >= 2:
        start_detecting = True      
      else:
        if start_detecting:
          blink_count  = blink_count + 1
          start_detecting = False
  else:
    # Reset the values if no face found
    start_detecting = False
    blink_count = 0

  # Print Blink count
  cv2.putText(frame, "BLINK COUNT: {}".format(blink_count), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)    
  
  cv2.imshow('Frame', frame)

  # Quit using 'q' key
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()