import socket

s = socket.socket()
s.connect(("localhost", 5000))
filetosend = open("attachments.zip", "rb")
data = filetosend.read(1024)
while data:
    print("Sending...")
    s.send(data)
    data = filetosend.read(1024)
filetosend.close()
s.send(b"DONE")
print("Done Sending.")
print(s.recv(1024))
s.shutdown(2)
s.close()