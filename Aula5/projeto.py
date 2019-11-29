#!/usr/bin/python3

#Trabalhar com mongo
import pymongo
import threading
import chat

try:
    client = pymongo.MongoClient(host'172.16.0.77')
    db = client['chat']
except Exception as e:
    print(e)

if __name__ == "__main__":
    usuario = input('Digite um apelido: ')
    try:
        paralelo = threading.Thread(target=chat.lerMensagem) #Método a definir
        paralelo.start
    except Exception as e:
        print(e)
    
    while paralelo.isAlive:
        chat.cadastrar(usuario,mensagem)
