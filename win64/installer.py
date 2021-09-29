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


