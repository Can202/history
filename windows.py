import os
import sys

args = ""

for i in range(len(sys.argv)):
    if i != 0:
        args += sys.argv[i] + " "

os.system("python C:\hyst\hyst-compiler.py " + args)