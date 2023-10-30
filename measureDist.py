import pygame
import pickle
import numpy as np


def get_coordinates(
    camera_matrix: np.ndarray, u: int, v: int, z_mts: float
) -> tuple[float, float]:
    """
    Get the coordinates of a pixel in the image in meters
    :param camera_matrix: The camera matrix
    :param u: The x coordinate of the pixel
    :param v: The y coordinate of the pixel
    :param z_mts: The distance of the pixel from the camera in meters
    """
    fx = camera_matrix[0][0]
    fy = camera_matrix[1][1]
    cx = camera_matrix[0][2]
    cy = camera_matrix[1][2]

    x = (u - cx) * z_mts / fx
    y = -(v - cy) * z_mts / fy

    return x, y


Z_MTS = 2.5  # m
pygame.init()

# Load the desire image
img = pygame.image.load("calibrated-images/logitech-c920-1/1.png")

PATH_TO_CALIBRATION = "calibrated-images/logitech-c920-1/calibration.pkl"

with open(PATH_TO_CALIBRATION, "rb") as file:
    data = pickle.load(file)

camera_matrix = data[0]
dist = data[1]

print(camera_matrix)
# Get the image size
imageWidth, importHeight = img.get_size()

# Create a Pygame window with similar dimensions as the image
screen = pygame.display.set_mode((imageWidth, importHeight))

# Display the image on the Pygame window
screen.blit(img, (0, 0))  # Draw one image onto another
pygame.display.flip()  # Update the contents of the entire display

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Mouse click
            (
                u,
                v,
            ) = event.pos  # Get the position of the mouse click
            pixelColor = img.get_at(
                (u, v)
            )  # Get the color of the pixel at the mouse click

            x, y = get_coordinates(camera_matrix, u, v, Z_MTS)
            print(f"Pixel at ({u},{v})")
            print(f"Pixel at ({x},{v}) is {pixelColor}")

pygame.quit()
