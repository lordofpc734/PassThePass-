import subprocess
import os
from time import sleep
import elevate
#elevate.elevate()
extns = ".safe"
filename_1 = "passcopy.csv"
filename_2 = filename_1 + extns
sleep(0.5)
os.rename(filename_1, filename_2)
#subprocess.run(["powershell", "restart-service -name \"cbdhsvc*\" -force",], capture_output=True)