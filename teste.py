def contar_caracteres(texto):
    return len(texto)
def contar_palavras(texto):
    return len(texto.split())
while True:
    print("Digite o texto para análise ou 'sair' para encerrar o programa.")
    texto_usuario = input()
    if texto_usuario.lower() == 'sair':
        break
    print("Você deseja contar 'caracteres' ou 'palavras'?")
    escolha = input()

    if escolha.lower() == 'caracteres':
        num_caracteres = contar_caracteres(texto_usuario)        
        print(f"O texto contém {num_caracteres} caracteres.")
    elif escolha.lower() == 'palavras':
        num_palavras = contar_palavras(texto_usuario)
        print(f"O texto contém {num_palavras} palavras.")
    else:
        print("Escolha inválida. Por favor, digite 'caracteres' ou 'palavras'.")