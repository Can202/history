import os
import sys
import shutil
import requests

if os.path.exists("C:\\hyst\\") == False:
    os.mkdir("C:\\hyst\\")

fil = requests.get("https://github.com/Can202/hyst-compiler/releases/download/0.0.1/hyst-compiler.exe")
with open("C:\\hyst\\hyst-compiler.exe", 'wb') as f:
    f.write(fil.content)
    f.close()

fil = requests.get("https://raw.githubusercontent.com/Can202/hyst-compiler/a6034b4aa62efd3b2d91145f076b0ce13df5e187/win64/windows.py")
with open("C:\\hyst\\hyst-compiler.py", 'wb') as f:
    f.write(fil.content)
    f.close()

print("Now you can add C:\\hyst\\ to PATH")


