
from Piece import Piece


class Bishop(Piece):
    '''
    Bishop Class inherited from Piece 
    '''

    def canMove(self,board,x,y):
       '''
       This func will return weather a bishop can move to provided x,y or not
       Input: Board and targer co-ordinates
       Output: Boolean result 
       '''
       #diagonal move check
       if abs(self.x-x)==abs(self.y-y): 
           return True
       else:
           return False        


