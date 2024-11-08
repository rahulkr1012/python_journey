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

# Paths to the pawn and rook images
pawn_image_path = 'img1.png'
rook_image_path = 'img2.png'

# Calculate black areas
pawn_image_name, pawn_black_area = calculate_black_area(pawn_image_path)
rook_image_name, rook_black_area = calculate_black_area(rook_image_path)

# Display the results with image names
print(f"Black surface area for {pawn_image_name}: {pawn_black_area} pixels")
print(f"Black surface area for {rook_image_name}: {rook_black_area} pixels")

# Determine the piece with the minimum and maximum black area
if pawn_black_area < rook_black_area:
    print(f"{pawn_image_name} is the Pawn with the minimum black surface area.")
    print(f"{rook_image_name} is the Rook with the maximum black surface area.")
elif rook_black_area < pawn_black_area:
    print(f"{rook_image_name} is the Pawn with the minimum black surface area.")
    print(f"{pawn_image_name} is the Rook with the maximum black surface area.")
else:
    print("Both images have the same black surface area.")
