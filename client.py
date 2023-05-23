from socket import *
from threading import *

class ChatThread(Thread):
    def __init__(self,con):
        Thread.__init__(self,con)
        self.com=con
    def run(self):
        name=current_thread().getName()
        while True:
            if name=='Sender':
                data=input('Server:')
            self.con.send(bytes(data,'utf-8'))
        elif name=='Reciever':
            recData=self.con.rev(1024).decode()
            print('Client:',recData)

client=socket()
client.connect(('127.0.0.1',15000))
server=ChatThread(client)
sender.setName('Sender')
receiver=ChatThread(client)
receiver.setName('Receiver')
sender.start()
receiver.start()