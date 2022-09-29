
#[10 points] Write a Python application to take an image file, or a directory full of images files, and
#convert them into a specified format. The CLI (command line interface) should look like this:
#$ python process_image.py <filename>|<dir> <format> [<output_dir>]
#A digression on CLI syntax...

#Let’s make sure you understand the syntax above, which defines the required program invocation by
#showing the name of the program, and also the acceptable command line arguments. First, the name of
#your program file must be “process_image.py”. So to invoke it on the command line, a user would pass
#this program file to the python interpreter like:
#$ python process_image.py
#Next, we specify a number of command line arguments, some required, some optional. Let’s start with
#the first one:
#$ python process_image.py <filename>|<dir>
#In the above, <filename> means you should provide a filename as a string, and <dir> means you should
#provide a directory path as a string. The “|” between them indicates a logical OR, so this means the user
#will either provide a filename OR a directory path as the first argument to the program. This represents
#a divergence in behavior – your program must be able to detect whether this argument is a filename or
#a directory, and behave appropriately depending on which is provided by the user.
#Let’s keep going...
#$ python process_image.py <filename>|<dir> <format>

#Now we’ve added a second argument, <format>. No logical OR here, so there is only one option. For
#this project, the value of the input <format> is an image file extension without the preceding period.
#The extensions you should support are:
#• jpg
#• jpeg
#• png
#• bmp
#• tiff


# importing the module
import sys
from PIL import Image


# error if statement
#if len(sys.argv) != 2:
#    print('error. please provide an input file.')
#    print()
#    print("usage: python process_image.py <file>.")
#    sys.exit(1)


# storing the arguments
program = sys.argv[0]
arg1 = sys.argv[1]
arg2 = sys.argv[2]
  

image = Image.open(arg1)

format = image.save("dopes.png")


print("Converting", arg1, "to", arg2)
  
# displaying the arguments
print("arg1 : " + arg1)
print("arg2 : " + arg2)
#print("Number of arguments : ", len(sys.argv))
#print(sys.argv)

# displaying the program name
print("Program name : " + program)
