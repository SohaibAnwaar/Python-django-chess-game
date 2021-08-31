
from Piece import Piece


class King(Piece):

    def canMove(self,board,x,y): #weather a king can move to x,y or not
       pointDffrnc=abs(self.x-x-self.y-y) #diff of src(x,y) and trgt(x,y)
       if pointDffrnc==1: 
           return True
       elif abs(self.x-x)==abs(self.y-y)==1: #diagonal difference of 1
           return True
       else:
           return False        


