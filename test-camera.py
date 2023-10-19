import cv2


def check_camera(index):
    """Check if a camera with a given index is available."""
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        cap.release()
        return False
    cap.release()
    return True


def list_cameras(max_cameras=10):
    """List all available cameras up to a specified maximum."""
    available_cameras = []
    for i in range(max_cameras):
        if check_camera(i):
            available_cameras.append(i)
    return available_cameras


if __name__ == "__main__":
    cameras = list_cameras()
    if cameras:
        print("Available cameras are:")
        for cam in cameras:
            print(f"Camera {cam}")
    else:
        print("No cameras available.")
