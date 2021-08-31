
from Queen import Queen
from Player import Player
from Board import Board
class Game:

  def canQueenKill(self):
    print('Welcome to Chess by Mujahid')
    board=Board()
    print('Enter position(x,y) of black queen')
    bQ=input()
    bQ=bQ.split(',')
    print('Enter position(x,y) of white queen')
    wQ=input()
    wQ=wQ.split(',')
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
   # print('Player 1 Please Enter your name')
   # name1=input()
   # print('Player 2 Please Enter your name')
   # name2=input()
   # player1=Player(name1,0)
   # player2=Player(name2,0)
   # print(player1.name + ' and ' +player2.name +' are playing now')
    self.canQueenKill()

