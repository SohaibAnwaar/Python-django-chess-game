
from Knight import Knight
from Rock import Rock
from Pawn import Pawn
from King import King
from Queen import Queen
from Bishop import Bishop
from Box import Box
from Piece import Piece
from termcolor import colored


class Board:
  '''
  This class has board object consisting of boxes and pieces
  '''
  grid=[]
  def __init__(self):
     '''
     This func will initialize all black and white boxes and place all pieces on it
     '''
     #initialize board with alternate box color
     color=1
     for i in range(8):
       templist=[]
       for j in range (8):
          if color==1:
            b=Box('W','')
            templist.append(b)
          elif color==2:
            b=Box('B','')
            templist.append(b)
          if j!=7:
            color=3-color
       self.grid.append(templist)  

      #insert all black pieces to board
     self.grid[0][0].piece=Rock('BR','Black',0,0)
     self.grid[0][1].piece=Knight('BK','Black',0,1)
     self.grid[0][2].piece=Bishop('BB','Black',0,2)
     self.grid[0][3].piece=Queen('QB','Black',0,3)
     self.grid[0][4].piece=King('KB','Black',0,4)
     self.grid[0][5].piece=Bishop('BB','Black',0,5)
     self.grid[0][6].piece=Knight('BK','Black',0,6)
     self.grid[0][7].piece=Rock('BR','Black',0,7)
     for i in range(8):
       self.grid[1][i].piece=Pawn('BP','Black',1,i)
     
      #insert all white pieces to board
     self.grid[7][0].piece=Rock('WR','White',7,0)
     self.grid[7][1].piece=Knight('WK','White',7,1)
     self.grid[7][2].piece=Bishop('WB','White',7,2)
     self.grid[7][3].piece=Queen('QW','White',7,3)
     self.grid[7][4].piece=King('KW','White',7,4)
     self.grid[7][5].piece=Bishop('WB','White',7,5)
     self.grid[7][6].piece=Knight('WK','White',7,6)
     self.grid[7][7].piece=Rock('WR','White',7,7)
     for i in range(8):
       self.grid[6][i].piece=Pawn('WP','White',6,i)



  def putPiece(self,piece):
    '''
     This func will place given piece on a box in board
     Input:Piece Object
     '''
    #creating box object using given piece 
    toPut=Box(self.grid[piece.x][piece.y].color,piece)
    self.grid[piece.x][piece.y]=toPut

  def getPiece(self,x,y):
     '''
     This func will return piece object based on given co-ordinates
     Input: X and Y co-ordinates
     Output: Piece object placed on given X,Y
     '''
     return self.grid[x][y].piece

  def isKingKilled(self,turn):
    '''
     This func will return weather opponent king is killed or not
     Input: Opponent Player's turn
     Output: Boolean result 
     '''

    #initialize assuming kings are killed 
    whiteKing=True
    blackKing=True
    #loop to check all board pieces for existence of kings
    for i in range(8):
      for j in range(8):
        if self.grid[i][j].piece!='':
          if self.grid[i][j].piece.namee=='KB':
           blackKing=False
          if self.grid[i][j].piece.namee=='KW': 
           whiteKing=False
    #output
    if turn==1:
      return whiteKing
    elif turn==2:
      return blackKing      


  def movePiece(self,piece,x,y):
    '''
     This func will move given piece to target co-ordinate killing any piece along way
     Input: Piece object,X and Y co-ordinates
     '''
    #maintain box color 
    color=self.grid[piece.x][piece.y].color 

     #place empty box
    self.grid[piece.x][piece.y]=Box(color,'')

    #place given piece to provided co-ordinates and kill 
    color=self.grid[x][y].color
    piece.x=x
    piece.y=y
    self.grid[x][y]=Box(color,piece)






  def printBoard(self):
    '''
     This func will print board and show all pieces on their positions
     '''
    for i in range(8):
      for j in range(8):
        if self.grid[i][j].piece!='':
         print(' '+self.grid[i][j].piece.namee + ' ',end='')
        elif self.grid[i][j].color=='B':
         print(colored(' __ ','grey'),end='')
        elif self.grid[i][j].color=='W':
         print(colored(' __ ','blue'),end='') 
        #print(self.grid[i][j].color + ' ',end='')   
      print('')      
           

         



      
   

