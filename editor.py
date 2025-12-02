import os
import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QFileDialog
from PySide6.QtCore import Qt



class MyWidget(QtWidgets.QWidget):
   
    def openScript(pyPath):
        print("opening in editor")

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ion IDE")
        self.showMaximized()

        self.saveButton = QPushButton("Save")
        self.saveButton.setStyleSheet("background-color: #4CAF50; color: white;")

        self.openButton = QPushButton("Open")
        self.openButton.setStyleSheet("background-color: #4CAF50; color: white;")

        self.openSrcButton = QPushButton("Open Source")
        self.openSrcButton.setStyleSheet("background-color: #4CAF50; color: white;")


        def saveFile():
            print('saving')

        def openFile():
            print('opening')
        
        def openSrc():
            print("opening src")

        self.saveButton.clicked.connect(saveFile)
        self.openButton.clicked.connect(openFile)
        self.openSrcButton.clicked.connect(openSrc)

        self.editor = QTextEdit()





if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec())
