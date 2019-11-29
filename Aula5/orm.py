#!/usr/bin/env python3

class Banco():
    def __init__(self,conexao,cursor):
        try:
            self.conexao = conexao
            self.cursor = cursor
        except Exception as e:
            raise Exception(e)

    def __del__(self):
        self.cursor.close()
        self.conexao.close()
    
    #Criando Crud - Create, read, update, delete
    def inserir(self, nome, conteudo):
        self.cursor.execute(f"INSERT into scripts(nome,conteudo) values('{nome}','{conteudo}')")
        self.conexao.commit()
        print('Inserido com sucesso')

    def atualizar(self, tabela, coluna, valor, coluna_old, valor_old):
        self.cursor.execute(f'UPDATE {tabela} set {coluna} = {valor} WHERE {coluna_old} = {valor_old}')
        self.conexao.commit()
        print('Atualizado com sucesso')

    def delete(self, tabela, coluna, valor):
        self.cursor.execute(f"DELETE FROM {tabela} WHERE {coluna} = '{valor}'")
        self.conexao.commit()
        print('Deletado com sucesso')

    def seleciona_todos(self, tabela):
        self.cursor.execute(f"SELECT * FROM {tabela}")
        return self.cursor.fetchall()

    def seleciona_primeiro(self, tabela):
        self.cursor.execute(f"SELECT * FROM {tabela}")
        return self.cursor.fetchone()
