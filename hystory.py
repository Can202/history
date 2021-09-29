import os
import sys
from sys import exit
import shutil
import PyInstaller.__main__

# Compiler 
# (Transform to py)

init = ""
save = ""
protagonistname = ""
friendname = ""
librarianname = ""
path = ""
savepath = "a.out"
if sys.platform == "win32":
    savepath = "a.exe"
pythonexport = False
variables = []

if len(sys.argv) > 1:
    for u in range(len(sys.argv)):
        if u == 0:
            continue
        elif sys.argv[u-1] == "--save":
            savepath = sys.argv[u]
        elif sys.argv[u] == "--python":
            pythonexport = True
        elif "--" not in sys.argv[u]:
            path = sys.argv[u]
            break
    if os.path.exists(path):
        if path[len(path)-5:len(path)] == ".hyst":
            fiLE = open(path, "r")
            text = fiLE.read()
            fiLE.close()
            commands = text.split(".")
            for i in range(len(commands)):
                if len(commands[i]) > 0:
                    while commands[i].startswith(" ") or commands[i].startswith("\n"):
                        commands[i] = commands[i][1:len(commands[i])]
                if commands[i].lower().startswith("narrador says "):
                    newlines = commands[i].split("\n")
                    for j in range(len(newlines)):
                        if newlines[j].lower().startswith("narrador says "):
                            newlines[j]= newlines[j][14:len(newlines[j])]
                        save += init + "# " + newlines[j]
                        save += "\n"
                else:
                    commands[i] = commands[i].replace(",", ".")
                    commands[i] = commands[i].replace("´", ",")
                    if commands[i].lower().startswith("protagonist is "):
                        func = commands[i][len("protagonist is "):len(commands[i])]
                        protagonistname = func
                    elif commands[i].lower().startswith("friend is "):
                        func = commands[i][len("friend is "):len(commands[i])]
                        friendname = func
                    elif commands[i].lower().startswith("librarian is "):
                        func = commands[i][len("librarian is "):len(commands[i])]
                        librarianname = func
                    elif commands[i].lower().startswith("new history: "):
                        func = commands[i][len("New History: "):len(commands[i])]
                        if " With " in commands[i]:
                            parameter = func[func.find(" With ") + 6: len(func)]
                            func = func[0:func.find(" With ")]
                            save += init + "def " + func + "(" + parameter + "):"
                        else:
                            save += init + "def " + func + "():"
                        save += "\n"
                        init += "    "
                    elif commands[i].lower().startswith("principal"):
                        save += init + "def main():"
                        save += "\n"
                        init += "    "
                    elif commands[i].startswith("Now go to "):
                        func = commands[i][len("Now go to "):len(commands[i])]
                        if " With " in commands[i]:
                            parameter = func[func.find(" With ") + 6: len(func)]
                            func = func[0:func.find(" With ")]
                            save += init + func + "(" + parameter + ")"
                        else:
                            save += init + func + "()"
                        save += "\n"
                    elif commands[i].startswith("Hi "):
                        var = commands[i][3:len(commands[i])]
                        variables.append(var)
                        save += init + var + " = None"
                        save += "\n"
                    elif commands[i].startswith(protagonistname + " says "):
                        var = commands[i][len(protagonistname + " says "):len(commands[i])]
                        save += init + "print(\"" + var + "\")"
                        save += "\n"
                    elif commands[i].startswith(protagonistname + " repeat "):
                        var = commands[i][len(protagonistname + " repeat "):len(commands[i])]
                        save += init + "print(" + var + ")"
                        save += "\n"
                    elif commands[i].startswith(librarianname + " brings "):
                        var = commands[i][len(librarianname + " brings "):len(commands[i])]
                        save += init + "import " + var
                        save += "\n"
                    elif commands[i].startswith(librarianname + " from "):
                        var = commands[i][len(librarianname + " from "):len(commands[i])]
                        var = var[0:var.find(" brings")]
                        libs = commands[i][commands[i].find(" brings ") + 8: len(commands[i])]
                        save += init + "from " + var + " import " + libs
                        save += "\n"
                    elif commands[i].startswith(friendname + " ask to " + protagonistname + " about "):
                        var = commands[i][len(friendname + " ask to " + protagonistname + " about "):len(commands[i])]
                        save += init + friendname + " = input(\"" + var + "\")"
                        save += "\n"
                    elif commands[i].startswith(friendname + " ask to " + protagonistname):
                        save += init + friendname + " = input()"
                        save += "\n"
                    elif commands[i].startswith("End"):
                        if len(commands[i]) <= 3:
                            save += init + "return 0"
                            save += "\n"
                            init = init[:-4]
                        else:
                            var = commands[i][4:len(commands[i])]
                            save += init + "return " + var
                            save += "\n"
                            init = init[:-4]
                    else:
                        for u in range(len(variables)):
                            if commands[i].startswith(variables[u] + " is "):
                                var = commands[i][len(variables[u] + " is "):len(commands[i])]
                                save += init + variables[u] + " = " + var
                                save += "\n"
            save += "main()"
            save += "\n"

            if pythonexport:
                exp = open(savepath + ".py", "w")
                exp.write(save)
                exp.close()
            else:
                exp = open("temp.py", "w")
                exp.write(save)
                exp.close()
                PyInstaller.__main__.run([
                    "temp.py",
                    '--onefile',
                    '-n',
                    savepath
                ])
                shutil.rmtree("build/", ignore_errors=True)
                shutil.copyfile("dist/" + savepath, savepath)
                shutil.rmtree("dist/", ignore_errors=True)
                shutil.rmtree("__pycache__/", ignore_errors=True)
                os.remove(savepath + ".spec")
                os.remove("temp.py")

        else:
            print("not hystory file")
    else:
        print ("the file does not exist")