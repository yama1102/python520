#!/usr/bin/python3

import psycopg2
import MySQLdb

from orm import Banco

try:
    #conexao postgres
    con_psql = psycopg2.connect('host=localhost dbname=projeto user=admin password=4linux')
    cur = con_psql.cursor()

    banco_psql = Banco(con_psql,cur)

    #conexao com MySQL

    con_mysql = MySQLdb.connect(host='localhost',db='scripts',user='developer',passwd='4linux')
    cur_mysql = con_mysql.cursor()
    banco_mysql = Banco(con_mysql,cur_mysql)
except Exception as e:
    print(e)
    exit()

try:
    # banco_psql.inserir('Daniel','Programador Python')
    # print(banco_psql.seleciona_todos('scripts'))
    # print(banco_psql.seleciona_primeiro('scripts'))
    # banco_psql.delete('scripts','nome','Tsubasa') # se esistem mesmos valores, deleta todos os dados com este valor
    # print(banco_psql.seleciona_todos('scripts'))
    
    # banco_mysql.inserir('Daniel','Programador python')
    # banco_mysql.inserir('Tsubasa','Engenheiro')
    # banco_mysql.delete('scripts','nome','Daniel')
    print(banco_mysql.seleciona_todos('scripts'))

except Exception as e:
    # con_psql.rollback()
    con_mysql.rollback()
    print(e)

