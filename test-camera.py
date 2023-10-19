import cv2

# Initialize the camera
cap = cv2.VideoCapture(1)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Capture a single frame
ret, frame = cap.read()

# Save the captured frame if it's valid
if ret:
    cv2.imwrite("captured_image.jpg", frame)
else:
    print("Error: Could not capture an image.")

# Release the camera
cap.release()
