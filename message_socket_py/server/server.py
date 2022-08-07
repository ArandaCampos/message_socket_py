import threading
import signal
import socket
import sys

server = 'localhost'
port = 7777
address = (server, port)
clients = []
ONLINE = threading.Event()

def main():
    global ONLINE
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind(address)
        server.listen()
        ONLINE.set()

        print(f'\nServidor conectado!\nOuvindo porta {port} ...\n')
    except:
        return print(f'\nFalha ao iniciar o servidor na porta {port}\n\n')

    while True:
        client, addr = server.accept()
        print(f'Entrou: {addr}')
        clients.append(client)

        thr = threading.Thread(target=recv_msg, args=[client])
        thr.setDaemon(True)
        thr.start()

    while ONLINE.is_set():
        pass

def recv_msg(client):
    while True:
        try:
            msg = client.recv(2048)
            broadcast(msg, client)
        except:
            client.send('Desconectado!'.encode('utf-8'))
            remove_cliente(client)
            break

def broadcast(msg, client):
    for user in clients:
        if not user == client:
            try:
                user.send(msg)
            except:
                remove_cliente(user)

def remove_cliente(client):
    if client in clients:
        clients.remove(client)

def close_server(signum, frame):
    global ONLINE

    ONLINE.clear()
    print('\rFechando servidor ...')
    exit(0)

signal.signal(signal.SIGINT, close_server)

main()
