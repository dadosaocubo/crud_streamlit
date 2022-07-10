# carregando as bibliotecas
import psycopg2

# conexão com o banco de dados PostgreSQL
con = psycopg2.connect(host='localhost',
                       database='crud',
                       user='postgres',
                       password='postgres')
# criando o cursos da conexão para acessar o banco
cur = con.cursor()
