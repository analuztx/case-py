import os
os.system('cls')

peso = float(input("Digite em KG o peso de uma pessoa: "))

print("\n 1. Mercúrio\n 2. Vênus\n 3. Marte\n 4. Júpiter\n 5. Saturno")

idPlaneta = float(input("Digite o ID do planeta: "))

match idPlaneta:
    case 1:
        pesoNovo = peso * 0.37
        print(f"\nPeso na Terra: {peso}")
        print(f"Peso em Mercúrio: {pesoNovo}")

    case 2:
        pesoNovo = peso * 0.88
        print(f"\nPeso na Terra: {peso}")
        print(f"Peso em Vênus: {pesoNovo}")

    case 3:
        pesoNovo = peso * 0.38
        print(f"\nPeso na Terra: {peso}")
        print(f"Peso em Marte: {pesoNovo}")

    case 4:
        pesoNovo = peso * 2.64
        print(f"\nPeso na Terra: {peso}")
        print(f"Peso em Júpiter: {pesoNovo}")

    case 5:
        pesoNovo = peso * 1.15
        print(f"\nPeso na Terra: {peso}")
        print(f"Peso em Saturno: {pesoNovo}")

    case _:
        print("Opção inválida. Tente novamente!")