
import socket


def server_connect():
    print("Starting socket")
    s = socket.socket()
    s.bind(("localhost", 5000))
    s.listen(5)
    c,a = s.accept()
    print(c,a)
    filetodown = open("scripts.zip", "wb")
    print("Opening Script...")
    while True:
        data = c.recv(1024)
        if data == b"DONE":
            print("Done Receiving.")
            break
        filetodown.write(data)
    filetodown.close()
    c.send("Thank you for connecting.")
    c.shutdown(2)
    c.close()
    s.close()

if __name__ == "__main__":
    server_connect()