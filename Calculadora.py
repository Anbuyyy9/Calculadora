# Calculadora em Python

# Solicita a operação e os números ao usuário
operacao = input("Digite sua operação (adicao, sub, mult, divisao): ").strip().lower()
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Funções para as operações matemáticas
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

# Verifica a operação escolhida e realiza o cálculo
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
    print("Operação inválida!")

# Exibe o resultado se o cálculo foi realizado com sucesso
if resultado is not None:
    print("O resultado da operação", operacao, "é:", resultado)
