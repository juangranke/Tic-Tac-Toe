import time

box = [
    [[], [], []],
    [[], [], []],
    [[], [], []]
]


def start():
    print('-=' * 20)
    print("JOGO DA VELHA".center(40))
    print('-=' * 20)


def tabela():
    for valor, item in enumerate(box):
        print(item)


global numero
jogador = "x"


mudar_jogador = 0
jogador1 = "x"
jogador2 = "o"
fim = 0


def jogar_novamente():
    pass


def ganhar():
    global fim
    # Horizontal 1
    if box[0][0] == "x" and box[0][1] == "x" and box[0][2] == "x":
        print("Jogador 1 venceu a partida!")
        fim = 1
    # Horizontal 2
    elif box[1][0] == "x" and box[1][1] == "x" and box[1][2] == "x":
        print("Jogador 1 venceu a partida!")
        fim = 1
    # Horizontal 3
    elif box[2][0] == "x" and box[2][1] == "x" and box[2][2] == "x":
        print("Jogador 1 venceu a partida!")
        fim = 1
    # Vertical 1
    elif box[0][0] == "x" and box[1][0] == "x" and box[2][0] == "x":
        print("Jogador 1 venceu a partida!")
        fim = 1
    # Vertical 2
    elif box[0][1] == "x" and box[1][1] == "x" and box[2][1] == "x":
        print("Jogador 1 venceu a partida!")
        fim = 1
    # Vertical 3
    elif box[0][2] == "x" and box[1][2] == "x" and box[2][2] == "x":
        print("Jogador 1 venceu a partida!")
        fim = 1
    # Diagonal \
    elif box[0][0] == "x" and box[1][1] == "x" and box[2][2] == "x":
        print("Jogador 1 venceu a partida!")
        fim = 1
    # Diagonal /
    elif box[2][0] == "x" and box[1][1] == "x" and box[0][2] == "x":
        print("Jogador 1 venceu a partida!")
        fim = 1



    # Horizontal 1
    if box[0][0] == "o" and box[0][1] == "o" and box[0][2] == "o":
        print("Jogador 2 venceu a partida!")
        fim = 1
    # Horizontal 2
    elif box[1][0] == "o" and box[1][1] == "o" and box[1][2] == "o":
        print("Jogador 2 venceu a partida!")
        fim = 1
    # Horizontal 3
    elif box[2][0] == "o" and box[2][1] == "o" and box[2][2] == "o":
        print("Jogador 2 venceu a partida!")
        fim = 1
    # Vertical 1
    elif box[0][0] == "o" and box[1][0] == "o" and box[2][0] == "o":
        print("Jogador 2 venceu a partida!")
        fim = 1
    # Vertical 2
    elif box[0][1] == "o" and box[1][1] == "o" and box[2][1] == "o":
        print("Jogador 2 venceu a partida!")
        fim = 1
    # Vertical 3
    elif box[0][2] == "o" and box[1][2] == "o" and box[2][2] == "o":
        print("Jogador 2 venceu a partida!")
        fim = 1
    # Diagonal \
    elif box[0][0] == "o" and box[1][1] == "o" and box[2][2] == "o":
        print("Jogador 2 venceu a partida!")
        fim = 1
    # Diagonal /
    elif box[2][0] == "o" and box[1][1] == "o" and box[0][2] == "o":
        print("Jogador 2 venceu a partida!")
        fim = 1
    else:
        pass


def lincol():
    print("\n")
    try:
        global mudar_jogador
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))
        if not bool(box[linha - 1][coluna - 1]):
            if (mudar_jogador % 2) == 0:
                box[linha - 1][coluna - 1] = jogador1
                ganhar()
            else:
                box[linha - 1][coluna - 1] = jogador2
                ganhar()
            mudar_jogador += 1
        else:
            print("Preencha um campo vazio.\n")
    except:
        print("Preencha o campo corretamente!")


start()
while True:
    lincol()
    tabela()
    if fim == 1:
        print("Fim do jogo!")
        time.sleep(3)
        break