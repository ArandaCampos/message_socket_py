import threading
import socket
import signal
from time import sleep

server = 'localhost'
port = 7777
address = (server, port)
CONNECT_SIGNAL = threading.Event()

def main():
    global CONNECT_SIGNAL

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(address)
        CONNECT_SIGNAL.set()
    except:
        return print('\nNão foi possível conectar-se ao servidor')

    print(f'\nSeja bem-vindo(a)\n')
    username = input('Insira seu usuário: ')
    print('\n')

    client.send(f'{username} entrou'.encode('utf-8'))

    thread1 = threading.Thread(target=recv_msg, args=[client, username])
    thread1.setDaemon(True)
    thread1.start()

    thread2 = threading.Thread(target=send_msg,args=[client, username])
    thread2.setDaemon(True)
    thread2.start()

    while CONNECT_SIGNAL.is_set():
        pass

    send_msg_client_exit(client, username)
    client.close()

def recv_msg(client, username):
    global CONNECT_SIGNAL

    while CONNECT_SIGNAL.is_set():
        try:
            msg = client.recv(2048).decode('utf-8')
            if msg != '':
                print(f'\r{msg}\nVocê: ', end='')
            else:
                CONNECT_SIGNAL.clear()
        except:
            print('\nVocê está DESCONECTADO!')
            CONNECT_SIGNAL.clear()

def send_msg(client, username):
    global CONNECT_SIGNAL

    while CONNECT_SIGNAL.is_set():
        try:
            msg = input('Você: ')
            if msg == 'quit()':
                CONNECT_SIGNAL.clear()
            else:
                client.send(f'{username}: {msg}'.encode('utf-8'))
        except:
            CONNECT_SIGNAL.clear()

def send_msg_client_exit(client, username):
    client.send(f'\n{username} saiu da sala!\n'.encode('utf-8'))

main()
