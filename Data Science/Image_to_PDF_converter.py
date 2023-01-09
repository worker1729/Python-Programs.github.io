import os
from PIL import Image
output_dir = "./PDFs" # You need to make a folder with the images as output
source_dir = "./images" # You also have to create a new folder where to get the input files

for file in os.listdir(source_dir):
    if file.split(".")[-1] in ("png", "jpg", "jpeg"):
        image = Image.open(os.path.join(source_dir, file))
        image_converted = image.convert("RGB")
        image_converted.save(os.path.join(output_dir, "{0}.pdf".format(file.split(".")[-2])))
