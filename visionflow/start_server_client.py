import subprocess
import time

# start server
server = subprocess.Popen(["python", "./server.py"])

# ensure the server had time to start
time.sleep(2)

# start client
client = subprocess.Popen(["python", "./client.py"])

# get output from the client
stdout, stderr = client.communicate()

# print the client output
if stdout:
    print('STDOUT:{}'.format(stdout))
if stderr:
    print('STDERR:{}'.format(stderr))

# kill the server process once we're done
server.terminate()