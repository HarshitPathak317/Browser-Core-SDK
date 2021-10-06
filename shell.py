import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


import basic

while True:
		text = input('basic > ')
		result, error = basic.run('<stdin>', text)

		if error: print(error.as_string())
		else: print(result)
