import os
import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QFileDialog
from PySide6.QtCore import Qt
import main



class MyWidget(QtWidgets.QWidget):

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


    def openScript(self, pyPath):
        app = QtWidgets.QApplication([])
        widget = MyWidget()
        widget.show()

        with open(pyPath, 'r', encoding='utf-8') as f:
            content = f.read()
        self.editor.setPlainText(content)

        try:
            with open(pyPath, 'r', encoding='utf-8') as f:
                content = f.read()
                self.editor.setPlainText(content)
        except Exception as e:
            print(f"Error: {e}")

        sys.exit(app.exec())