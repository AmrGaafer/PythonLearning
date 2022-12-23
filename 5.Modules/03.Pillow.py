# -------------------------------------------------------------------------------------------------------------
# Pillow Module: image processing module (external module)
#   Resource: https://pillow.readthedocs.io/en/stable/
# -------------------------------------------------------------------------------------------------------------

import os
os.system('cls')        # cls command

print('\n# ********************************************* #')
print('Pillow module:\n')

# current file path
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

from PIL import Image

# show image and get image information
myImage = Image.open(f'{__location__}\python.jpg')
myImage.show()
print('this image size is ', myImage.width, ' x ', myImage.height)

# crop image
myCropSize = (700, 260, 1300, 860)
myCrop = myImage.crop(myCropSize)
myCrop.show()

# black and white mode
myImageConverted = myImage.convert('L')
myImageConverted.show()
