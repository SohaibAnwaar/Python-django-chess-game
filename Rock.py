
from Piece import Piece


class Rock(Piece):

    """
    Rock class is inherit from Piece
    """

    def canMove(self,board,x,y):

        """
        param x : take the target x-axis coordinate
        param y : take the target y-axis coordinate
        """

        sourceX,sourceY,targetX,targetY=self.x,self.y,x,y
        # check only rock can move in four directions forward, backward, left, right
        if sourceX == targetX or sourceY == targetY:
            return True
        else:
            return False