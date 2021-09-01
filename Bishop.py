
from Piece import Piece


class Bishop(Piece):

    def canMove(self,board,x,y): #weather bishop can move to x,y or not
       if abs(self.x-x)==abs(self.y-y): #diagonal move check
           return True
       else:
           return False        


