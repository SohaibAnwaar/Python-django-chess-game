
from Piece import Piece


class Queen(Piece):
    '''
    Queen Class inherited from Piece 
    '''
    def canAttack(self,board,piece):
        '''
        Bonus func to check weather a queen can kill other queen 
        '''
        sourceX,sourceY,targetX,targetY=self.x,self.y,piece.x,piece.y
        if sourceX==targetX or sourceY==targetY:
            return True
        elif abs(sourceX-targetX)==abs(sourceY-targetY):
            return True    
        else:
            return False


    def canMove(self,board,x,y):
        '''
     This func will return weather a queen can move to provided x,y or not
     Input: Board and targer co-ordinates
     Output: Boolean result 
     '''
        sourceX,sourceY,targetX,targetY=self.x,self.y,x,y
        #move in same row
        if sourceX==targetX and sourceY!=targetY: 
            return True
        #move in same col    
        elif sourceX!=targetX and sourceY==targetY: 
            return True 
        #diagnonal move        
        elif abs(sourceX-targetX)==abs(sourceY-targetY):  
            return True    
        else:
            return False
