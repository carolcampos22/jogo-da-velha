import time

# Tabuleiro vazio com 9 posições
tabuleiro = [" " for _ in range(9)]

# Função para exibir o tabuleiro
def exibir_tabuleiro():
    for i in range(0, 9, 3):
        print(f"{tabuleiro[i]} | {tabuleiro[i+1]} | {tabuleiro[i+2]}")
        if i < 6:
            print("--+---+--")
    print()

# Função para verificar se um jogador venceu
def verificar_vencedor(tabuleiro, jogador):
    combinacoes_vencedoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colunas
        [0, 4, 8], [2, 4, 6]              # diagonais
    ]
    return any(all(tabuleiro[pos] == jogador for pos in combinacao) for combinacao in combinacoes_vencedoras)

# Verifica se deu empate
def verificar_empate(tabuleiro):
    return " " not in tabuleiro

# Algoritmo Minimax
def minimax(tabuleiro, profundidade, maximizando):
    if verificar_vencedor(tabuleiro, "X"):
        return -10 + profundidade
    if verificar_vencedor(tabuleiro, "O"):
        return 10 - profundidade
    if verificar_empate(tabuleiro):
        return 0

    if maximizando:  # Jogada do computador (O)
        melhor_valor = -float("inf")
        for i in range(9):
            if tabuleiro[i] == " ":
                tabuleiro[i] = "O"
                valor = minimax(tabuleiro, profundidade + 1, False)
                tabuleiro[i] = " "
                melhor_valor = max(melhor_valor, valor)
        return melhor_valor
    else:  # Jogada do jogador (X)
        melhor_valor = float("inf")
        for i in range(9):
            if tabuleiro[i] == " ":
                tabuleiro[i] = "X"
                valor = minimax(tabuleiro, profundidade + 1, True)
                tabuleiro[i] = " "
                melhor_valor = min(melhor_valor, valor)
        return melhor_valor

# Função para encontrar a melhor jogada do computador
def melhor_jogada(tabuleiro):
    melhor_valor = -float("inf")
    melhor_posicao = -1

    for i in range(9):
        if tabuleiro[i] == " ":
            tabuleiro[i] = "O"
            valor = minimax(tabuleiro, 0, False)
            tabuleiro[i] = " "
            if valor > melhor_valor:
                melhor_valor = valor
                melhor_posicao = i

    return melhor_posicao

# Função principal do jogo
def jogar_jogo():
    while True:
        exibir_tabuleiro()

        # Turno do jogador
        while True:
            try:
                jogada = int(input("Escolha uma posição (0-8): "))
                if 0 <= jogada <= 8 and tabuleiro[jogada] == " ":
                    break
                else:
                    print("Posição inválida ou já ocupada.")
            except ValueError:
                print("Por favor, insira um número de 0 a 8.")
        tabuleiro[jogada] = "X"

        if verificar_vencedor(tabuleiro, "X"):
            exibir_tabuleiro()
            print("Você venceu!")
            break
        if verificar_empate(tabuleiro):
            exibir_tabuleiro()
            print("Empate!")
            break

        # Turno do computador
        print("Computador está pensando...")
        time.sleep(1)
        melhor_pos = melhor_jogada(tabuleiro)
        tabuleiro[melhor_pos] = "O"

        if verificar_vencedor(tabuleiro, "O"):
            exibir_tabuleiro()
            print("O computador venceu!")
            break
        if verificar_empate(tabuleiro):
            exibir_tabuleiro()
            print("Empate!")
            break

print("Bem-vindo ao Jogo da Velha!")
print("Você é o X. O computador é o O.")
print("Posições do tabuleiro:")
print("0 | 1 | 2\n--+---+--\n3 | 4 | 5\n--+---+--\n6 | 7 | 8\n")

jogar_jogo()

