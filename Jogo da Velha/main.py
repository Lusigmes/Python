from jogo_velha import createBoard, printBoard,\
                getInputValid, checkMotion, doMotion, checkWinner
board = createBoard()
winner = checkWinner(board)
player = 0
while(not winner):
    printBoard(board)
    i = getInputValid("\nType the line: ")
    j = getInputValid("Type the column: ")

    if(checkMotion(board, i, j)):
        doMotion(board, i, j, player)
        player = (player+1)%2
        # quando jogador = 1 -> 1+1 = 2%2= 0 -> vez do jogador 0 = token X
        # quando jogador = 0 -> 0+1  = 1#2 = 1 -> vez do jogdador 1 = token O
        # sempre alternando essas posições a cada movimento
        # sempre alterando os tokens

    winner = checkWinner(board)

if(winner == "Tie"):
    print("="*15)
    printBoard(board)
    print("\nPlayers tied\n")
    print("=" * 15)
else:
    print("+" * 15)
    printBoard(board)
    print("\nPlayer ",winner, " wins!\n")
    print("+" * 15)