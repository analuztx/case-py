import os
os.system('cls')

print(f"Calculo de Grandezas \n\n1. Tensão (em Volt)\n2. Resistência (em Ohm)\n3. Corrente (em Ampére)")
op = float(input("\nDigite uma opcão:"))

match op:
    case 1:
        r = float(input("Digite o valor da Resistência (em Ohm): "))
        i = float(input("Digite o valor da Corrente (em Ampére): "))

        u = r * i

        print(f"\nO valor da Tensão é: {u}")

    case 2:
        u = float(input("Digite o valor da Tensão (em Volts): "))
        i = float(input("Digite o valor da Corrente (em Ampére): "))

        r = u/i

        print(f"\nO valor da Resistência é: {r}")

    case 3:
        u = float(input("Digite o valor da Tensão (em Volts): "))
        r = float(input("Digite o valor da Resistência (em Ohm): "))

        i = u/r

        print(f"\nO valor da Corrente é: {i}")

    case _:
        print("Opção inválida. Tente novamente!")
