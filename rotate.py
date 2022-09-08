#[5 points] Write a Python program to solve the following problem: When given any string s and an
#integer r, you must “rotate” the characters of the string r times. Rotation is defined as moving each
#character one space to the right, while shifting the last character to the front of the string. For example,
#“captain”
#Rotated 1 time = “ncaptai”
#Rotated 2 times = “incapta”
#Rotated 3 times = “aincapt”
#…
#Rotated 7 times = “captain”


word = input("Enter a Word:")
num = input("Enter a Rotate Number")

#test = "tiger"

#rust = word[-1:] + word[:-1]

#print (rust)

def rotateString(string,direction,n):
    if direction == "backwards":
        new_string = string[n:] + string[:n]
    else: 
        new_string = string[-n:] + string[:-n]
    return new_string

print(rotateString("progrmaming","backwards",2))
print(rotateString("progrmaming","forwards",3))

#def scramble (word,num):
#    if 

#Your program should consist of a file named rotate.py, and must operate in the following manner:
#$ python rotate.py captain 3
#String “captain” rotated 3 times: aincapt