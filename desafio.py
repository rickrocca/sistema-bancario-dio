menu = """

<=====================>
    [d]Depositar
    [s]Sacar
    [e]Extrato
    [q]Sair
<=====================>

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    

    if opcao == "d":
        print("Deposito")
        deposito = float(input("Insira o valor: "))
        if deposito > 0:
            pass
            extrato += f"+{deposito:.2f}\n"
            saldo += deposito
            print(f"Saldo: {saldo:.2f}")
    elif opcao == "s":
        if LIMITE_SAQUES == 0:
            print("Limite de saques diarios atingido.")
        else:
            print("Saque")
            saque = float(input("Valor do saque: "))
            if saque > 500:
                print("Limite Maximo de R$ 500.00 por saque.")
            elif saldo <= 0 or saque > saldo:
                print("Nao foi possivel sacar o dinheiro.\n      Falta de saldo")
                print(f"Saldo: {saldo:.2f}")
            else:
                extrato += f"-{saque:.2f}\n"
                saldo -= saque
                print(f"Saldo: {saldo:.2f}")
                LIMITE_SAQUES -= 1
    elif opcao == "e":
        print("Extrato")
        print(extrato) 
        print(f"Saldo: {saldo:.2f}")
    elif opcao == "q":
        break

    else:
        print("Opcao invalida, selecione novamente")
        






