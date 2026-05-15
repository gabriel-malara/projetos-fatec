jogador = "X"
jogo = [[' ' for i in range(3)] for _ in range(3)]

separador = '|'

def exibir_jogo():
    for i in jogo:
        print(separador.join(i))

while True:
    casa_desejada = int(input(f'Digite a casa que deseja ocupar ({jogador}): '))
    jogada_sucedida = False

    if 1 <= casa_desejada <= 9:
        if casa_desejada <= 3:
            if jogo[0][casa_desejada-1] == " ":
                jogo[0][casa_desejada-1] = jogador
                jogada_sucedida = True
        elif casa_desejada <= 6:
            if jogo[1][casa_desejada-4] == " ":
                jogo[1][casa_desejada-4] = jogador
                jogada_sucedida = True
        elif casa_desejada <= 9:
            if jogo[2][casa_desejada-7] == " ":
                jogo[2][casa_desejada-7] = jogador
                jogada_sucedida = True

    if jogada_sucedida:
        exibir_jogo()
        if jogador == "X":
            jogador = "O"
        else:
            jogador = "X"
    else:
        print("Um erro ocorreu. Tente novamente.")