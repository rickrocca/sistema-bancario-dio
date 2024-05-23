def menu():
    menu = """

    <=====================>
        [d]  Depositar
        [s]    Sacar
        [e]   Extrato
        [q]     Sair
        [nu] Novo Usuario
        [nc]  Nova Conta
        [lc] Listar Contas
    <=====================>

    """
    return input(menu)

def depositar(saldo, deposito, extrato, /): 
    if deposito > 0:
        pass
        extrato += f"+{deposito:.2f}\n"
        saldo += deposito
        print(f"Saldo: {saldo:.2f}")
    else:
        print("Insira um Valor Valido!")
    return saldo, extrato

def sacar(*, saldo, saque,  extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = saque > saldo
    excedeu_limite = saque > limite
    excedeu_saques = numero_saques >= limite_saques
    #print(numero_saques)
    if excedeu_saques:
        print("Limite de saques diarios atingido.")
    
    elif excedeu_limite:
        print("Limite Maximo de R$ 500.00 por saque.")

    elif excedeu_saldo:
        print("Nao foi possivel sacar o dinheiro.\n      Falta de saldo")
        print(f"Saldo: {saldo:.2f}")

    elif saque > 0:
        extrato += f"-{saque:.2f}\n"
        saldo -= saque
        numero_saques += 1
        print(f"Saldo: {saldo:.2f}")
    else:
        print("Valor informado Invalido")       

    return saldo, extrato, numero_saques

def exibirExtrato(extrato, /, *, saldo):
    print("Extrato")
    print(extrato) 
    print(f"Saldo: {saldo:.2f}")

def criarUsuario(usuarios):
    cpf = input("Informe o CPF (somente numero): ")
    usuario = filtrarUsuario(cpf, usuarios)
    
    if usuario:
        print("\n Ja existe um usuario com esse cpf")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereco (logradouro, nro - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("Usuario criado com sucesso")

def filtrarUsuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criarConta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrarUsuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com Sucesso!!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nUsuario nao encontrado")

def listarContas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()
        
        if opcao == "d":
            print("Deposito")
            valor = float(input("Insira o valor: "))
            saldo, extrato = depositar(saldo, valor, extrato) 

        elif opcao == "s":
            print("Saque")
            valor = float(input("Valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo = saldo,
                saque = valor,
                extrato = extrato, 
                limite = limite, 
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES
            )

        elif opcao == "e":
            exibirExtrato(extrato, saldo = saldo)

        elif opcao == "nu":
            criarUsuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criarConta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listarContas(contas)

        elif opcao == "q":
            break

        else:
            print("Opcao invalida, selecione novamente")

main()
