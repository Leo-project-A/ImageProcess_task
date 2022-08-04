## run: python JPGtoPNGconverter Pokedex\ newPok\  -> create new folder with converted images
import sys
import os
from PIL import Image

def run():
    print(f"run {__name__} with {len(sys.argv)} args")
    if len(sys.argv) == 3:
        #The path of the current dir for saving files - str
        curpath = os.path.dirname(__file__) + "\\"
        source = sys.argv[1]                    # should be str
        newDirectory = sys.argv[2]              # should be str
        try:
            os.makedirs(curpath + newDirectory)     # create new folder
            print(f"{newDirectory[:-1]} created succesfuly")
            loopDirectory(curpath + source, curpath + newDirectory)
        except OSError:
            print("folder already exists")
    else:
        print(f"{sys.argv[0]} requires 2 args to run")

def loopDirectory(source, newDirectory):
    for file in os.listdir(source):
        if file.endswith('.jpg'):
            try:
                img = Image.open(source + file)
                img.save(newDirectory + file[:-3] + 'png', 'png')          
            except:
                print("somthing went wrong")

if __name__ == "__main__":
    run()