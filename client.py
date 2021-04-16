import socket

def client_connect():

    # establish connection
    s = socket.socket()
    s.connect(("localhost", 5000))
    filetosend = open("att2.zip", "rb")
    data = filetosend.read(1024)

    while data:
        print("Sending...")
        s.send(data)
        data = filetosend.read(1024)
    
    filetosend.close()
    s.send(b"DONE")
    print("Finished Sending!")
    s.shutdown(2)
    s.close()

if __name__ == "__main__":
    client_connect()