import os
from editor import MyWidget
import main

def makeMain(path):
    print("making file")

    pyPath = os.path.join(path, "main.py")
    starter_code = """\
# This is the main file for your project
# You must ALWAYS have a main.py or re-route the start file

def main():
    print("Hello, world!")

main()
        """
    
    with open(pyPath, 'w') as f:
        f.write(starter_code)
    print("created succesfuly!")

    MyWidget().openScript(pyPath)
    if (MyWidget().openScript(pyPath) == True): {
        main.sys.exit()
    }