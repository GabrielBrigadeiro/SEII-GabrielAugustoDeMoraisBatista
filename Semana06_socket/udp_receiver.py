import socket #importando biblioteca socket
import select #importando biblioteca select

UDP_IP = "127.0.0.1" #definindo IP do servidor UDP
IN_PORT = 5005 #definindo porta do servidor UDP
timeout = 3 #definindo tempo de esgotamento da solicitação


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #criando um servidor UDP para socket
sock.bind((UDP_IP, IN_PORT)) #fazendo a associação do socket com o localhost

while True:
    data, addr = sock.recvfrom(1024) #recebendo os dados do sender
    if data:
        print("File name:", data) #imprimindo o nome do arquivo
        file_name = data.strip() #retirando espaços

    f = open(file_name, 'wb') #abrindo arquivo para escrita em binário

    while True:
        ready = select.select([sock], [], [], timeout) #utilizando a função select para fazer a multiplexação de entrada e saída
        if ready[0]:
            data, addr = sock.recvfrom(1024) #recebendo os dados do socket
            f.write(data) #escrevendo os dados no arquivo
        else:
            print("%s Finish!" % file_name) #imprimindo que o processo de escrita foi finalizado
            f.close() #fechando o arquivo
            break