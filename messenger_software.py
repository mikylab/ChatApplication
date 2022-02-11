from tkinter import *
import socket
import select
import sys
from thread import *



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


if len(sys.argv) != 3: 
    print ("Correct usage: script, IP address, port number")
    exit()

IP_address = str(sys.argv[1])

server.bind((IP_address, 3000))

server.listen(100) 
  
list_of_clients = []

#def clientthread(conn, addr): 
    conn.send("Welcome to this chatroom!") 
  
    while True: 
            try: 
                message = conn.recv(2048) 
                if message: 
                    print ("<" + addr[0] + "> " + message) 
                    message_to_send = "<" + addr[0] + "> " + message 
                    broadcast(message_to_send, conn) 
  
                else: 
                    remove(conn) 
  
            except: 
                continue
def broadcast(message, connection): 
    for clients in list_of_clients: 
        if clients!=connection: 
            try: 
                clients.send(message) 
            except: 
                clients.close() 
                remove(clients) 

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

        

    def create_widgets(self):
        # Label 
        self.display = Label(self,
               text = "IP Address: ",
               height = 2,
               width = 35,
             )
        self.display.grid(row = 0,
                     column = 0,
                     sticky = NSEW,
                     padx = 5,
                     pady = 5)

        self.address = Text(self,
                          height=2,
                          width=35,
                          borderwidth=2
                          )

        self.address.grid(row = 0,
                        column = 1,
                        sticky = NSEW,
                        padx = 5,
                        pady = 5)
        
        self.message = Text(self,
                          height=10,
                          width=35,
                          borderwidth=2
                          )

        self.message.grid(row = 1,
                        column = 0,
                        sticky = NSEW,
                        padx = 5,
                        pady = 5)
        

        self.recieve = Label(self,
                        text="test",   
                        height=10,
                        width=35,
                        borderwidth=2
                        )

        self.recieve.grid(row = 1,
                        column = 1,
                        sticky = NSEW,
                        padx = 5,
                        pady = 5)
    
 
        
        Button(self,
               text="Send",
               height = 3,
               width = 35,
               command = self.send_button
               ).grid(row = 2,
                      column = 0,
                      sticky = NSEW)

    def word_count(self):
        message = self.message.get("1.0",END)
        length=len(message).split()
        print(length)
        
        
    def send_button(self):
        address = self.address.get("1.0",END)
        print(address)

        message = self.message.get("1.0",END)
        print(message)


root = Tk()
root.title("Chat System")
app = Application(root)
root.mainloop()





