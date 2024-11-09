# Import the libraries
from PIL import Image
import numpy as np
import os
# Import tqdm for progress bar
import tqdm
# Suppress the DecompressionBombWarning
Image.MAX_IMAGE_PIXELS = None

# Define the input and output directories
input_dir = "input"
output_dir = "output"

# Define the matrix filter as a 3x3 numpy array
# This filter is a simple sharpening filter
# You can change the values to get different effects
filter = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

# Loop through all the files in the input directory
# Wrap the loop with tqdm for progress bar
for filename in tqdm.tqdm(os.listdir(input_dir)):
    # Check if the file is an image
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Open the image using Pillow
        image = Image.open(os.path.join(input_dir, filename))
        # Convert the image to a numpy array
        image_array = np.array(image)
        # Get the dimensions of the image
        height, width, channels = image_array.shape
        # Create an empty array for the output image
        output_array = np.zeros_like(image_array)
        # Create a nested tqdm loop for each image
        # Pass the total number of pixels to tqdm
        with tqdm.tqdm(total=height*width*channels) as pbar:
            # Loop through each pixel of the image
            for i in range(1, height-1):
                for j in range(1, width-1):
                    for k in range(channels):
                        # Apply the filter to the pixel and its neighbors
                        # using convolution
                        output_array[i, j, k] = np.sum(
                            filter * image_array[i-1:i+2, j-1:j+2, k])
                        # Clip the values to be between 0 and 255
                        output_array[i, j, k] = np.clip(
                            output_array[i, j, k], 0, 255)
                        # Update the progress bar by one unit
                        pbar.update(1)
        # Convert the output array back to an image using Pillow
        output_image = Image.fromarray(output_array)
        # Save the output image to the output directory
        output_image.save(os.path.join(output_dir, filename))
