import log_manager
logger = log_manager.get(__name__)
import subprocess
from threading import Thread
import time
import sys


DEBUG_TARGET = "client"
DEBUG_TARGET = "server"


match DEBUG_TARGET:
    case "client":
        # Use the current Python interpreter executable
        python_executable = sys.executable

        # start server
        # note, because defaults to localhost, don't need to pass in -H argument
        cmd = [python_executable, "visionflow/server.py"]
        # server = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        server = subprocess.Popen(cmd)
        # ensure the server had time to start
        pause = input("Type something to move on")
        # time.sleep(.5)

        import visionflow.client

    case "server":
        # Use the current Python interpreter executable
        python_executable = sys.executable
        # start server
        def start_server():
            import visionflow.server
        
        thread = Thread(target = start_server, args=[], daemon=False)
        thread.start()
        logger.info("")
        # time.sleep(5)
        wait = input("hold")
        logger.info(f"About to initiate client.py")
        # note, because defaults to localhost, don't need to pass in -H argument
        cmd = [python_executable, "visionflow/client.py"]
        # server = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        server = subprocess.Popen(cmd)
        # ensure the server had time to start
        # pause = input("Type something to move on")

