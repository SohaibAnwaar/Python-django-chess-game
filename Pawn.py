
from Piece import Piece


class Pawn(Piece):

    """
    Pawn class inherit from Piece
    """

    def canMove(self,board,x,y,turn):

        """
        param x : take the target x-axis coordinate
        param y : take the target y-axis coordinate
        param turn: from 1,2 you will know which player turn it is 1 = White, 2 = Black
        """
        sourceX,sourceY,targetX,targetY=self.x,self.y,x,y

        # turn 1 == white player
        if turn==1:
            """
            check if the source is greater and the subtraction is < 2 and > 0 
            so the pawn can only more one or two steps
            """
            if  sourceX > targetX and (abs(sourceX - targetX) == 1
                                       or abs(sourceX - targetX) == 2):
                return True
            else:
                return False
                # turn 2 == Black player
        elif turn==2:
            # same as white but in opposite direction
            if sourceX < targetX and (abs(sourceX - targetX) == 1
                                      or abs(sourceX - targetX) == 2):
                return True
            else:
                return False 
        
