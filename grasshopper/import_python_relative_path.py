# import scripts externally, relative folder
import sys
import os

import Grasshopper

path=os.path.dirname(Grasshopper.Instances.ActiveCanvas.Document.FilePath)
parent_path=os.path.dirname(path)
sub_directory="src"
path=os.path.join(parent_path, sub_directory)
sys.path.append(path)