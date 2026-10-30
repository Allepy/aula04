num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")
match operacao:
    case '+':
        resultado = num1 + num2
        print(f"0 resultado de {num1} + {num2} é: {resultado}")
    case '-':
        resultado = num1 + num2
        print(f"0 resultado de {num1} - {num2} é: {resultado}")
        