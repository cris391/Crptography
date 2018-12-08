#!/usr/bin/env python3
"""Server for multithreaded (asynchronous) chat application."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

"""For AES encryption and Symmetric key encryption"""
import nacl.secret
import nacl.utils
from nacl.public import PrivateKey, SealedBox, PublicKey

"""Creation of general key"""
gk = key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)

def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        #receiving the public key from recent user
        pk = client.recv(BUFSIZ)
        
        #creating sealed box and sending key to client
        box = SealedBox(PublicKey(pk))
        encryptedKey = box.encrypt(gk)
        client.send(bytes(encryptedKey))

        print("%s:%s has connected." % client_address)
        greeting = "Greetings from the cave! Now type your name and press enter!".encode(encoding='utf-8')
        encryptedGreet = nacl.secret.SecretBox(gk).encrypt(greeting)
        client.send(bytes(encryptedGreet))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    name = nacl.secret.SecretBox(gk).decrypt(client.recv(BUFSIZ))
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(nacl.secret.SecretBox(gk).encrypt(welcome))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = nacl.secret.SecretBox(gk).decrypt(client.recv(BUFSIZ))
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break


def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""

    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

        
clients = {}
addresses = {}

HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()