"""
Configuration file for the camera calibration script
Change the variables to suit your needs

The test data variables will be used to test the script
"""
from pathlib import Path

# Test data
MODEL_NAME = "lab_web_cam"
CHESSBOARD_SIZE = (9, 6)
IMAGE_EXTENSIONS = "jpg"  # png, jpg, jpeg, bmp, tiff, tif, pgm, ppm, pbm, sr, ras, jp2, j2k, jpf, jpx, jpm, mj2 ...
FRAME_SIZE = (640, 480)


# Tests for correct data

# Check image path
UNCALIBRATED_IMAGES_PATH = Path(".") / "uncalibrated-images" / MODEL_NAME
CALIBRATED_IMAGE_PATH = Path(".") / "calibrated-images" / MODEL_NAME
CALIBRATED_IMAGE_PATH.mkdir(parents=True, exist_ok=True)

if not UNCALIBRATED_IMAGES_PATH.exists():
    raise Exception(f"Path {UNCALIBRATED_IMAGES_PATH} does not exist")

# Check even x odd chessboard size
if CHESSBOARD_SIZE[0] % 2 == 0:
    raise Exception("CHESSBOARD_SIZE[0] must be odd")
if CHESSBOARD_SIZE[1] % 2 == 0:
    raise Exception("CHESSBOARD_SIZE[1] must be odd")
