<h1>Transparent PNG Image Cropper</h1>

- This Python script utilizes the PIL fork, Pillow, to process a PNG image, with a transparent background, to create a bounding box around the pixel area that has non-transparent pixels and then crop the excess transparent border of the image.


<h2>Use Case</h2>

- Printing where a raster image processor (RIP) is used. 
- This allows the printing application to accurately print an image to the desired physical size.


<h2>Requirements</h2>

Tested on...
- Python 3.9
- Pillow 8.4


<h2>Process</h2>

1. The script will iterate through the current directory looking for PNGs
2. Once a PNG is found it opens the image and utlilzes the image.getbbox() method to isolate the non-transparent pixels.
3. Then the script utilizes the image.crop() method to remove the area around the bounding box.
4. The image is then saved in a subdirectory created at the beginning of the script.


<h2>Errors & Additional Considerations</h2>

<h3>Duplicate filenames</h3>

- What if the filename already exists in the subdirectory?
  - The script checks if there is an existing txt log for duplicates in the subdirectory, if not it creates one.
  - Also, upon initializing the script, an empty list called duplicates is created and a timestamp is written at the top of the txt log.
  - As duplicates are found, the filenames are added to the duplicates list and the filenames are added to new lines in the txt log.
- What if I'm not paying attention to the txt log everytime the script is run?
  - The script checks if there are any entries in the duplicates list
  - If so, then ctypes is utilized to create a popup dialog indicating that there are duplicates!
 
<h3>High Resolution Images</h3>

- Pillow has a maximum image size value that can constrain the function of this script and will warn of a potential decompression bomb when an image exceeds the default max value.
- This can happen frequently when dealing with high resolution print images.
- The script changes the value to none so that images of any size can be processed.
