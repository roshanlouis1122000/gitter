import os
os.system("sudo apt-get update&&upgrade")
os.system("sudo apt-get install ruby-full")
os.system("sudo apt-get install python3-pip")
os.system("sudo apt-get install -y cargo")
os.system("sudo apt install snapd")
os.system("sudo apt install npm")
os.system("sudo apt install nodejs")
os.system("sudo apt install libcurl4-openssl-dev libssl-dev")
os.system("sudo apt-get install -y python-tk tk-dev libffi-dev libssl-dev pandoc \libgmp3-dev libzbar-dev tesseract-ocr xsel libpoppler-cpp-dev libmpc-dev \")
os.system("pip3 install google")
os.system("pip3 install beautifulsoup4")
myCmd = os.popen('pwd').read()
inputfile = "/gitter.py"
cmd = myCmd.rstrip("\n")
cmd = cmd + inputfile
command = "sudo ln -s " + cmd + " /usr/bin/gitter"
os.system(command)
myCmd = os.popen('sed -i -e "s/\r$//" gitter.py').read()
