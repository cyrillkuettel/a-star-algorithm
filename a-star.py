from node import node


class AStar:

    def __init__(self, start: node, end: node):
        pass

    def g(self, n: node):   # calculate h-cost
        """
         g : the cost of moving from the initial cell to the current cell. Basically, it is the sum of all the cells that
         have been visited since leaving the first cell.
        """
