import os
os.system('cls')

indice = float(input("Digite o índice de poluição do local: "))

match indice:
    case 0|1|2:
        print(f"O índice de Poluição {indice} é ACEITÁVEL!")

    case 3|4|5:
        print(f"O índice de Poluição {indice} para SUSPENDER ATIVIDADES GRUPO I")
    
    case 6|7:
        print(f"O índice de Poluição {indice} é para SUSPENDER ATIVIDADES GRUPO II")

    case _:
        print(f"O nível de Poluição {indice} é para SUSPENDER ATIVIDADES DE TODOS OS GRUPOS")