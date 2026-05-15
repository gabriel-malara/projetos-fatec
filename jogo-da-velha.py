jogador = "X"
jogo = [[' ' for i in range(3)] for _ in range(3)]

separador = '|'

def exibir_jogo():
    for i in jogo:
        print(separador.join(i))

def verificar_vitoria():
    for i in range(len(jogo)):
        if jogo[0][i] == jogo[1][i] == jogo[2][i] and (jogo[0][i] != " "):
            print("Vitoria!")
            return True
        if jogo[i][0] == jogo[i][1] == jogo[i][2] and (jogo[i][0] != " "):
            print("Vitoria!")
            return True
    if jogo[0][0] == jogo[1][1] == jogo[2][2] and (jogo[0][0] != " "):
        print("Vitoria!")
        return True
    if jogo[0][2] == jogo[1][1] == jogo [2][0] and(jogo[0][2] != " "):
        print("Vitoria!")
        return True
    
def verificar_empate():
    if not any(" " in espacos for espacos in jogo):
        print("Empate!")
        return True

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

        if verificar_vitoria():
            break
        if verificar_empate():
            break
    else:
        print("Um erro ocorreu. Tente novamente.")