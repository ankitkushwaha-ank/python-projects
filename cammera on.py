import cv2

# Initialize the camera (0 is the default camera)
camera = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not camera.isOpened():
    print("Error: Could not open camera")
else:
    # Capture a frame (take a picture)
    ret, frame = camera.read()

    # If frame is captured successfully
    if ret:
        # Display the captured image
        cv2.imshow("Captured Image", frame)

        # Save the image to a file
        cv2.imwrite("captured_image.jpg", frame)

        # Wait for a key press and close the window
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error: Could not read frame")

# Release the camera
camera.release()