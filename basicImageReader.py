import cv2
# Read an image
image = cv2.imread(0)

# Display the image
cv2.imshow('Image', image)

# Wait for a key event and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
