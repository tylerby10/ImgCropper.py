# Python Script used on PNG Images with transparent backgrounds to trim excess transparent space.
# This script will iterate through the directory where it is located to find the images.
# There are several helpful errors and logs generated as well.
# This is helpful for images that need to be printed with accurate physical dimesions.

# Import necessary libraries
import ctypes
import os
import datetime
from PIL import Image

# Disable the maximum image pixel limit in Pillow (PIL)
# Many high resolution images will trip the Decompression Bomb Warning
Image.MAX_IMAGE_PIXELS = None

# Set the directory to the current directory (where the script is located)
directory = '.'

# Check if a directory named "Cropped" does not exist, and if not, create it
if not os.path.exists("Cropped"):
    os.makedirs("Cropped")

# Initialize an empty list to store duplicate filenames
duplicates = []

# Open a file for writing to store duplicate filenames
with open("Cropped/duplicate_filenames.txt", "w") as f:
    
    # Get the current date and time in the format "YYYY-MM-DD HH:MM:SS"
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Write the current date and time to the file
    f.write(f"{current_time}\n")
    
    # Iterate through the files in the current directory
    for filename in os.listdir(directory):
        # Check if the file has a .png or .PNG extension (case insensitive)
        if filename.endswith(".png") or filename.endswith(".PNG"):
            # Open the image using Pillow
            image = Image.open(filename)
            
            # Get the bounding box of the image
            imageBox = image.getbbox()
            
            # Crop the image to the bounding box
            cropped = image.crop(imageBox)
            
            # Create a new filename for the cropped image in the "Cropped" directory
            cropped_filename = "Cropped/" + filename
            
            # Check if a file with the same name already exists in the "Cropped" directory
            if os.path.exists(cropped_filename):
                # If it does, add the filename to the list of duplicates
                duplicates.append(cropped_filename.replace('Cropped/',''))
                # Write the duplicate filename to the duplicate_filenames.txt file
                f.write(f"{cropped_filename.replace('Cropped/','')}\n")
            else:
                # If it doesn't exist, save the cropped image
                cropped.save(cropped_filename)

# Check if there are any duplicate filenames in the list
if duplicates:
    # Display a Windows message box with an error message listing the duplicate filenames
    ctypes.windll.user32.MessageBoxW(0, f"Error: Duplicate files: {duplicates}", "Error", 0x40 | 0x1)
