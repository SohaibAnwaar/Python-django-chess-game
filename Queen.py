
from Piece import Piece


class Queen(Piece):
    def canAttack(self,board,piece):
        sourceX,sourceY,targetX,targetY=self.x,self.y,piece.x,piece.y
        if sourceX==targetX or sourceY==targetY:
            return True
        elif abs(sourceX-targetX)==abs(sourceY-targetY):
            return True    
        else:
            return False


    def canMove(self,board,x,y):
        sourceX,sourceY,targetX,targetY=self.x,self.y,x,y
        if sourceX==targetX and sourceY!=targetY:
            return True
        elif sourceX!=targetX and sourceY==targetY:
            return True    
        elif abs(sourceX-targetX)==abs(sourceY-targetY):
            return True    
        else:
            return False
