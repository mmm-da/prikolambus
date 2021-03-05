import socket
import time
import os

port = int(os.environ["POSTGRES_PORT"])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Ждем пока поднимется postgres')
while True:
    try:
        s.connect(('database', port))
        s.close()
        break
    except socket.error as ex:
        time.sleep(0.1)