from Rosehip.os import OS;from os import popen
def start():popen('sudo apt-get update && sudo apt install python3-pip && pip3 install requests opencv-python selenium');OS().run()
