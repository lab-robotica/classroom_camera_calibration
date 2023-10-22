# General Camera Calibration

OpenCV method for calibrating cameras with python. This repo follows the
[tutorial](https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html). Also here is a video that also explains it very good.

![Video explaining camera calibration](https://www.youtube.com/watch?v=3h7wgR5fYik)

# Cameras Calibrated

| Name | Model | Calibrated | 
| ---- | ----- | --- | 
| Web Cam Lab | web_cam | no | 

# Setup

Install the following: 

- python
- opencv

Then you need *chessboard pictures* in order to calibrate the camera. You need a chessboard with a known *mxn* grid (where **m** is even and **n** is odd). Then you need to take **at least 14 images** with the following requirements: 

- The must be taken with a **static camera** (the camera is fixed and the chessboard is the only thing that moves)
- The images must display the chessboard in different positions, rotations, and small perspective changes (skewed)
- **Opencv** must be able to find the chessboard with the function  `cv.findChessboardCorners`

Then save the images under `./uncalibrated-images/<model_name>`. Then, run the script `./calibrate.py`, changing the `MODEL_NAME` variable to match the `<model_name>`
