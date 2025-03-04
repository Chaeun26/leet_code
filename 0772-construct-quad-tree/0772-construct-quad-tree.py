"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def is_uniform(grid, row, col, size):
            first=grid[row][col]
            for r in range(row,row+size):
                for c in range(col,col+size):
                    if grid[r][c]!=first:
                        return False, None
            return True, first

        def build(grid, row=0, col=0, size=None):
            if size is None:
                size=len(grid)
            
            uniform, val = is_uniform(grid, row, col, size)
            if uniform:
                return Node(val, True)

            half = size//2
            topLeft = build(grid,row,col,half)
            topRight = build(grid,row,col+half,half)
            bottomLeft = build(grid,row+half,col,half)
            bottomRight = build(grid,row+half,col+half,half)

            return Node(1,False,topLeft,topRight,bottomLeft,bottomRight)

        return build(grid)