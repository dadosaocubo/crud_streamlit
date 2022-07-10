# carregando as funções em outros arquivos .py
import services.database as db

# função para inserir registros no banco de dados
def incluir (nome, idade, profissao):
    db.cur.execute("""
            INSERT into public.clientes (nome, idade, profissao) 
            values('%s', '%s', '%s')
    """ % (nome, idade, profissao))
    db.con.commit()

# função para excluir registros no banco de dados
def excluir (id):
    db.cur.execute("""
            DELETE FROM clientes WHERE id = '%s'
    """ % (id))
    db.con.commit()

# função para alterar registros no banco de dados
def alterar (nome, idade, profissao, id):
    db.cur.execute("""
            UPDATE clientes SET (nome, idade, profissao) = ('%s', '%s', '%s')  WHERE id = '%s'
    """ % (nome, idade, profissao, id))
    db.con.commit()

# função para selecionar todos os registros no banco de dados
def selecionar ():
    db.cur.execute("""SELECT * FROM clientes""")
    recset = db.cur.fetchall()
    rows = []
    for rec in recset:
        rows.append(rec)
    return rows

# função para selecionar apenas um registros no banco de dados
def selecionar_id (id):
    db.cur.execute("""
            SELECT * FROM clientes WHERE id = '%s'
    """ % (id))
    recset = db.cur.fetchall()
    rows = []
    for rec in recset:
        rows.append(rec)
    return rows