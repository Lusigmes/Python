import sqlite3
from pathlib import Path
from sqlite3 import Connection, Cursor

def criar_conexao() -> Connection:
    ROOT_PATH = Path(__file__).parent
    return sqlite3.connect(ROOT_PATH / "sistema_bancario_bd.sqlite")

def construir_banco(cursor: Cursor) -> None:
    cursor.executescript(
        """
        CREATE TABLE IF NOT EXISTS cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL,
            status TEXT NOT NULL,
            criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        
        CREATE TABLE IF NOT EXISTS pessoa_fisica (
            clientef_id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL,
            renda_mensal REAL NOT NULL,
            FOREIGN KEY (clientef_id) REFERENCES cliente(id)
        );
        
        CREATE TABLE IF NOT EXISTS pessoa_juridica (
            clientej_id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            cnpj TEXT NOT NULL,
            faturamento_anual REAL NOT NULL,
            FOREIGN KEY (clientej_id) REFERENCES cliente(id)
        );
        """
    )