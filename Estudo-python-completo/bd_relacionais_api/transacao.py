import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "empresa.db")
print(f"Conexão:[{conexao}]")

cursor = conexao.cursor()  
cursor.row_factory = sqlite3.Row 

try:
    cursor.execute("INSERT INTO cliente (nome, idade) VALUES (?, ?)", ("Minho", 7))
    cursor.execute("INSERT INTO cliente (id, nome, idade) VALUES (?, ?, ?)", (2, "Robertinho", 1))
    conexao.commit()
except Exception as e:
    print(f"ERRO: [{e}]")
    conexao.rollback()
# finally:
    # conexao.commit()