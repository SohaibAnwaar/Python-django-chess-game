
from Queen import Queen
from Player import Player
from Board import Board
class Game:

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
    print('Welcome to Chess by Mujahid')
    print('Player 1 Please Enter your name')
    name1=input()
    print('Player 2 Please Enter your name')
    name2=input()
    player1=Player(name1,0)
    player2=Player(name2,0)
    print(player1.name + ' and ' +player2.name +' are playing now')
    board=Board() #initialize Board 
    board.putPiece(Queen('WQ','White',2,2))#just for testing
    turn=1
    #game started
    while True:
     if turn==1:
       print(player1.name + "'s Turn")
     elif turn==2:
       print(player2.name + "'s Turn")
     board.printBoard()  
     print('Please enter "X1,Y1,X2,Y2" ')
     x1,y1,x2,y2=input().split(',')
     x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)
     currentPiece=board.getPiece(x1,y1)
     if currentPiece.canMove(board,x2,y2):
       board.movePiece(currentPiece,x2,y2)
       turn=3-turn#changing turn
     else:
       print('Not a valid move. Try again')





    

