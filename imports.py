from PIL import Image
import argparse
import sys


#inputs= input()

#inputs = {}


formats = {
    "jpg": "jpg",
    "jpeg": "jpeg",
    "png": "png",
    "bmp": "bmp",
    "tiff": "tiff",
}

parser = argparse.ArgumentParser(description="Formats")
#parser.add_argument("file", type=str)
parser.add_argument("extension", type=str)
args = parser.parse_args()

type = formats.get(args.extension, "")
print(type)


#file = Image.open(inputs)


#image = Image.open(fish)


#image.save("dopes.png")


#print("Converting", image, "to", outfile)

