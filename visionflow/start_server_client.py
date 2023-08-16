import subprocess
import time
import sys


DEBUG_TARGET = "server"
DEBUG_TARGET = "client"


match DEBUG_TARGET:
    case "client":
        # Use the current Python interpreter executable
        python_executable = sys.executable

        # start server
        cmd = [python_executable, "visionflow/server.py"]
        # server = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        server = subprocess.Popen(cmd)
        # ensure the server had time to start
        pause = input("Type something to move on")
        time.sleep(.5)

        import visionflow.client

    case "server":
        # Use the current Python interpreter executable
        python_executable = sys.executable
        # start server
        import visionflow.server

        time.sleep(5)
        cmd = [python_executable, "visionflow/client.py"]
        # server = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        server = subprocess.Popen(cmd)
        # ensure the server had time to start
        # pause = input("Type something to move on")

