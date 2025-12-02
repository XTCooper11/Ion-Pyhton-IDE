import sys
import os
from datetime import datetime
import json
from PySide6 import QtWidgets
from PySide6.QtWidgets import QPushButton, QFileDialog, QInputDialog
from functools import partial
import fileM

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ion IDE")
        self.layout = QtWidgets.QVBoxLayout(self)

        self.label = QtWidgets.QLabel("Welcome to Ion IDE!", self)
        self.label.setStyleSheet("font-size: 34px; font-weight: bold;")
        self.layout.addWidget(self.label)

        self.button1 = QPushButton(self)
        self.button1.setGeometry(40, 40, 100, 50)
        self.button1.setText("Open Folder")
        self.button1.clicked.connect(partial(self.clicked_btn, 'OpenFolder'))
        self.layout.addWidget(self.button1)

        self.button1 = QPushButton(self)
        self.button1.setGeometry(40, 40, 100, 50)
        self.button1.setText("New Project")
        self.button1.clicked.connect(partial(self.clicked_btn, 'NewProject'))
        self.layout.addWidget(self.button1)

    def clicked_btn(self, action):
        if action == 'OpenFolder':
            print("Open Folder button clicked")
            of = QFileDialog(self, "Select Folder")
            of.setFileMode(QFileDialog.FileMode.Directory)
            of.setDirectory("projects")
            if of.exec():
                folder_path = of.selectedFiles()[0]
                print(f"Selected folder: {folder_path}")


        elif action == 'NewProject':
            print("New Project button clicked")
            pop, ok = QInputDialog.getText(None, "Enter Project Name", "Name: ")

            if ok and pop:
                TOC = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                dir = os.path.join('projects', pop)
                os.makedirs(dir, exist_ok=True)

                data = {
                "nameP": pop,
                "dateCreated": TOC,
                "entry": 'main.py'
                 }
                config_path = os.path.join('projects', "configION.json")
                with open(config_path, 'w') as f:
                    json.dump(data, f, indent=4)
                    print("Project made!")

                    path = os.path.dirname(config_path)
                    fileM.makeMain(path)




if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())