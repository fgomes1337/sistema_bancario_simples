import contas


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f"nome={self.nome!r}, idade={self.idade!r}"
        return f"{class_name}({attrs})"


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None

