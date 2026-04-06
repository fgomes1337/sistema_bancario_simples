import contas
import pessoas
import banco

c1 = pessoas.Cliente("Felipe", 26)
c2 = pessoas.Cliente("Maria", 18)

cc1 = contas.ContaCorrente(222, 7474, 0, 100)
cp1 = contas.ContaPoupanca(111, 9898)
c1.conta = cc1
c2.conta = cp1

bank = banco.Banco()
bank.agencias.extend([111, 222])
bank.clientes.extend([c1, c2])
bank.contas.extend([cc1, cp1])


if bank.autenticar(c1, cc1):
    c1.conta.sacar(50)
    c1.conta.sacar(50)
    c1.conta.sacar(1)
    c1.conta.depositar(200)
else:
    print("ERRO: Cliente 1 tentando acessar conta de terceiros!")

if bank.autenticar(c2, cp1):
    c2.conta.sacar(1)
    c2.conta.depositar(100)
    c2.conta.sacar(50)
else:
    print("ERRO: Cliente 1 tentando acessar conta de terceiros!")

if bank.autenticar(c1, cp1):
    c1.conta.sacar(50)
    c1.conta.sacar(50)
    c1.conta.sacar(1)
    c1.conta.depositar(200)
else:
    print("ERRO: Cliente 1 tentando acessar conta de terceiros!")

if bank.autenticar(c2, cc1):
    c2.conta.sacar(50)
    c2.conta.sacar(50)
    c2.conta.sacar(1)
    c2.conta.depositar(200)
else:
    print("ERRO: Cliente 1 tentando acessar conta de terceiros!")
