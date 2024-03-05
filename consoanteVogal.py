import os
os.system('cls')

letra = input("Digite uma letra: ")

match letra:
    case "a"|"A"|"e"|"E"|"i"|"I"|"o"|"O"|"u"|"U":
        print(f"A letra '{letra}' é uma vogal!")
    case _:
        print(f"A letra '{letra}' é uma consoante!")

