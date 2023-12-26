import cv2
# Capture video from webcam (0) or a file ('filename.mp4')
cap = cv2.VideoCapture(0)

while True:
    # Read a frame
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow('Video', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()
cv2.destroyAllWindows()
