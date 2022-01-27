# importando módulos

import socket
import threading
import time

"""
Como o próprio nome do arquivo indica, este código trata-se do cliente do chat implementado no vídeo,
que é chamado pelo servidor quando recebe uma nova mensagem.
Nas linhas 14 até 17 são fornecidos os dados do servidor, como ip, número de porta, ADDR como uma tupla
com informações de IP e porta, e o formato da mensagem.
"""

PORT = 5050
FORMATO = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

"""
Nas linhas 25 e 26 é iniciado o socket, especificando sua classe e o tipo de E/S,
e faz a conexão do socket com o servidor.
"""

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

"""
A função handle_mensagens lida o com o gerenciamento das mensagens enviadas pelo servidor,
recebendo-as na variável msg, e separando a mensagem nos sinais de "=", para que possam ser
imprimidos separadamente o nome do cliente e a mensagem destinada a ele.
"""

def handle_mensagens():
    while(True):
        msg = client.recv(1024).decode()
        mensagem_splitada = msg.split("=")
        print(mensagem_splitada[1] + ": " + mensagem_splitada[2])

"""
A função enviar realiza o envio do dado (nome ou mensagem) ao servidor.
"""

def enviar(mensagem):
    client.send(mensagem.encode(FORMATO))

"""
A função iniciar_envio chama as funções enviar_nome e enviar_mensagem, que fazem o papel
de receber a entrada do teclado para o nome do cliente e a mensagem que deseja enviar, respectivamente
e chamar a função enviar para passar o nome e a mensagem que receberam do teclado para 
o servidor.
"""

def enviar_mensagem():
    mensagem = input()
    enviar("msg=" + mensagem)

def enviar_nome():
    nome = input('Digite seu nome: ')
    enviar("nome=" + nome)

def iniciar_envio():
    enviar_nome()
    enviar_mensagem()

"""
A função iniciar, tem como tarefa iniciar as threads necessárias para o funcionamento
do chat, sendo passado para as threads as funções handle_mensagens e iniciar_envio,
para que possam rodar junto com outras partes do código
"""

def iniciar():
    thread1 = threading.Thread(target=handle_mensagens)
    thread2 = threading.Thread(target=iniciar_envio)
    thread1.start()
    thread2.start()

iniciar()