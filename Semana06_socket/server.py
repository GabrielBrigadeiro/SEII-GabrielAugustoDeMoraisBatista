# importando módulos

import socket
import threading
import time

"""
Como o próprio nome do arquivo indica, este código trata-se do servidor do chat implementado no vídeo,
que trabalha de maneira que o servidor é quem chama o cliente quando existe alguma mensagem nova para ele.
Nas linhas 14 até 17 são fornecidos os dados para o servidor, como ip, número de porta, ADDR como uma tupla
com informações de IP e porta, e o formato da mensagem.
"""

SERVER_IP = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER_IP, PORT)
FORMATO = 'utf-8'

"""
Nas linhas 25 e 26 é iniciado o socket, especificando sua classe e o tipo de E/S,
e faz a conexão do socket com o localhost. Nas linhas 28 e 29, são definidas listas vazias,
que receberão as conexões e mensagens.
"""

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

conexoes = []
mensagens = []

"""
A função enviar_mensagem_individual, como seu nome sugere, envia uma mensagem para apenas uma pessoa,
e trabalha recebendo o parâmetro conexao, que entra em um loop para ler as mensagens de envio, e poder enviá-las,
enquanto que a função enviar_mensagem_todos, envia a mensagem para todos os usuários, se utilizando de um loop para
chamar a função enviar_mensagem_individual para todas as conexões necessárias.
"""

def enviar_mensagem_individual(conexao):
    print(f"[ENVIANDO] Enviando mensagens para {conexao['addr']}")
    for i in range(conexao['last'], len(mensagens)):
        mensagem_de_envio = "msg=" + mensagens[i]
        conexao['conn'].send(mensagem_de_envio.encode())
        conexao['last'] = i + 1
        time.sleep(0.2)

def enviar_mensagem_todos():
    global conexoes
    for conexao in conexoes:
        enviar_mensagem_individual(conexao)

"""
1 vez que o cliente entrar, vai mandar o nome:
nome=.....
E as mensagens vem:
msg=
"""

"""
Função para manipular os clientes que se conectam. Nela é definido o tamanho máximo da mensagem e especificado seu formato,
e a mensagem é separada, caso ela comece com "nome=", significa que é um nome, e a separação ocorre de maneira que o nome do cliente 
é separado e salvo na variável nome, e é criado então o mapa da conexão, com os dados necessários para envio da mensagem ao cliente,
que é enviada em seguida adicionando o mapa da conexão ao fim da lista de conexões e enviando por meio da função enviar_mensagem_individual. 
Caso a mensagem comece com "msg=", significa que se trata de uma mensagem, e a mesma é separada de maneira que possa ser salva na variável,
mensagem, juntamente com o nome do cliente e adicionada à lista de mensagens, e no fim, é chamada a função enviar_mensagem_todos para que
seja enviada a mais de um cliente de uma vez.
"""

def handle_clientes(conn, addr):
    print(f"[NOVA CONEXAO] Um novo usuario se conectou pelo endereço {addr}")
    global conexoes
    global mensagens
    nome = False

    while(True):
        msg = conn.recv(1024).decode(FORMATO)
        if(msg):
            if(msg.startswith("nome=")):
                mensagem_separada = msg.split("=")
                nome = mensagem_separada[1]
                mapa_da_conexao = {
                    "conn": conn,
                    "addr": addr,
                    "nome": nome,
                    "last": 0
                }
                conexoes.append(mapa_da_conexao)
                enviar_mensagem_individual(mapa_da_conexao)
            elif(msg.startswith("msg=")):
                mensagem_separada = msg.split("=")
                mensagem = nome + "=" + mensagem_separada[1]
                mensagens.append(mensagem)
                enviar_mensagem_todos()


"""
A função start inicia o processo de "ouvir" do socket, trabalhando de maneira que possa aceitar a entrada
de um cliente e registrar sua conexão e endereço por meio da chamada server.accept(), após isso, ela cria e inicia uma thread para 
enviar mensagens para o novo cliente, envia conn e addr para a função handle_clientes e espera por novas conexões.
"""

def start():
    print("[INICIANDO] Iniciando Socket")
    server.listen()
    while(True):
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_clientes, args=(conn, addr))
        thread.start()

start()