# import scripts externally, in same folder
import sys
import os

import Grasshopper

path=os.path.dirname(Grasshopper.Instances.ActiveCanvas.Document.FilePath)
sys.path.append(path)
