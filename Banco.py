import json
from datetime import datetime
import os

# ================================
#  UTILITÁRIOS
# ================================

def carregar_dados():
    """Carrega dados do arquivo JSON, se existir."""
    if os.path.exists("banco_dados.json"):
        with open("banco_dados.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {"usuarios": [], "contas": []}


def salvar_dados(dados):
    """Salva os dados no arquivo JSON."""
    with open("banco_dados.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)


def gerar_numero_conta(dados):
    """Gera automaticamente numeração sequencial de contas."""
    return len(dados["contas"]) + 1


def timestamp():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


# ================================
#  SISTEMA DE USUÁRIOS
# ================================

def criar_usuario(dados):
    print("\n=== Cadastro de Usuário ===")
    cpf = input("CPF (somente números): ")

    # Verificar existência
    for u in dados["usuarios"]:
        if u["cpf"] == cpf:
            print("⚠ Usuário já cadastrado!")
            return dados

    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (DD/MM/AAAA): ")
    endereco = input("Endereço completo (Rua, Nº, Bairro, Cidade): ")

    novo_usuario = {
        "cpf": cpf,
        "nome": nome,
        "nascimento": nascimento,
        "endereco": endereco
    }

    dados["usuarios"].append(novo_usuario)
    print("✔ Usuário criado com sucesso!")
    return dados


def selecionar_usuario(dados):
    cpf = input("Digite o CPF do usuário: ")
    
    for usuario in dados["usuarios"]:
        if usuario["cpf"] == cpf:
            return usuario
    
    print("⚠ Usuário não encontrado!")
    return None


# ================================
#  CONTAS BANCÁRIAS
# ================================

def criar_conta(dados):
    print("\n=== Criar Conta Bancária ===")
    usuario = selecionar_usuario(dados)

    if not usuario:
        return dados

    numero = gerar_numero_conta(dados)

    conta = {
        "numero": numero,
        "cpf": usuario["cpf"],
        "saldo": 0,
        "extrato": [],
        "saques_diarios": 0
    }

    dados["contas"].append(conta)
    print(f"✔ Conta criada com sucesso! Número da conta: {numero}")
    return dados


def listar_contas(dados):
    print("\n=== CONTAS CADASTRADAS ===")
    for conta in dados["contas"]:
        print(f"Conta: {conta['numero']} | CPF: {conta['cpf']} | Saldo: R$ {conta['saldo']:.2f}")


def selecionar_conta(dados):
    numero = int(input("Número da conta: "))

    for conta in dados["contas"]:
        if conta["numero"] == numero:
            return conta
    print("⚠ Conta não encontrada!")
    return None


# ================================
#  OPERAÇÕES FINANCEIRAS
# ================================

def registrar_extrato(conta, tipo, valor):
    conta["extrato"].append({
        "data": timestamp(),
        "tipo": tipo,
        "valor": valor
    })


def depositar(conta):
    valor = float(input("Valor do depósito: R$ "))

    if valor <= 0:
        print("⚠ Depósito inválido!")
        return

    conta["saldo"] += valor
    registrar_extrato(conta, "Depósito", valor)
    print("✔ Depósito realizado com sucesso!")


def sacar(conta, limite=500, limite_saques=3):
    valor = float(input("Valor do saque: R$ "))

    if valor <= 0:
        print("⚠ Valor inválido.")
    elif valor > conta["saldo"]:
        print("⚠ Saldo insuficiente.")
    elif valor > limite:
        print("⚠ Limite de R$ 500 excedido.")
    elif conta["saques_diarios"] >= limite_saques:
        print("⚠ Limite diário de saques atingido.")
    else:
        conta["saldo"] -= valor
        conta["saques_diarios"] += 1
        registrar_extrato(conta, "Saque", valor)
        print("✔ Saque realizado!")

def transferir(dados):
    print("\n=== Transferência ===")
    origem = selecionar_conta(dados)
    destino = selecionar_conta(dados)

    if not origem or not destino:
        print("⚠ Erro ao selecionar contas.")
        return

    if origem["numero"] == destino["numero"]:
        print("⚠ Não é possível transferir para a mesma conta.")
        return

    valor = float(input("Valor da transferência: R$ "))

    if valor <= 0:
        print("⚠ Valor inválido.")
    elif valor > origem["saldo"]:
        print("⚠ Saldo insuficiente.")
    else:
        origem["saldo"] -= valor
        destino["saldo"] += valor
        registrar_extrato(origem, "Transferência Enviada", valor)
        registrar_extrato(destino, "Transferência Recebida", valor)
        print("✔ Transferência concluída!")


def exibir_extrato(conta):
    print("\n====== EXTRATO ======")
    if not conta["extrato"]:
        print("Nenhuma movimentação.")
    else:
        for mov in conta["extrato"]:
            print(f"{mov['data']} - {mov['tipo']}: R$ {mov['valor']:.2f}")

    print(f"\nSaldo atual: R$ {conta['saldo']:.2f}")
    print("======================")


def exportar_extrato(conta):
    nome_arquivo = f"extrato_conta_{conta['numero']}.txt"
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write("=== EXTRATO BANCÁRIO ===\n")
        for mov in conta["extrato"]:
            f.write(f"{mov['data']} - {mov['tipo']}: R$ {mov['valor']:.2f}\n")
        f.write(f"\nSaldo final: R$ {conta['saldo']:.2f}")
    
    print(f"✔ Extrato exportado para '{nome_arquivo}'")


# ================================
#  MENU PRINCIPAL
# ================================

def menu():
    print("""
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
""")
    return input("Escolha: ")


def main():
    dados = carregar_dados()

    while True:
        opcao = menu()

        if opcao == "1":
            dados = criar_usuario(dados)

        elif opcao == "2":
            dados = criar_conta(dados)

        elif opcao == "3":
            conta = selecionar_conta(dados)
            if conta:
                depositar(conta)

        elif opcao == "4":
            conta = selecionar_conta(dados)
            if conta:
                sacar(conta)

        elif opcao == "5":
            transferir(dados)

        elif opcao == "6":
            conta = selecionar_conta(dados)
            if conta:
                exibir_extrato(conta)

        elif opcao == "7":
            conta = selecionar_conta(dados)
            if conta:
                exportar_extrato(conta)

        elif opcao == "8":
            listar_contas(dados)

        elif opcao == "0":
            salvar_dados(dados)
            print("✔ Dados salvos. Sistema encerrado.")
            break

        else:
            print("⚠ Opção inválida! Tente novamente.")


main()
