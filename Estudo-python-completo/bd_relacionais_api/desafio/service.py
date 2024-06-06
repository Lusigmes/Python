from sqlite3 import Cursor
from entity import Cliente, PessoaFisica, PessoaJuridica

class ClienteService:
    def __init__(self, cursor: Cursor) -> None:
        self.cursor = cursor
        
        def _mostrar_dados(self, dados_cliente: dict[str, str | int ]) -> str:
            if "cpf" in dados_cliente:
                return PessoaFisica.converter_obj_bd(objeto_db=dados_cliente)
            return PessoaJuridica.converter_obj_bd(objeto_db=dados_cliente)
        
        def _criar_cliente(self, cliente: Cliente) -> int:
            self.cursor.execute(
                "INSERT INTO cliente (email, telefone, status) VALUES (?, ?, ?)",
                (cliente.email, cliente.telefone, cliente.status)
            )
            return self.cursor.lastrowid
        
