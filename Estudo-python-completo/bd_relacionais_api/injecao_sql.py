import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "empresa.db")
print(f"Conexão:[{conexao}]")

cursor = conexao.cursor()  
cursor.row_factory = sqlite3.Row 

id_cliente = input("Informe o ID do cliente: ")
# cursor.execute(f"SELECT * FROM cliente WHERE id={id_cliente}") # inseguro
cursor.execute("SELECT * FROM cliente WHERE id=?", (id_cliente,)) # seguro
# cliente = cursor.fetchone()
# print(dict(cliente))

clientes = cursor.fetchall()
for cliente in clientes:
    print(dict(cliente))
