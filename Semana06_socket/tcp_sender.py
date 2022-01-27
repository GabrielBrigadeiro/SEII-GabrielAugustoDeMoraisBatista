import socket #importando biblioteca socket
import sys #importando biblioteca sys

TCP_IP = "127.0.0.1" #definindo IP do servidor TCP
FILE_PORT = 5005 #definindo porta de arquivo
DATA_PORT = 5006 #definindo porta de dados
buf = 1024 #definindo tamanho do buffer
file_name = sys.argv[1] #definindo nome do arquivo à partir de entrada no terminal


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #iniciando um socket
    sock.connect((TCP_IP, FILE_PORT)) #fazendo conexão com o host
    sock.send(file_name) #enviando o nome do arquivo
    sock.close() #encerrando o socket iniciado na linha 12

    print("Sending %s ..." % file_name) #imprimindo o que está enviando o socket com nome definido na linha 8

    f = open(file_name, "rb") #abrindo arquivo para leitura em binário
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #iniciando um socket
    sock.connect((TCP_IP, DATA_PORT)) #fazendo conexão com o host
    data = f.read() #lendo os dados do arquivo
    sock.send(data) #enviando dados do arquivo

finally:
    sock.close() #encerrando a conexão
    f.close() #fechando o arquivo