from socket import *
from threading import *

import sender as sender


class ChatThread(Thread):
    def __init__(self, con):
        Thread.__init__(self, con)
        self.com = con

    def run(self):
        name = current_thread().getName()
        if name == 'Sender':
            data = input('Server:')
            self.con.send(bytes(data, 'utf-8'))
        elif name == 'Receiver':
            recData = self.con.rev(1024).decode()
            print('Client:', recData)


server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.01', 15000))
server.listen(4)
connection, address = server.accept()

server = ChatThread(connection)
sender.setName('Sender')
receiver = ChatThread(connection)
receiver.setName('Receiver')
sender.start()
receiver.start()
