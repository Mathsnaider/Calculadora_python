def calculadora():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        print("\nEscolha a operação:")
        print("1 - Adição (+)")
        print("2 - Subtração (-)")
        print("3 - Multiplicação (*)")
        print("4 - Divisão (/)")

        op = input("Digite o número da operação desejada: ")

        if op == "1":
            print(f"\nResultado: {num1} + {num2} = {num1 + num2}")
        elif op == "2":
            print(f"\nResultado: {num1} - {num2} = {num1 - num2}")
        elif op == "3":
            print(f"\nResultado: {num1} * {num2} = {num1 * num2}")
        elif op == "4":
            if num2 == 0:
                print("\nErro: divisão por zero não é permitida!")
            else:
                print(f"\nResultado: {num1} / {num2} = {num1 / num2}")
        else:
            print("\nOpção inválida! Escolha uma operação válida.")

    except ValueError:
        print("\nErro: Digite apenas números!")

# Executar a calculadora
calculadora()

