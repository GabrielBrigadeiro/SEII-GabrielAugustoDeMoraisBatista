import socket #importando biblioteca socket

TCP_IP = "127.0.0.1" #definindo IP do servidor TCP
FILE_PORT = 5005 #definindo porta de arquivo
DATA_PORT = 5006 #definindo porta de dados
timeout = 3 #definindo tempo de esgotamento da solicitação
buf = 1024 #definindo tamanho do buffer


sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #iniciando um socket
sock_f.bind((TCP_IP, FILE_PORT)) #fazendo a associação do socket com o localhost
sock_f.listen(1) #ouvindo solicitação de conexões

sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #iniciando um socket
sock_d.bind((TCP_IP, DATA_PORT)) #fazendo a associação do socket com o localhost
sock_d.listen(1) #ouvindo solicitação de conexões


while True:
    conn, addr = sock_f.accept() #aceitando conexão do sender
    data = conn.recv(buf) #recebendo nome do arquivo
    if data:
        print("File name:", data) #imprimindo nome do arquivo
        file_name = data.strip() #removendo espaços

    f = open(file_name, 'wb') #abrindo arquivo para escrita em binário

    conn, addr = sock_d.accept() #aceitando conexão com o sender
    while True:
        data = conn.recv(buf) #recebendo dados
        if not data: #caso não existam dados, interrompe
            break
        f.write(data) #escrevendo dados no arquivo

    print("%s Finish!" % file_name) #imprimindo que o processo de escrita foi finalizado
    f.close() #fechando o arquivo