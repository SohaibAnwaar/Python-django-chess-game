
from Box import Box
from Piece import Piece
from termcolor import colored


class Board:
  grid=[]
  def __init__(self):
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
     


  def putPiece(self,piece):
    toPut=Box(self.grid[piece.x][piece.y].color,piece)
    self.grid[piece.x][piece.y]=toPut



  def printBoard(self):
    for i in range(8):
      for j in range(8):
        if self.grid[i][j].piece!='':
         print(self.grid[i][j].piece.namee,end='')
        elif self.grid[i][j].color=='B':
         print(colored('__','grey'),end='')
        elif self.grid[i][j].color=='W':
         print(colored('__','blue'),end='') 
        #print(self.grid[i][j].color + ' ',end='')   
      print('')      
           

         



      
   

