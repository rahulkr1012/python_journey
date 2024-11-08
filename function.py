import cv2
import numpy as np
import os

def calculate_black_area(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image at path {image_path} could not be loaded.")
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply a binary threshold to separate the piece from the background
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    
    # Calculate black surface area (number of black pixels)
    black_area = np.sum(binary == 255)  # 255 indicates black in the inverted image
    
    # Get the image name from the path
    image_name = os.path.basename(image_path)
    
    return image_name, black_area