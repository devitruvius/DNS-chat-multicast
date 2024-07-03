import json
import socket
import struct
import sys

def emissor(nome):
    # Configurações
    MULTICAST_GROUP = '224.3.29.71'
    MULTICAST_PORT = 5007

    # Criar socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    ttl = struct.pack('b', 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

    # Json
    msg = {
        'user': nome,
        'data': None
    }

    # Enviar mensagem
    print(f'Olá {nome}. Vamos iniciar o chat!')
    while True:
        msg['data'] = input('Digite uma mensagem: ')
        if msg['data'] == 'sair':
            break
        msg_json = json.dumps(msg)
        sock.sendto(msg_json.encode('utf-8'), (MULTICAST_GROUP, MULTICAST_PORT))

    sock.close()

def receptor(nome):
    # Configurações
    MULTICAST_GROUP = '224.3.29.71'
    MULTICAST_PORT = 5007

    # Criar socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', MULTICAST_PORT))

    # Grupo multicast
    group = socket.inet_aton(MULTICAST_GROUP)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    # Receber e exibir mensagens
    print(f'Olá, {nome}. Vamos começar o chat!')
    try:
        while True:
            data, addr = sock.recvfrom(1024)
            msg_json = data.decode('utf-8')
            msg = json.loads(msg_json)
            print(f'Mensagem de {msg["user"]}: {msg["data"]}')
            if msg['data'] == 'sair':
                break
    except KeyboardInterrupt:
        print("Chat encerrado pelo usuário.")
    finally:
        sock.close()

def main(tipo, nome):
    if tipo == 'receptor':
        receptor(nome)
    elif tipo == 'emissor':
        emissor(nome)
    else:
        print("Tipo inválido. Use 'emissor' ou 'receptor'.")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso: python script.py <tipo> <nome>")
        print("<tipo>: 'emissor' ou 'receptor'")
        print("<nome>: Nome do usuário")
    else:
        tipo = sys.argv[1]
        nome = sys.argv[2]
        main(tipo, nome)