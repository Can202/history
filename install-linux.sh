#!/bin/bash

if [ ! $(whoami) = "root" ]
then
    echo "Execute this script as root"
    exit
fi

echo "Installing hyst-compiler"

mkdir -p /opt/
mkdir -p /opt/hyst-compiler/

curl -L https://raw.githubusercontent.com/Can202/hyst-compiler/0.0.1/hystory.py > "/opt/hyst-compiler/hyst-compiler.py"
if [ -f "/usr/bin/pip3" ]
then
    echo "pip3 installed"
    pip3 install pyinstaller
else
    echo "install pip3"
    exit
fi
if [ -f "/usr/bin/python3" ]
then
    echo "Python3 installed"
    echo "#!/bin/bash
ARGS=\"\$1 \$2 \$3 \$4 \$5 \$6 \$7 \$8 \$9\"
python3 /opt/hyst-compiler/hyst-compiler.py \$ARGS" > /usr/local/bin/hyst-compiler
    chmod a+x /usr/local/bin/hyst-compiler
else
    echo "install python3"
    exit
fi