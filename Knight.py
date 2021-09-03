
from Piece import Piece


class Knight(Piece):

    """
    Knight class inherit from Piece
    """

    def canMove(self,board,x,y):
        """
        param x : take the target x-axis coordinate
        param y : take the target y-axis coordinate
        """
        sourceX, sourceY, targetX, targetY = self.x, self.y, x, y


        """
        since Knight can move only in L shape so that means it can be divide
        into four coordinates     |
                               ++ | +-   
                            -------------
                               -+ | --
                                  |
        from that we can understand and we can predict the next moves
        """

        # -- side
        if sourceX > targetX and sourceY > targetY:
            if  (targetX - sourceX) == -2 \
                    and (targetY - sourceY) == -1 \
                    or  (targetX - sourceX) == -1 \
                    and (targetY - sourceY) == -2:

            return True

        # +- side
        elif sourceX < targetX and sourceY > targetY:
            if (targetX - sourceX) == 2 and (targetY - sourceY) == -1 \
                    or (targetX - sourceX) == 1 and (targetY - sourceY) == -2:
                return True
        # ++ side
        elif sourceX < targetX and sourceY < targetY:
            if (targetX - sourceX) == 2 and (targetY - sourceY) == 1 \
                    or (targetX - sourceX) == 1 and (targetY - sourceY) == 2:
                return True
        # -+ side
        elif sourceX > targetX and sourceY < targetY:
            if (targetX - sourceX) == -2 and (targetY - sourceY) == 1 \
                    or (targetX - sourceX) == -1 and (targetY - sourceY) == 2:
                return True
        else:
            return False
