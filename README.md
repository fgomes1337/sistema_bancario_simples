# Sistema Bancário simples em Python

Projeto desenvolvido em python para praticar conceitos de POO, modularização e boas práticas de desenvolvimento

## Conceitos de ADS Aplicados

- **Abstração & Herança:** Uso de classes abstratas (`ABC`) para definir a base das contas e herança para `Cliente` (herdando de `Pessoa`.)
- **Polimorfismo:** O método `sacar`comporta-se de forma distinta para `ContaCorrente` (com limite) e `ContaPoupança`.
- **Encapsulamento:** Proteção de atributos (`_saldo`) e uso de métodos internos de validação no Banco.
- **Composição:** O `Banco` gerencia coleções de objetos, e cada `Cliente`possui uma associação com uma `Conta`.
- **Modularização:** Divisão do código em arquivos separados (`contas.py`, `pessoas.py`, `banco.py`) para facilitar a manutenção.

## 📂 Estrutura do Projeto:

- `contas.py`: Contém a lógica de classes abstrata, herança e tipos de conta.
- `pessoas.py`: Gerencia Pessoa e Cliente.
- `banco.py`: O "Cérebro" do sistema, responsável pela autenticação e gestão de Clientes e Contas
- `main.py`: Execução e testes do sistema.

## Lógica de Autenticação

- Se a agência é permitida pelo banco.
- Se o cliente está cadastrado no banco.
- Se a conta está cadastrada no banco.
- Se a conta informada pertence legalmente ao cliente que tenta a operação.

Versão do Python utilizada: **Python 3.12.3**
