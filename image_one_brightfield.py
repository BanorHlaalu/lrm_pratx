'''image_cells.py
  
Protocol for designed for long duration brightfield and beta imaging of living cells

The protocol loops numberCaptures times
During each loop it:
	captures 1 brightfield image
	captures 1 beta image of betaSecondsPerImage total duration time

Severin Lustenberger
Adapted from:
Justin Klein
Stanford University
Department of Radiation Oncology
2018
'''
from lrm import LRM
from datetime import datetime

# File-related Settings
baseDir = './output/'
experimentDir='one_brightfield'
experimentDataPath = baseDir + experimentDir
timestamp = datetime.strftime(datetime.today(),format="%y%m%d_%H%M%S")
bfFileName = f"{timestamp}_bf"

# Initialize LRM class
LRM = LRM()
  
# Get exposure settings for brightfield images and lock them in
bfGain,bfShutter = LRM.get_brightfield_exposure()

# Override brightfield shutter duration if so desired
bfShutter=1000

# Announce
print(f"Capturing single brightfield image. Shutter = {str(bfShutter)} ms")

# Capture brightfield 
LRM.capture_brightfield(fullPath=experimentDataPath,
						filePrefix=bfFileName,
						numberImages=5,
						analogGain=bfGain,
						exposureDurationUs=bfShutter)
LRM.preview_last(True)
