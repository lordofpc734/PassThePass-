import subprocess
import elevate
elevate.elevate()
subprocess.run(["powershell", "restart-service -name \"cbdhsvc*\" -force",], capture_output=True)