import os
os.system('cls')

salario = float(input("Digite o seu salário atual: "))
categoria = input("Digite a sua categoria: (A | B | C): ")

match categoria:
    case "A" | "a":
        porcentagem = (salario * 10) / 100
        novoSalario = salario + porcentagem

        print(f"\nSeu salário atual: {salario}\nSeu aumento será de: {porcentagem}")
        print(f"Seu NOVO salário: {novoSalario}")

    case "B" | "B":
        porcentagem = (salario * 15) / 100
        novoSalario = salario + porcentagem

        print(f"\nSeu salário atual: {salario}\nSeu aumento será de: {porcentagem}")
        print(f"Seu NOVO salário: {novoSalario}")

    case "C" | "c":
        porcentagem = (salario * 25) / 100
        novoSalario = salario + porcentagem

        print(f"\nSeu salário atual: {salario}\nSeu aumento será de: {porcentagem}")
        print(f"Seu NOVO salário: {novoSalario}")

    case _:
        print("Valor incorreto. Tente novamente!")
