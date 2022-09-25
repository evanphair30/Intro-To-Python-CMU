from PIL import Image
import sys

if len(sys.argv) != 2:
    print('Error. please provide an input file.')
    print()
    print("Usage: python testing.py <file>.")
    sys.exit(1)

infile = sys.argv[1]

image = Image.open(infile)

#if len(sys.argv) != 2:
#    print('Error. please provide an input file.')
#    print()
#    print("Usage: python testing.py <file>.")
#    sys.exit(1)

#infiles = sys.argv[1]

image.save("dopes.png")


print("Converting", infile, "to outfile")

#image.show()
#def images():

#    if img

#    else



#if else abort/return fails



#def imags():

#    if img

#    else


