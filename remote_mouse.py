# the one and only function call starts the whole integrated remote
# mouse app

import pywhatkit
import pyautogui
import flask

pywhatkit.start_server()
# get this pc local ip and look it in a browser at port 8000 by
# default