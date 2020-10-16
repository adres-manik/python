#
# Resize (reduce) images (.png .jpg) size using ffmpeg
# 
# Create by Adres Ginting <adres.manik@gmail.com>
# Tangerang Selatan, 15rd October 2020
#
# All image file put on same folder with this script,
# All image file will executed one-by-one


import glob, os
import fileinput
import re

global textfilename
global counter
 
# this command return path of running script.py
script_path = os.path.realpath(__file__)
head, tail = os.path.split(script_path)
script_path = head

os.chdir(script_path)

# List all image files on current folder on the list box
for image in glob.glob("**/*.??g", recursive = True):
    output = "out-" + image 
    command = f"ffmpeg -i {image} -vf scale=800:-1 -compression_level 9 {output}"
# scale=800:-1 means rescale to width=800 and proportional
#    command = f"ffmpeg -i {image} -vf scale=800:-1 {output}"
    os.system(command)
    os.remove(image)
    os.rename(output,image)
