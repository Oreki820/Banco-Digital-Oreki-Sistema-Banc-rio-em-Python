# 🏦 Banco Digital Oreki — Sistema Bancário em Python

✨ *Um sistema bancário completo, modular e profissional, desenvolvido para estudos, portfólio e desafios da DIO.*

---

## 📌 Sobre o Projeto

Este projeto é uma evolução do tradicional **Sistema Bancário em Python** exigido nos desafios da DIO.
Aqui ele foi completamente **refatorado**, **organizado em funções**, **expandido**, e transformado em um **banco digital completo**, com múltiplas contas, usuários, transferências e persistência de dados.

Ideal para:

* ✔ Estudos de Python
* ✔ Prática de lógica de programação
* ✔ Portfólio profissional
* ✔ Entrevistas técnicas
* ✔ Entrega de desafios da DIO

---

## 🚀 Funcionalidades Implementadas

O sistema inclui **todos os requisitos dos desafios originais**, e muito mais:

### 🧍 Gestão de Usuários

* Cadastro de usuário
* Busca por CPF
* Validação de existência

---

### 🏦 Gestão de Contas Bancárias

* Criação de contas vinculadas ao usuário
* Numeração automática de contas
* Listagem de contas existentes

---

### 💰 Operações Financeiras

* Depósito
* Saque (com limite diário e limite por operação)
* Transferência entre contas
* Saldo em tempo real
* Extrato formatado com timestamp

---

### 📜 Extratos e Histórico

* Histórico detalhado de todas as operações
* Data e hora registradas
* Extrato limpo e organizado
* Exportação de extrato para arquivo `.txt`

---

### 💾 Persistência de Dados

Os dados são armazenados em:

```
banco_dados.json
```

Sempre que você fecha o sistema, tudo é salvo automaticamente.

---

## 🧠 Arquitetura Lógica

```
📁 Sistema Bancário
│
├── banco_dados.json      # Banco de dados local
├── banco.py              # Arquivo principal do sistema
└── README.md             # Este arquivo :)
```

---

## 🖥 Como Executar

1. Certifique-se de ter o **Python 3.10+** instalado.

2. Clone o repositório:

```bash
git clone https://github.com/SeuUsuario/Sistema-Bancario-Oreki.git
```

3. Entre na pasta:

```bash
cd Sistema-Bancario-Oreki
```

4. Execute:

```bash
python banco.py
```

Pronto! O sistema iniciará automaticamente com o menu interativo.

---

## 📋 Menu Principal

O sistema exibe o seguinte menu:

```
=============================
     BANCO DIGITAL OREKI
=============================
[1] Criar usuário
[2] Criar conta
[3] Depositar
[4] Sacar
[5] Transferir
[6] Extrato
[7] Exportar extrato
[8] Listar contas
[0] Sair
```

---

## 🏗 Tecnologias Utilizadas

* **Python 3**
* JSON (persistência)
* Programação Procedural
* Modularização
* Estruturas de Dados (listas e dicionários)

---

## ⭐ Diferenciais do Projeto

Este sistema vai além do desafio original:

### 🔥 Evoluções Implementadas

* Múltiplas contas por usuário
* Transferência entre contas
* Exportação de extrato
* Histórico com timestamp
* Saques limitados por dia
* Arquitetura escalável
* JSON como banco de dados
* Sistema pronto para evoluir para API (Flask / FastAPI)

---

## 📌 Exemplos de Uso

### Criando usuário:

```
Nome completo: Lucas Gabriel
CPF: 00011122233
Nascimento: 12/03/2000
Endereço: Rua das Flores, 123 – Centro – Santana do Livramento
```

### Criando conta:

```
✔ Conta criada com sucesso! Número da conta: 1
```

### Realizando depósito:

```
Valor: 200
✔ Depósito realizado!
```

### Extrato:

```
05/11/2025 14:33 - Depósito: R$ 200,00
Saldo atual: R$ 200,00
```

---

## 🛠 Futuras Melhorias (Roadmap)

* [ ] Criar API com Flask ou FastAPI
* [ ] Criar interface gráfica (Tkinter ou PyQt)
* [ ] Criar dashboard de gerenciamento
* [ ] Implementar login com senha
* [ ] Dashboard HTML + Bootstrap

---

## 🤝 Contribuições

Contribuições, sugestões e melhorias são sempre bem-vindas!
Abra uma *issue* ou envie um *pull request*.

---

## 🧑‍💻 Autor

**Lucas Gabriel Ferreira Gomes (Oreki)**
Desenvolvedor Python e Cientista de Dados Jr
📍 Santana do Livramento – RS
🔗 GitHub | LinkedIn | Portfólio

---

## ⭐ Deixe uma Estrela no Repositório!

Se este projeto te ajudou, deixe uma ⭐ no GitHub — isso me motiva a continuar criando projetos incríveis 💜

É só pedir!
