import os
os.system('cls')

total = float(input("Digite o valor total da compra: "))
print("\n 1. À vista em espécie\n 2. Débito\n 3. Crédito")
formaPagamento = float(input("\nDigite o Código da forma de Pagamento: "))

match formaPagamento:
    case 1:
        porcentagem = (15 * total) / 100
        novoTotal = total - porcentagem

        print(f"À vista: O novo total é {novoTotal}")

    case 2:
        porcentagem = (10 * total) / 100
        novoTotal = total - porcentagem

        print(f"Débito: O novo total é {novoTotal}")

    case 3:
        porcentagem = (5 * total) / 100
        novoTotal = total - porcentagem

        print(f"Crédito: O novo total é {novoTotal}")

    case _:
        print("Opção inválida. Tente novamente!")
