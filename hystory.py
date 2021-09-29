import os
import sys
from sys import exit

# Compiler 
# (Transform to py)

init = ""
save = ""
protagonistname = ""
friendname = ""

if len(sys.argv) > 1:
    path = sys.argv[1]
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
                if commands[i].lower().startswith("protagonist is "):
                    func = commands[i][len("protagonist is "):len(commands[i])]
                    protagonistname = func
                if commands[i].lower().startswith("friend is "):
                    func = commands[i][len("friend is "):len(commands[i])]
                    friendname = func
                if commands[i].lower().startswith("new history: "):
                    func = commands[i][len("New History: "):len(commands[i])]
                    save += init + "def " + func + "():"
                    save += "\n"
                    init += "    "
                if commands[i].lower().startswith("principal"):
                    save += init + "def main():"
                    save += "\n"
                    init += "    "
                elif commands[i].lower().startswith("narrador says "):
                    newlines = commands[i].split("\n")
                    for j in range(len(newlines)):
                        if newlines[j].lower().startswith("narrador says "):
                            newlines[j]= newlines[j][14:len(newlines[j])]
                        save += init + "# " + newlines[j]
                        save += "\n"
                elif commands[i].startswith("Hi "):
                    var = commands[i][3:len(commands[i])]
                    save += init + var + " = None"
                    save += "\n"
                elif commands[i].startswith(protagonistname + " says "):
                    var = commands[i][len(protagonistname + " says "):len(commands[i])]
                    save += init + "print(\"" + var + "\")"
                    save += "\n"
                elif commands[i].startswith("I say that: "):
                    var = commands[i][12:len(commands[i])]
                    save += init + "print(" + var + ")"
                    save += "\n"
                elif commands[i].startswith(friendname + " ask to " + protagonistname + " about "):
                    var = commands[i][len(friendname + " ask to " + protagonistname + " about "):len(commands[i])]
                    save += init + friendname + " = input(\"" + var + "\")"
                    save += "\n"
                elif commands[i].startswith(friendname + " ask to " + protagonistname):
                    save += init + friendname + " = input()"
                    save += "\n"
                    
                if commands[i].startswith("End"):
                    if len(commands[i]) <= 3:
                        save += init + "return 0"
                        save += "\n"
                        init = init[:-4]
                    else:
                        var = commands[i][4:len(commands[i])]
                        save += init + "return " + var
                        save += "\n"
                        init = init[:-4]
                #if "New History:" in commands[i]:
                #    name = commands[i].split(" ")
                #    print("New History is ")
            save += "main()"
            save += "\n"
            exp = open("export.py", "w")
            exp.write(save)
            exp.close()
        else:
            print("not hystory file")
    else:
        print ("the file does not exist")