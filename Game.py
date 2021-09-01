
from Pawn import Pawn
from Queen import Queen
from Player import Player
from Board import Board
class Game:
  '''
  Main Class having all game logic
  '''

  def canQueenKill(self): 
    print('Welcome to Chess by Mujahid')
    board=Board()
    print('Enter position(x,y) of black queen')
    bQ=input().split(',')
    print('Enter position(x,y) of white queen')
    wQ=input().split(',')
    blackQueen=Queen('BQ','Black',int(bQ[0]),int(bQ[1]))
    whiteQueen=Queen('WQ','White',int(wQ[0]),int(wQ[1]))
    board.putPiece(blackQueen)
    board.putPiece(whiteQueen)
    board.printBoard()
    if blackQueen.canAttack(board,whiteQueen):
      print('Yes Then can attack!')
    else:
      print('No They can not attack') 

  def play(self):
    '''
    Main func creating game flow and having all game objects,rules etc
    '''
    print('Welcome to Chess by Mujahid')

    #get user names
    print('Player 1 Please Enter your name')
    name1=input()
    print('Player 2 Please Enter your name')
    name2=input()

    #initialze player objects
    player1=Player(name1,0)
    player2=Player(name2,0)
    print(player1.name + ' and ' +player2.name +' are playing now')

    #initialize Board 
    board=Board() 
    #set turn for white player
    turn=1

    #game loop started
    while True:
      try:
        if turn==1:
          print(player1.name + "'s Turn (white)")
        elif turn==2:
          print(player2.name + "'s Turn (black)")

        #show current board with all pieces
        board.printBoard()  

        #gettig user input for source and target position
        print('Please enter "X1,Y1,X2,Y2" ')
        x1,y1,x2,y2=input().split(',')
        x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)

        #get current and target piece from board based on given x,y
        currentPiece=board.getPiece(x1,y1)
        targetPiece=board.getPiece(x2,y2)

        #check if target box has same color piece
        if targetPiece!='' and currentPiece.color==targetPiece.color:
          print('Cant kill your own soldier')
          continue

        #getting type of Piece
        pieceType=type(currentPiece)

        #pawn spcific check as pawn can only move forward
        if pieceType==Pawn:
          if currentPiece.canMove(board,x2,y2,turn):
            board.movePiece(currentPiece,x2,y2)
            #game end condition check
            if board.isKingKilled(3-turn)==True:
             break
            #changing turn
            turn=3-turn
          else:
            print('Not a valid move. Try again') 

        #for all other pieces
        elif currentPiece.canMove(board,x2,y2):
          board.movePiece(currentPiece,x2,y2)
           #game end condition check
          if board.isKingKilled(3-turn)==True:
            break 
          #changing turn
          turn=3-turn
        else:
          print('Not a valid move. Try again')
        
      except Exception as e:
        print(e)  

     #ending game and show winner
    if turn==1:
          print(player1.name + " Won (white)")
    elif turn==2:
          print(player2.name + " Won (black)")    





    

