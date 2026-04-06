import contas
import pessoas


class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[pessoas.Pessoa] | None = None,
        contas: list[contas.Conta] | None = None,
    ) -> None:
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f"agencias={self.agencias!r}, clientes={self.clientes!r}, contas={self.contas!r}"
        return f"{class_name}({attrs})"

    def _checa_agencia(self, conta: contas.Conta) -> bool:
        if conta.agencia in self.agencias:
            return True
        return False

    def _checa_cliente(self, cliente: pessoas.Pessoa) -> bool:
        if cliente in self.clientes:
            return True
        return False

    def _checa_conta(self, conta: contas.Conta) -> bool:
        if conta in self.contas:
            return True
        return False

    def _checa_conta_do_cliente(self, cliente, conta) -> bool:
        if cliente.conta is conta:
            return True
        return False

    def autenticar(self, cliente: pessoas.Pessoa, conta: contas.Conta) -> bool:
        return (
            self._checa_agencia(conta)
            and self._checa_cliente(cliente)
            and self._checa_conta(conta)
            and self._checa_conta_do_cliente(cliente, conta)
        )
