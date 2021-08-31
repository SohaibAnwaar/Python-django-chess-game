
from Piece import Piece


class Rock(Piece):

    def canMove(self,board,x,y):
        sourceX,sourceY,targetX,targetY=self.x,self.y,x,y
        if sourceX == targetX or sourceY == targetY:
            return True
        else:
            return False