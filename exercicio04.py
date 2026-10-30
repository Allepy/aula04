nota = input("Digite a letra que represente a nota (A, B, C, D ou F): ").upper()
match nota:
    case 'A':
        print("Excelente!")
    case 'B':
        print("Bom!")
    case 'C':
        print("Regular!")
    case 'D':
        print("Ruim!")
    case 'F':
        print("Reprovado!")
    case _:
        print("Erro: Letra inválida! Por favor, digite apenas A, B, C, D ou F.")    