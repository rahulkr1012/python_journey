import cv2
import numpy as np
import os
import function

# Paths to the pawn and rook images
pawn_image_path = 'img1.png'
rook_image_path = 'img2.png'

# Calculate black areas
pawn_image_name, pawn_black_area = function.calculate_black_area(pawn_image_path)
rook_image_name, rook_black_area = function. calculate_black_area(rook_image_path)

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
