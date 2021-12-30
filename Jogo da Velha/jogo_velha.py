blank = " " #valores da matriz/tabela em branca
token  = ["X", "O"] #opçoes de jogada dos jogadores
                    #X sempre começa, pois é a posição 0
#criar tabela, matriz 3x3 em branco
def createBoard():
    board = [
        [blank, blank, blank],
        [blank, blank, blank],
        [blank, blank, blank]
    ]
    return board
#printar tabela, n entendi mt fds, mas a cada iteração do i coloca |
def printBoard(board):
    for i in range(3):
        print("|".join(board[i])) #separar colunas
        if(i<2):
            print("-----") ##separar linhas


#receber o valor das linhas e colunas
def getInputValid(message):
    try:
        n = int(input(message))
        if(n >=1 and n <=3):
            return n - 1
        else:
            print("Value ", n, " invalid")
            return getInputValid(message)
    except:
        print("Value invalid")
        return getInputValid(message)


def checkMotion(board, i , j):
    if(board[i][j] == blank): #se a posição for branca a jogada é feita
        print("Played successfully, next player\n")
        return True
    else:
        print("Occupied position, try again\n") #senao nao ne, ai repete
        return False

def doMotion(board, i, j, player):
    board[i][j] = token[player]
    #pra cada jogada na tabela
    #é inserido o token do jogador(X ou O)
    #na posição escolhida pelo seu respectivo jogador
    #a cada jogada feita, passa a vez para o proximo jogador



def checkWinner(board):
    #linhas
    for i in  range(3):
        if(board[i][0] != blank and board[i][0] == board[i][1] and board[i][1] == board[i][2]):
            return board[i][0]
    #colunas
    for i in range(3):
        if(board[0][i] != blank and board[0][i] == board[1][i] and board[1][i] == board[2][i]):
            return board[0][i]
    #diagonal principal
    if(board[0][0] != blank and board[0][0] == board[1][1]  and board[1][1] == board[2][2]):
        return board[0][0]
    #diagonal secundária
    if (board[0][2] != blank and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        return board[0][2]

    for i in range(3):
        for j in range(3):
            if(board[i][j] == blank):
                    return False
            #se hoouer alguma posição em branco o jogo continua, pois ainda não há vencedor
            #se houver 3 tokens X ou O na posição[i][j], o respectivo jogador é o vencedor
            #saindo do loop naas condiçoes anteriores
            #se não houver linhas em branco deu empate e encerra o jogo
    return "Tie"
