import cv2

# Create a black image
img = cv2.imread("/home/henrikvklasson/rain-images.jpg")  # Update the path to an actual image

# Display the image in a window
cv2.imshow('Test Window', img)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
