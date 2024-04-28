from PIL import Image
import os
import re


def splitAndSave(filename, path, output_dir=None):
    # If output_dir not passed treat path as output dir
    if output_dir is None:
        output_dir = path

    # Check if output directory exists
    # If returns a file not found error create it.
    try:
        os.listdir(output_dir)
    except FileNotFoundError:
        os.makedirs(output_dir)

    # Split filename by "."
    split_filename = re.split("\.", filename)
    # Take all but last element and join into string separated by "."
    filename = ".".join(split_filename[0:-1])
    # Take last element as the file extension
    extension = "." + split_filename[-1]

    with Image.open(f"{path}/{filename}{extension}") as im:
        # Create left and right boxes (image split in middle)
        left_tuple = [0, 0, im.width / 2, im.height]
        right_tuple = [im.width / 2, 0, im.width, im.height]
        # Crop and save
        im.crop(box=left_tuple).save(f"{output_dir}/{filename}_L{extension}")
        im.crop(box=right_tuple).save(f"{output_dir}/{filename}_R{extension}")
