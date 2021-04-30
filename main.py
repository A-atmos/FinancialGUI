from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow, QDialog
import datetime as dt


import UI
import core

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UI.Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    
    MainWindow = QMainWindow()
    ui = UI.Ui_MainWindow()
    ui.setupUi(MainWindow, app)
    MainWindow.show()
    print(core.get_file())
    core.get_file()
    engine = core.Calculations(core.not_df)

    # engine.income_data(ui.inSource.text(), int(ui.inAmount.text()), ui.inDate.text() )
    # engine.expense_data(ui.outSource.text(), int(ui.outAmount.text()), ui.outDate.text() )
    # ui.saveButton.clicked.connect(Integrate().press_save)
    # ui.saveButton_2.clicked.connect(Integrate().press_save_2)
    ui.show_balance()
    sys.exit(app.exec_())