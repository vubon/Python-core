import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'codervubon.com'

def pscan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False


for i in range(1,26):
    if pscan(i):
        print('Port', i, 'is open')
    else:
        print('Port', i, 'is close')
