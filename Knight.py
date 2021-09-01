
from Piece import Piece


class Knight(Piece):


    def canMove(self,board,x,y):
        sourceX, sourceY, targetX, targetY = self.x, self.y, x, y
        if sourceX > targetX and sourceY > targetY:
            if  (targetX - sourceX) == -2 
            and (targetY - sourceY) == -1 
            or  (targetX - sourceX) == -1 
            and (targetY - sourceY) == -2:

                return True
        elif sourceX < targetX and sourceY > targetY:
            if (targetX - sourceX) == 2 and (targetY - sourceY) == -1 or (targetX - sourceX) == 1 and (targetY - sourceY) == -2:
                return True
        elif sourceX < targetX and sourceY < targetY:
            if (targetX - sourceX) == 2 and (targetY - sourceY) == 1 or (targetX - sourceX) == 1 and (targetY - sourceY) == 2:
                return True
        elif sourceX > targetX and sourceY < targetY:
            if (targetX - sourceX) == -2 and (targetY - sourceY) == 1 or (targetX - sourceX) == -1 and (targetY - sourceY) == 2:
                return True
        else:
            return False
