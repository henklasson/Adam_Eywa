import cv2

# URL of the incoming stream - this should match the one you're sending to
stream_url = 'udp://@:12345'

# Create a VideoCapture object
cap = cv2.VideoCapture(stream_url)

# Check if the stream was opened successfully
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

# Read and display frames from the stream
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Can't receive frame (stream end?). Exiting ...")
        break

    cv2.imshow('Webcam Stream', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

# Release the VideoCapture object and close windows
cap.release()
cv2.destroyAllWindows()
