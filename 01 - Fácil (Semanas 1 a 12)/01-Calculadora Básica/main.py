def soma (a,b):
    return a+b

def subtracao (a,b):
    return a-b

def multiplicacao (a,b):
    return a*b

def divisao (a,b):
    if b == 0:
        print("Não permitido divisão por zero")
    else:
        return a/b

while True:

    operacao = input("Digite a operacao desejada: +, -, *, /")
    if operacao not in ["+","-","*","/"]:
        print("Operação inválida")
        continue

    try:
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
    except ValueError:
        print("Erro: Digite números válidos!")
        continue

    if operacao == "+":
        resultado = soma(num1,num2)
    elif operacao == "-":
        resultado = subtracao(num1,num2)
    elif operacao == "*":
        resultado = multiplicacao(num1,num2)
    elif operacao == "/":
        resultado = divisao(num1,num2)  
    else:
        print("Operação inválida")  

    print("O resultado é: ", resultado)

    continuar = input("Deseja continuar? (s/n): ").strip().lower()
    if continuar == "n":
        print("Encerrando a calculadora. Até mais!")
        break