def contar_caracteres_incluindo_espacos(texto):
    return len(texto)

def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

while True:
    print("Escolha uma opção:")
    print("1. Contar caracteres (incluindo espaços)")
    print("2. Contar palavras")
    print("3. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        texto = input("Digite o texto: ")
        resultado = contar_caracteres_incluindo_espacos(texto)
        print(f"O número de caracteres (incluindo espaços) é: {resultado}")
    elif opcao == "2":
        texto = input("Digite o texto: ")
        resultado = contar_palavras(texto)
        print(f"O número de palavras é: {resultado}")
    elif opcao == "3":
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
