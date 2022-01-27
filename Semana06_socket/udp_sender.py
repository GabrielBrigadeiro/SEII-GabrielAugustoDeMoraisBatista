import socket #importando biblioteca socket
import time #importando biblioteca time
import sys #importando biblioteca sys

UDP_IP = "127.0.0.1" #definindo IP do servidor UDP
UDP_PORT = 5005 #definindo porta do servidor UDP
buf = 1024 #definindo tamanho do buffer 
file_name = sys.argv[1] #definindo nome do arquivo à partir de entrada no terminal


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #criando um servidor UDP para socket
sock.sendto(file_name, (UDP_IP, UDP_PORT)) #enviando o nome do arquivo e passando IP e porta
print("Sending %s ..." % file_name) #imprmindo qual arquivo está sendo enviado

f = open(file_name, "r") #abrindo arquivo para leitura
data = f.read(buf) #lendo os dados do arquivo de acordo com o tamanho do buffer
while(data):
    if(sock.sendto(data, (UDP_IP, UDP_PORT))): #enviando os dados para IP e porta passados
        data = f.read(buf) #lendo o arquivo de pouco em pouco, até o final
        time.sleep(0.02) #dando um pequeno tempo para o receiver salvar o arquivo

sock.close() #encerrando conexão
f.close() #fechando o arquivo