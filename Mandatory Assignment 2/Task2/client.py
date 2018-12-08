#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter

"""For AES encryption and Symmetric key encryption"""
import nacl.secret
import nacl.utils
from nacl.public import PrivateKey, SealedBox

#Creation of RSA Keys
sk = PrivateKey.generate()
pk = sk.public_key

def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = nacl.secret.SecretBox(gk).decrypt(client_socket.recv(BUFSIZ))
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(nacl.secret.SecretBox(gk).encrypt(msg)))
    if msg == "{quit}":
        client_socket.close()
        top.quit()

def encryption():
    """Handles receiving of keys and inititalize encryption process"""

    #Sending key to server
    print("Sending public key to server")
    client_socket.send(bytes(pk))

    #Receiving symmetric key
    symmKey = client_socket.recv(BUFSIZ)
    gk = SealedBox(sk).decrypt(symmKey)

    return gk



def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()

top = tkinter.Tk()
top.title("Chatter")

messages_frame = tkinter.Frame(top)
my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("Type your messages here.")
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

#----Now comes the sockets part----
HOST = input('Enter host: ')
PORT = input('Enter port: ')
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

#Starting the encryption process
gk = encryption()

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  # Starts GUI execution.