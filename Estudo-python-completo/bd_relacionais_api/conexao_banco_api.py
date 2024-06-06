import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# Conexão com o banco
conexao = sqlite3.connect(ROOT_PATH / "empresa.db")
print(f"Conexão:[{conexao}]")

# Criar cursor para executar sql
cursor = conexao.cursor()  
cursor.row_factory = sqlite3.Row # retorna os resultados como dicionarios
# facilita o acesso as colunas

# Criar Tabela
def criar_tabela(conexao, cursor):
    cursor.execute("CREATE TABLE cliente (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(50), idade INTEGER)")
    conexao.commit() # Sempre commitar quando executar uma manipulação dentro do banco

# Inserir Um Objeto na Tabela
def inserir_cliente(conexao, cursor, nome, idade):
    dados = (nome,idade)
    cursor.execute("INSERT INTO cliente (nome, idade) VALUES (?, ?)" , dados) # Valores mascarados
    print("Inserido")
    conexao.commit() # Sempre commitar quando executar uma manipulação dentro do banco

# Inserir Vários Objetos na Tabela
def inserir_clientes(conexao, cursor, dados):
    cursor.executemany("INSERT INTO cliente (nome, idade) VALUES (?, ?)", dados)
    print("Varios clientes inseridos")
    conexao.commit()
    
# Atualizar Dados na Tabela
def atualizar_infos(conexao, cursor, nome, idade, id):
    dados = (nome,idade, id)
    cursor.execute("UPDATE cliente SET nome=?, idade=? WHERE id=?", dados)
    print("Atualizado")
    conexao.commit() # Sempre commitar quando executar uma manipulação dentro do banco

# Remover Dados na Tabela
def remover_clientes(conexao, cursor, id):
    dados = (id,)
    cursor.execute("DELETE FROM cliente WHERE id=?", dados)
    print("Removido")
    conexao.commit()
    
# Consultar tabela
def consultar_um(cursor, id):
    dados = (id,)
    cursor.execute("SELECT * FROM cliente WHERE id=?", dados)
    consulta = cursor.fetchone() # return cursor.fetchone() # caso usar assim, recuperar o objeto fora do metodo
    print(dict(consulta))
    print(consulta["nome"])
    
def consultar_todos(cursor):
    cursor.execute("SELECT * FROM cliente") # return cursor.execute("SELECT * FROM cliente") # caso usar assim, recuperar o objeto fora do metodo
    consultas = cursor.fetchall()
    for consulta in consultas: # se usar return... usar laço fora do metodo
        print(dict(consulta))
    
    
# inserir_cliente(conexao, cursor, "Miu",7)

# atualizar_infos(conexao, cursor, "Luis", 26, 1)

# remover_clientes(conexao, cursor, 3)

# varios_clientes = [('Roberto', 1), ('Larissa', 2), ('Vanderlei', 1),] 
# inserir_clientes(conexao, cursor, varios_clientes)

consultar_todos(cursor)
print("*"*50)
consultar_um(cursor, 1)
