
from Piece import Piece


class Pawn(Piece):

    def canMove(self,board,x,y,turn):
        sourceX,sourceY,targetX,targetY=self.x,self.y,x,y
        
        if turn==1:
            if  sourceX > targetX and (abs(sourceX - targetX) == 1 or abs(sourceX - targetX) == 2):
             return True
            else:
                return False 

        elif turn==2:
            if sourceX < targetX and (abs(sourceX - targetX) == 1 or abs(sourceX - targetX) == 2):
                return True
            else:
                return False 
        
