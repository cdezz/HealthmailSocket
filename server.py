#!/usr/bin/env python3

import socket
import datetime
import logging

logging.basicConfig(filename='logging.log', level=logging.DEBUG)


def server_connect():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('192.168.1.10', 5000)
    ip, port = server_address
    print('starting up on {} port {}'.format(*server_address))
    logging.debug(f"starting up on {ip} port {port}")
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        
        try:
            logging.debug(f"connection from {client_address}")
            print('connection from', client_address)
            # Gonna name the zip file`the current time
            current_time = datetime.datetime.now().strftime("%H-%M-%S")
            filetodown = open(f"{current_time}.zip", "wb")
            logging.debug(f"{current_time}.zip created, waiting for data...")
            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(1024)
                print('received data')
                filetodown.write(data)
                if data:
                    print('sending data back to the client')
                else:
                    print('no data from', client_address)
                    logging.debug(f"Closing {current_time}.zip")
                    filetodown.close()

                    break

        finally:
            # Clean up the connection
            connection.close()

if __name__ == "__main__":
    server_connect()
