# import ctypes
# user32 = ctypes.windll.user32

# print(user32.GetSystemMetrics(1), user32.GetSystemMetrics(0))

# from screeninfo import get_monitors
# for m in get_monitors():
#     print(str(m))

from PyQt5 import QtWidgets
import sys

MyApp = QtWidgets.QApplication(sys.argv)
V = MyApp.desktop().screenGeometry()
h = V.height()
w = V.width()
print("The screen resolution (width X height) is the following:")
print(str(w) + "X" + str(h))