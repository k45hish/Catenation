import sys
try:
    if sys.argv[1]=="test.txt":
        with open("test.txt")as f:
            f.read()
except FileNotFoundError:
        print("File name is invalid, please enter name again : ")
#use in read only