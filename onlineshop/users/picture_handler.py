import os
# pip install pillow works here to get PIL going.
# Solution at: https://stackoverflow.com/questions/20060096/installing-pil-with-pip
from PIL import Image
from flask import url_for, current_app

def add_profile_pic(pic_upload,username):

# The splitter splits the filename around its dot and then goes
# on to adjust the original filename
    filename = pic_upload.filename
    ext_type = filename.split('.')[-1]
    storage_filename = str(username) + '.' +ext_type

    filepath = os.path.join(current_app.root_path, 'static/profile_pics', storage_filename)

# The size of the output picture can be adjusted here
    output_size = (300, 300)

# this uploads the picture, adjusts the size to 300x300, then saves it on the
# above filepath
    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename
