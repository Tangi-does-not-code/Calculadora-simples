def adicao(x, y):
    """Soma dois números."""
    return x + y

def subtracao(x, y):
    """Subtrai dois números."""
    return x - y

def multiplicacao(x, y):
    """Multiplica dois números."""
    return x * y

def divisao(x, y):
    """Divide dois números."""
    if y == 0:
        return "Não da pra dividir por zero bobinho."
    return x / y

print("Selecione a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

while True:
    escolha = input("Digite sua escolha (1/2/3/4): ")

    if escolha in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite números.")
            continue

        if escolha == '1':
            print(num1, "+", num2, "=", adicao(num1, num2))

        elif escolha == '2':
            print(num1, "-", num2, "=", subtracao(num1, num2))

        elif escolha == '3':
            print(num1, "*", num2, "=", multiplicacao(num1, num2))

        elif escolha == '4':
            print(num1, "/", num2, "=", divisao(num1, num2))

        proxima_calculadora = input("Deseja fazer outro cálculo? (s/n): ")
        if proxima_calculadora.lower() != 's':
            break
    else:
        print("Algo deu errado. Por favor, digite um número entre 1 e 4.")