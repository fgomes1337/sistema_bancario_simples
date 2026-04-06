from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self._saldo = saldo

    @abstractmethod
    def sacar(self, valor: float) -> float: ...

    def depositar(self, valor: float) -> float:
        if valor > 0:
            self._saldo += valor
            self.detalhes(f"(DEPÓSITO {valor:.2f})")
            return self._saldo

        print("Não é possível depositar uma quantia tão baixa.")
        return self._saldo

    def detalhes(self, msg="") -> None:
        print(f"O seu saldo é {self._saldo:.2f}. {msg}")
        print("--")

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f"agencia={self.agencia!r}, conta={self.conta!r}, saldo={self._saldo!r}"
        return f"{class_name}({attrs})"


class ContaPoupanca(Conta):
    def sacar(self, valor: float) -> float:
        valor_pos_saque = self._saldo - valor

        if valor_pos_saque >= 0:
            self._saldo -= valor
            self.detalhes(f"(SAQUE {valor:.2f})")
            return self._saldo

        print(f"Não foi possível realizar o saque: {valor:.2f}")
        self.detalhes(f"(SAQUE NEGADO {valor:.2f})")
        return self._saldo


class ContaCorrente(Conta):
    def __init__(
        self, agencia: int, conta: int, saldo: float = 0, limite: float = 0
    ) -> None:
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = (
            f"agencia={self.agencia!r}, conta={self.conta!r},"
            f"saldo={self._saldo!r}, limite={self.limite!r}"
        )
        return f"{class_name}({attrs})"

    def sacar(self, valor: float) -> float:
        valor_pos_saque = self._saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self._saldo -= valor
            self.detalhes(f"(SAQUE {valor:.2f})")
            return self._saldo

        print(f"Não foi possível realizar o saque: {valor:.2f}")
        print(f"Seu limite é de {self.limite:.2f}")
        self.detalhes(f"(SAQUE NEGADO {valor:.2f})")
        return self._saldo


# if __name__ == "__main__":
#     cp1 = ContaPoupanca(222, 9898)
#     print(cp1)
#     cp1.sacar(1)
#     cp1.depositar(1)
#     cp1.sacar(1)
#     cp1.sacar(1)

#     cc1 = ContaCorrente(222, 9898, 0, 100)
#     print(cc1)
#     cc1.sacar(1)
#     cc1.depositar(1)
#     cc1.sacar(1)
#     cc1.sacar(50)
#     cc1.sacar(49)
#     cc1.sacar(1)
