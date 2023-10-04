# Calculadora


operacao = input("Digite sua operação (adicao, sub, mult, divisao): ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

def adicao(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        print("ERRO!! Divisão por zero não é permitida.")
        return None
    return x / y

resultado = None

if operacao == "adicao":
    resultado = adicao(num1, num2)
elif operacao == "sub":
    resultado = sub(num1, num2)
elif operacao == "mult":
    resultado = mult(num1, num2)
elif operacao == "divisao":
    resultado = divisao(num1, num2)
else:
    print("Operação inválida")

if resultado is not None:
    print("O resultado da operação", operacao, resultado)
