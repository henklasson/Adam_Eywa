    # Import required libraries
import cv2
import numpy as np
import dlib
import time
initiate_conversation = False
end_conversation = False
def face_detected():
    # Connects to your computer's default camera
    cap = cv2.VideoCapture(0)
  
  
    # Detect the coordinates
    detector = dlib.get_frontal_face_detector()
  
    count = 0
    start_count = False
    global initiate_conversation
    global end_conversation
    greeting = False
    # Capture frames continuously
    while True:
  
        # Capture frame-by-frame
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
  
        # RGB to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
  
        # Iterator to count faces
        i = 0
        face_detected = False
        for face in faces:
  
            # Get the coordinates of faces
            x, y = face.left(), face.top()
            x1, y1 = face.right(), face.bottom()
            cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)
  
            # Increment iterator for each face in faces
            i = i+1
            if face:
                face_detected = True
                start_count = True
                count = 0
            
            # Display the box and faces
            cv2.putText(frame, 'face num'+str(i), (x-10, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            #print(face, i)
  
        # Display the resulting frame
        cv2.imshow('frame', frame)
        
        if start_count == True:
            count +=1
            initiate_conversation = True
            end_conversation = False
        # else:
        #     count = 0
        if count >= 20:
            #print("Goodbye")
            initiate_conversation = False
            end_conversation = True
            start_count = False
            count = 0
            

        
        print(initiate_conversation, end_conversation)
        

        # This command let's us quit with the "q" button on a keyboard.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
  
  
    # Release the capture and destroy the windows
    cap.release()
    cv2.destroyAllWindows()

face_detected()




# if start == False and end == False and greeting == False:
#     pass
# elif start == True and greeting == False:
#     print("Hello")
#     greeting = True
# elif start == False and greeting == True:
#     print("Goodbye")
# else:
#     input("Input:" )
#     response = "This is a response"
#     print(response)
    

# greeting = False
# for initiate_conversation, end_conversation in face_detected():
#     if initiate_conversation == True and greeting == False:
#         print("Hello")
#         greeting = True
#     elif initiate_conversation == False and greeting == True:
#         print("Goodbye")
#     else:
#         while initiate_conversation:
#             input("Input: ")
#             response = "this is a response"
#             print(response)
        

    
        
