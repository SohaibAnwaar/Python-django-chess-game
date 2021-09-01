
from Piece import Piece


class King(Piece):
    '''
    King Class inherited from Piece 
    '''

    def canMove(self,board,x,y): 
       '''
       This func will return weather a king can move to provided x,y or not
       Input: Board and targer co-ordinates
       Output: Boolean result 
       '''
        #diff of src(x,y) and trgt(x,y) 
       pointDffrnc=abs(self.x-x)+abs(self.y-y) 
       if pointDffrnc==1: 
           return True
       #diagonal difference of 1    
       elif abs(self.x-x)==abs(self.y-y)==1: 
           return True
       else:
           return False        


