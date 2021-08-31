
from Piece import Piece


class Pawn(Piece):

    def canMove(self,board,x,y):
        sourceX,sourceY,targetX,targetY=self.x,self.y,x,y
        if sourceX == targetX and sourceX < targetX and ((sourceX - targetX) == 1 or (sourceX - targetX) == 2):
            print("true")
            return True
        else:
            return False
