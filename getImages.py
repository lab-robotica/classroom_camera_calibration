# Original code from https://github.com/niconielsen32/CameraCalibration
# Adapted by G00Z-G00Z

import cv2
from configuration import IMAGES_PATH

cap = cv2.VideoCapture(
    2
)  # The index of the camera to use (usually 0 is for the internal, and 2 is for the external)

num = 0

while cap.isOpened():
    succes, img = cap.read()

    k = cv2.waitKey(5)

    if k == 27:
        break
    elif k == ord("s"):  # wait for 's' key to save and exit
        img_name = f"{num}.png"
        cv2.imwrite(f"{IMAGES_PATH.absolute()}{img_name}", img)
        print("Image saved: " + img_name)
        num += 1

    cv2.imshow("Img", img)

# Release and destroy all windows before termination
cap.release()

cv2.destroyAllWindows()
